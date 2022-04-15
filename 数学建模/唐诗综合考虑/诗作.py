import json
import os

#唐诗
path=r'../tang'
files=os.listdir(path)
for file in files:
    with open(f'./tang/{file}','r',encoding='utf-8') as fp:
        json_data=json.load(fp)
    for item in json_data:
        a=item['paragraphs']
        with open ('./tang.txt','a',encoding='utf-8') as fp:
            fp.write(''.join(a)+'\n')

