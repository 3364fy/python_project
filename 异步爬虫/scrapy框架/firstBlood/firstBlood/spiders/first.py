import scrapy
class FirstSpider(scrapy.Spider):
    name = 'first'
    #allowed_domains = ['www.xxxx.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response, **kwargs):
        div_list=response.xpath('')
        all_data=[]
        for div in div_list:
            author=div.xpath('./text()').extract()
            content=div.xpath('./text()').extract()
            content=''.join(content)
            dic={
                'author':author,
                'content':content
            }
            all_data.append(dic)
        return all_data

