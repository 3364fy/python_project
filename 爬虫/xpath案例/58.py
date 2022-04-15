import requests
from lxml import etree
if __name__ == '__main__':
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/11'
    }
    url='https://bj.58.com/ershoufang/'
    page_text=requests.get(url=url,headers=header).text
    tree=etree.HTML(page_text)
    div_list=tree.xpath('//section[@class="list"]/div')
    for div in div_list:
        title=div.xpath('./a/div[@class="property-content"]/div/div/h3/text()')[0]
        print(title)