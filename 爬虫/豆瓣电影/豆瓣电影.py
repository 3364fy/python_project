import requests
import json
if __name__ == '__main__':
    url='https://movie.douban.com/j/chart/top_list'
    param={
        'type': '24',
        'interval_id': '100:90',
        'action':'',
        'start': '0',
        'limit': '20'
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/11'
    }
    response=requests.get(url=url,params=param,headers=header)
    list_data=response.json()
    fp=open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)#中文不能用ASCII编译
    print('保存成功')
