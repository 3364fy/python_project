import requests
import re
import os
#ex='(?<=标签).*?(?=标签)'
if __name__ == '__main__':
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/11'
    }
    url='https://www.qiushibaike.com/imgrank/'
    page_text=requests.get(url=url,headers=header).text
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list=re.findall(ex,page_text,re.S)
    for src in img_src_list:
        src='https:'+src
        img_data=requests.get(url=src,headers=header).content
        img_name=src.split('/')[-1]
        img_Path='./qiutuLibs/'+img_name
        with open(img_Path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功')

