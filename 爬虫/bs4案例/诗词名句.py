import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/11'
    }
    url='http://www.shicimingju.com/book/sanguoyanyi.html'
    page_text=requests.get(url=url,headers=header).content
    soup=BeautifulSoup(page_text,'lxml')
    li_list=soup.select('.book-mulu > ul > li')
    fp=open('E:/sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title=li.a.string
        detail_url='https://www.shicimingju.com'+li.a['href']
        detail_page_text = requests.get(url=detail_url, headers=header).content
        detail_soup=BeautifulSoup(detail_page_text,'lxml')
        div_tag=detail_soup.find('div',class_='chapter_content')
        content=div_tag.text
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功')
