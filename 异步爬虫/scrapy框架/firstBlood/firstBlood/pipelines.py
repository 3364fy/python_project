# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class FirstbloodPipeline:
    fp=None
    #重写父类方法，该方法只在开始爬虫的时候被调用一次
    def open_spider(self,spider):
        print('开始爬虫......')
        self.fp=open('./a.txt','w',encoding='utf-8')
    def process_item(self, item, spider):
        author=item['author']
        content=item['content']
        self.fp.write(author+':'+content+'\n')
        return item

    def close_spider(self, spider):
        print('结束爬虫！！！')
        self.fp.close()
class MySqlPipeLine():
    coon=None
    cursor=None
    def open_spider(self,spider):
        self.coon=pymysql.Connect(host="localhost",user="root",password="33649464",database="ll",charset='utf-8')
    def process_item(self, item, spider):
        self.cursor=self.coon.cursor()
        try:
            self.cursor.execute('insert into ll values("%s","%s")'%(item["author"],item["content"]))
            self.coon.commit()
        except Exception as e:
            print(e)
            self.coon.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.coon.close()

