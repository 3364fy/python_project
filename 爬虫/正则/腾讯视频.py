import requests
import re
import os
if __name__ == '__main__':
    if not os.path.exists('D:/txsp'):
        os.mkdir('D:/txsp')
    try:
        a=int(input('请输入页码(只能输入正整数呦)：'))
        if a==1:
            header={
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/11'
            }
            url='https://v.qq.com/channel/tv'
            page_text=requests.get(url=url,headers=header).text
            ex = '/uploads/allimg/.+?jpg'
            img_src_list=re.findall(ex,page_text,re.S)
            for src in img_src_list:
                src='https://pic.netbian.com'+src
                img_data=requests.get(url=src,headers=header).content
                img_name=src.split('/')[-1]
                img_Path='D:/txsp/'+img_name
                with open(img_Path,'wb') as fp:
                    fp.write(img_data)
                    print(img_name,'下载成功')
        else:
            '''header={
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/11'
            }
            url=f'https://pic.netbian.com/index_{a}.html'
            page_text=requests.get(url=url,headers=header).text
            ex = '/uploads/allimg/.+?jpg'
            img_src_list=re.findall(ex,page_text,re.S)
            for src in img_src_list:
                src='https://pic.netbian.com'+src
                img_data=requests.get(url=src,headers=header).content
                img_name=src.split('/')[-1]
                img_Path='D:/bizhiLibs/'+img_name
                with open(img_Path,'wb') as fp:
                    fp.write(img_data)
                    print(img_name,'下载成功')'''
    except:
        print('输入错误')