import json
import os

#唐诗
path= '../song'
files=os.listdir(path)
for file in files:
    with open(f'{path}/{file}','r',encoding='utf-8') as fp:
        json_data=json.load(fp)
    for item in json_data:
        author=item['author']
        # if not os.path.exists(f'./唐诗/{author}'):
        #     try:
        #         os.mkdir(f'./唐诗/{author}')
        #     except:
        #         author=author[0]
        #         os.mkdir(f'./唐诗/{author}')
        a=item['paragraphs']
        title=item['title']
        try:
            if not os.path.exists(f'训练诗集/{author}'):
                os.mkdir(f'训练诗集/{author}')
            with open (rf'训练诗集/{author}/{title}.txt','w',encoding='utf-8') as fp:
                fp.write(''.join(a)+'\n')
        except:
            c=''.join(a)
            if not os.path.exists(f'训练诗集/无名'):
                os.mkdir(f'训练诗集/无名')
            with open (rf'训练诗集/无名/{c[0:7]}.txt','w',encoding='utf-8') as fp:
                fp.write(''.join(a)+'\n')

