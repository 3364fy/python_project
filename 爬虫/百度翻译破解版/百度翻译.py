import requests
import json
if __name__ == '__main__':
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/11'
    }
    url='https://fanyi.baidu.com/sug'
    word=input('enter a word:')
    param={'kw':word}
    response=requests.post(url=url,params=param,headers=header)
    dic_obj=response.json()
    fileName=word+'.html'
    fp=open('./dog.json','w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)#中文不能用ASCII编译
    print(fileName,'保存成功')
