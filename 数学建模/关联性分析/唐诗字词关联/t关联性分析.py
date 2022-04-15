from efficient_apriori import apriori
with open('t词频1000.txt', 'r', encoding='utf-8') as fp:
    words=eval(fp.readlines()[0])
relations=[]
for line in open("../../唐诗综合考虑/tang.txt", encoding='utf-8'):
    relation=[]
    for word in words:
        if word in line:
            relation.append(word)
    relations.append(tuple(relation))
itemsets,rules=apriori(relations,min_support=0.05,min_confidence=0.5)
#print(itemsets)
print(rules)
