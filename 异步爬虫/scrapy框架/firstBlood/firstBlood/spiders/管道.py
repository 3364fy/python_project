import scrapy
from firstBlood.item import FirstbloodItem
class FirstSpider(scrapy.Spider):
    name = 'first'
    #allowed_domains = ['www.xxxx.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response, **kwargs):
        div_list=response.xpath('')
        all_data=[]
        for div in div_list:
            author=div.xpath('./text()').extract()
            content=div.xpath('./text()').extract()
            content=''.join(content)
            item=FirstbloodItem()
            item['author']=author
            item['content']=content
            yield item