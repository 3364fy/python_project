import json
import os
t_exc={'姚合': 537, '張祜': 639, '杜牧': 557, '李白': 1258, '易靜': 1278, '許渾': 551, '錢起': 551, '不詳': 1778, '王建': 584, '劉禹錫': 906, '貫休': 798, '陸龜蒙': 652, '王梵志': 627, '皎然': 500, '羅隱': 549, '白居易': 3106, '李商隱': 629, '孟郊': 538, '無名氏': 971, '劉長卿': 542, '元稹': 970, '杜甫': 1507, '韋應物': 599, '齊己': 866}
authors=[]
for author in t_exc:
   authors.append(author)
path= r'../tang'
files=os.listdir(path)
for file in files:
    with open(f'../tang/{file}','r',encoding='utf-8') as fp:
        json_data=json.load(fp)
    for item in json_data:
        if item['author'] in authors:
            a=item['paragraphs']
            with open ('./t_exc_poet.txt', 'a', encoding='utf-8') as fp:
                fp.write(''.join(a)+'\n')