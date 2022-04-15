import requests
if __name__ == '__main__':
    url='https://www.sougou.com/web'
    kw=input('enter a word:')
    param={'query':kw}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/11'
    }
    response=requests.post(url=url,params=param,headers=header)
    page_text=response.text
    print(page_text)
    fileName=kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功')
