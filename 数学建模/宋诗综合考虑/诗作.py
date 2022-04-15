import json
import os

path= r'../song'
files=os.listdir(path)
for file in files:
    with open(f'./song/{file}','r',encoding='utf-8') as fp:
        json_data=json.load(fp)
    for item in json_data:
        a=item['paragraphs']
        with open ('song.txt', 'a', encoding='utf-8') as fp:
            fp.write(''.join(a)+'\n')
