import requests
from lxml import etree
import re
from multiprocessing.dummy import Pool
if __name__ == '__main__':
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/11'
    }
    url='https://www.pearvideo.com/category_5'
    page_text=requests.get(url=url,headers=header).text
    tree=etree.HTML(page_text)
    li_list=tree.xpath('//ul[@class="listvideo-list clearfix"]/li')
    urls=[]
    for li in li_list:
        title=li.xpath('./div/a/div[2.csv]/text()')[0]+'.mp4'
        detail_url='https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
        mum=li.xpath('./div/a/@href')[0]
        num=mum.split('_')[-1]
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/11',
            'Referer': detail_url
        }
        puls_url=f'https://www.pearvideo.com/videoStatus.jsp?contId={num}'
        detail_page_text=requests.get(url=puls_url,headers=headers).text
        ex='https://video.+mp4'
        video_url=re.findall(ex,detail_page_text)[0]
        url_lst=video_url.split('/')
        num_2=url_lst[6]
        num_3=url_lst[4]
        num_4=url_lst[5]
        ex2='-\d{8}.+?hd.mp4'
        num_5=re.findall(ex2,num_2)[0]
        url_2=f'https://video.pearvideo.com/mp4/{num_3}/{num_4}/cont-{num}{num_5}'
        dic={
            'title':title,
            'url':url_2
        }
        urls.append(dic)
    def fy(dic):
        url=dic['url']
        print(dic['title'],'正在下载')
        content = requests.get(url=url, headers=header).content
        with open('E:/视频/python/' + dic['title'], 'wb') as fp:
            fp.write(content)
            print(dic['title'],'下载成功')
    pool=Pool(4)
    pool.map(fy,urls)

    pool.close()
    pool.join()


