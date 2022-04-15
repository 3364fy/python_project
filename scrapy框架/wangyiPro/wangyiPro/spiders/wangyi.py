import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    #allowed_domains = ['news.163.com']
    start_urls = ['http://news.163.com/']
    #Store the URLs of the five sections corresponding to the details page
    models_urls=[]
    #Parse the url of the details page corresponding to the five major sections

    #Instantiate a browser object
    def __init__(self):
        self.bro=webdriver.Chrome(executable_path='E:\python项目\淘宝\淘宝模拟登陆\chromedriver.exe')

    def parse(self, response, **kwargs):
        li_list=response.xpath('//*[@id="index2016_wrap"]/div[3]/div[2.csv]/div[2.csv]/div[2.csv]/div/ul/li')
        alist=[3,4,6,7,8]
        for index in alist:
            mode_url=li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(mode_url)
            #Request the page corresponding to each section in turn
            for url in self.models_urls:
                yield scrapy.Request(url,callback=self.parse_model)

    # Parse the title of the corresponding news in each section page and the url of the news details page
    def parse_model(self,response):
        div_list=response.xpath('/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title=div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url=div.xpath('./div/div[1]/h3/a/@href').extract_first()

            item=WangyiproItem()
            item['title']=title

            yield scrapy.Request(url=new_detail_url,callback=self.parse_detail,meta={'item':item})
    #解析新闻内容
    def parse_detail(self, response):
        content=response.xpath('//*[@id="content"]/div[2.csv]//text()').extract()
        content=''.join(content)
        item=response.meta['item']
        item['content'] = content

        yield item

    def closed(self,spider):
        self.bro.quit()
