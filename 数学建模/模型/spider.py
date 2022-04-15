import json
import os

#唐诗
path= '../tang'
files=os.listdir(path)
for file in files:
    with open(f'../tang/{file}','r',encoding='utf-8') as fp:
        json_data=json.load(fp)
    for item in json_data:
        # author=item['author']
        # if not os.path.exists(f'./唐诗/{author}'):
        #     try:
        #         os.mkdir(f'./唐诗/{author}')
        #     except:
        #         author=author[0]
        #         os.mkdir(f'./唐诗/{author}')
        a=item['paragraphs']
        title=item['title']
        try:
            with open (rf'训练诗集/唐诗/{title}.txt','w',encoding='utf-8') as fp:
                fp.write(''.join(a)+'\n')
        except:
            c=''.join(a)
            with open (rf'训练诗集/唐诗/{c[0:7]}.txt','w',encoding='utf-8') as fp:
                fp.write(''.join(a)+'\n')

# #宋诗
# path= '../song'
# files=os.listdir(path)
# for file in files:
#     with open(f'../song/{file}','r',encoding='utf-8') as fp:
#         json_data=json.load(fp)
#     for item in json_data:
#         # author=item['author']
#         # try:
#         #     if not os.path.exists(f'./宋诗/{author}'):
#         #         os.mkdir(f'./宋诗/{author}')
#         # except:
#         #     author = '无名'
#         #     if not os.path.exists(f'./宋诗/{author}'):
#         #         os.mkdir(f'./宋诗/{author}')
#         a=item['paragraphs']
#         title=item['title']
#         try:
#             with open (rf'训练诗集/宋诗/{title}.txt','w',encoding='utf-8') as fp:
#                 fp.write(''.join(a)+'\n')
#         except:
#             c = ''.join(a)
#             with open(rf'训练诗集/宋诗/{c[0:7]}.txt', 'w', encoding='utf-8') as fp:
#                 fp.write(''.join(a) + '\n')
