import json
import os
path= r'../song'
files=os.listdir(path)
b=[]
for file in files:
    with open(f'./song/{file}','r',encoding='utf-8') as fp:
        json_data=json.load(fp)
    for item in json_data:
        a=item['author']
        b.append(a)
        #c.update(a)
        # with open ('./s_author.txt','a',encoding='utf-8') as fp:
        #     fp.write(''.join(a)+'\n')
#print(b,end='=============================================================================================')
c=set(b)
dict={}
for i in c:
    dict.update({i: b.count(i)})
with open ('./s_author.txt','a',encoding='utf-8') as fp:
    fp.write(str(dict))
print(dict.values())

e={}
for author in dict:
    if dict[author]>=1000:
        e[author]=dict[author]
print(e)
print(len(e))
with open ('./s_author.txt','a',encoding='utf-8') as fp:
    fp.write(str(e))