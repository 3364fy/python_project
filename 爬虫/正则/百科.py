import requests
import re
import os
url='https://baike.baidu.com/item/%E6%9C%80%E5%B0%8F%E4%BA%8C%E4%B9%98%E6%B3%95/2522346?fr=aladdin'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/11'
}
response=requests.get(url=url,headers=header)
page_text=response.text
ex='http.?://?.{1,100}svg'
img_src_list=re.findall(ex,page_text,re.S)
if not os.path.exists('./baike'):
    os.mkdir('./baike')
a=1
for img in img_src_list:
    img_name = img.split('svg')[:-1]
    print(img_name[0])
    src = img_name[0]+'png'
    img_data = requests.get(url=src, headers=header).content
    img_Path = './baike/' + f'{a}.png'
    with open(img_Path, 'wb') as fp:
        fp.write(img_data)
        print(f'{a}.png', '下载成功')
    a+=1

