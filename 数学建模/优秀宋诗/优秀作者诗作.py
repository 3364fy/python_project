import json
import os
s_exc={'白玉蟾': 1206, '蘇軾': 2925, '周紫芝': 1904, '王安石': 1744, '彭汝礪': 1177, '呂本中': 1359, '楊萬里': 4295, '韓維': 1029, '吳芾': 1150, '陳造': 2039, '韋驤': 1176, '方回': 3072, '釋正覺': 1302, '項安世': 1546, '范成大': 1949, '蘇轍': 1854, '劉克莊': 4736, '劉攽': 1280, '趙蕃': 3735, '宋祁': 1599, '方岳': 1427, '許及之': 1091, '樓鑰': 1245, '郭祥正': 1449, '張耒': 2275, '釋文珦': 1048, '釋居簡': 1664, '韓淲': 2632, '李綱': 1610, '釋印肅': 1125, '陳著': 1319, '洪咨夔': 1003, '陸游': 9277, '張鎡': 1055, '王十朋': 2193, '梅堯臣': 2940, '邵雍': 1574, '司馬光': 1268, '釋德洪': 1860, '黄庭堅': 2222, '劉敞': 1733, '郊廟朝會歌辭': 1641, '朱熹': 1468, '曹勛': 1329}
authors=[]
for author in s_exc:
   authors.append(author)
path= r'../song'
files=os.listdir(path)
for file in files:
    with open(f'../song/{file}','r',encoding='utf-8') as fp:
        json_data=json.load(fp)
    for item in json_data:
        if item['author'] in authors:
            a=item['paragraphs']
            with open ('./s_exc_poet.txt', 'a', encoding='utf-8') as fp:
                fp.write(''.join(a)+'\n')