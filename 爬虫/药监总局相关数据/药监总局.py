import requests
import json
if __name__ == '__main__':
    url='http://scxk.nmpa.gov.cn:81/xk/ '
    data={
        'on':'true',
        'page':'1',
        'pageSize':'15',
        'productName':'',
        'conditionType':'1',
        'applyname':'',
        'applysn':''
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/11'
    }
    id_list=[]
    all_data_list=[]
    response=requests.post(url=url,data=data,headers=headers)
    json_ids=response.json()
    for dic in json_ids['list']:
        id_list.append(dic['ID'])
    post_url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    for id in id_list:
        post_data={
            'id':id
        }
        detail_json=requests.post(url=post_url,data=post_data,headers=headers).json()
        print(detail_json)
        all_data_list.append(detail_json)
    fp = open('./all_data.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)


