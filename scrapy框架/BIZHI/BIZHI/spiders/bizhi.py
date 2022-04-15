import scrapy
from BIZHI.items import BizhiItem
import time
class BizhiSpider(scrapy.Spider):
    name = 'bizhi'
    #allowed_domains = ['pic.netbian.com']
    start_urls = ['http://pic.netbian.com/']
    page_mumber=2

    def parse(self, response, **kwargs):
        li_list=response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_list:
            li='https://pic.netbian.com/'+li.xpath('./a/img/@src | ./a/span/img/@src').extract_first()
            item = BizhiItem()
            item['li']=li
            yield item
        if self.page_mumber<=10:
            new_url=f'https://pic.netbian.com/index_{self.page_mumber}.html'
            self.page_mumber+=1
            yield scrapy.Request(url=new_url,callback=self.parse,meta={'item':item})