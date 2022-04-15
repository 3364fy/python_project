import jieba
txt = open(r"../../宋诗综合考虑/song.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)#进行分词处理并形成列表
counts = {}#构造字典，逐一遍历words中的中文单词进行处理，并用字典计数
for word in words:
    counts[word] = counts.get(word, 0) + 1 #获取到的词在字典中寻找如果有的话在原来的基础上+1，如果没有就收录到字典中
items = list(counts.items())#转换列表类型并排序
items.sort(key=lambda x:x[1], reverse=True)
cipin=[]
for i in range(1000):#输出前15位单词
    word, count = items[i]
    cipin.append(word)
with open('s词频1000.txt', 'a', encoding='utf-8') as fp:
    fp.write(str(cipin))