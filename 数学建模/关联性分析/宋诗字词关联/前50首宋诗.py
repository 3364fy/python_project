with open('s词频1000.txt', 'r', encoding='utf-8') as fp:
    words=eval(fp.readlines()[0])
# a=[]
# for line in open("../../唐诗综合考虑/tang.txt", encoding='utf-8'):
#     dic={}
#     num=0
#     for word in words:
#         if word in line:
#             num+=1
#     dic[line]=num
#     a.append(dic)
# print(a)

b=[]
for line in open("../../宋诗综合考虑/song.txt", encoding='utf-8'):
    dic={}
    num=0
    for word in words:
        if word in line:
            num+=1
    dic[num]=line
    b.append(dic)

c=[]
for dict in b:
    for key in dict:
        c.append(key)
c.sort()
print(c[-50:-1])
for dict in b:
    #print(dict)
    for key in dict:
        #print(key)
        if key in c[-50:-1]:
            #print(dict[key])
            with open('../宋诗字词关联/s50.txt','a',encoding='utf-8') as fp:
                fp.write(dict[key])