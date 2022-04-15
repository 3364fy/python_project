import os
import jieba

authors=['孟浩然','李白','杜甫','高適','陸游','戴復古','李清照']
for author in authors:
    # if not os.path.exists(author):
    #     os.makedirs(author)
    try:
        path=f'all_poets/唐诗/{author}'
        poets = os.listdir(path)
        #print(path)
    except:
        path=f'all_poets/宋诗/{author}'
        poets = os.listdir(path)
        #print(path)
    for poet in poets:
        with open(f'{path}/{poet}','r',encoding='utf-8') as fp:
            content=fp.readlines()
            txt=''.join(content)
            # print(txt)
            with open(f'风格诗集/{author}.txt', 'a', encoding='utf-8') as fp:
                fp.write(txt)
