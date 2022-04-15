import requests
import json

if __name__ == "__main__":
    # 获取企业id数据
    url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    id_list = []  # 用来存储获取到的id值
    all_detail_list = []  # 用来存储所有的企业详情数据
    for page in range(1, 3):  # 遍历所有页中的公司
        page = str(page)
        data = {
            'on': ' true',
            'page': page,
            'pageSize': ' 15',
            'productName': '',
            'conditionType': ' 1',
            'applyname': '',
            'applysn': '',
        }
        json_ids = requests.post(url=url, headers=headers, data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
            # print(id_list)
    # 接下来获取企业详情页
    post_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id': id
        }
        detail_list = requests.post(url=post_url, data=data, headers=headers).json()
        all_detail_list.append(detail_list)
    # 永久化存储
    fp = open('./yaojianju.json', 'w', encoding='utf-8')
    json.dump(all_detail_list, fp=fp, ensure_ascii=False)
    print('over!!')
