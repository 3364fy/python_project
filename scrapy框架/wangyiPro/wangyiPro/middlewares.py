# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
from time import sleep

class WangyiproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None
    #Intercept the response objects corresponding to the five major sections and tamper with them
    def process_response(self, request, response, spider):
        #获取了在爬虫类中定义的浏览器对象
        bro=spider.bro
        #Pick out the specified response object for tampering
        #Specify request by url
        #Specify response by request
        if request.url in spider.models_urls:
            bro.get(request.url)#对五个板块对应的url进行请求发送
            sleep(2)
            page_text=bro.page_source#包含了动态加载的新闻数据
            #response #五大板块对应的响应对象
            #针对这些定位到的response进行篡改
            #实例化一个新的响应对象（符合需求：包含动态加载出的新闻数据），替代原来旧的响应对象
            new_response=HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)
            return new_response
        else:
            return response


    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
