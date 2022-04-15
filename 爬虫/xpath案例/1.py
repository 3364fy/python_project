import requests
from lxml import etree
if __name__ == '__main__':
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/11'
    }
    url='https://z1.m1907.cn/?jx=%E6%B8%A9%E5%B7%9E%E4%B8%80%E5%AE%B6%E4%BA%BA'
    page_text=requests.get(url=url,headers=header).content
    with open('a.mp4','wb') as fp:
        fp.write(page_text)
