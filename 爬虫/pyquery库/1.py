from pyquery import PyQuery as pq
#字符串
doc=pq('html')
print(doc('li'))
print(doc('#container.list li'))
for item in doc('#container.list li').items():
    print(item.text())

#url
doc=pq(url='')
print(doc('title'))

#查找子孙节点
doc=pq('html')
items=doc('.list')
lis=items.find('li')
print(lis)

#查找子节点
lis=items.children()
print(lis)

#筛选符合条件的节点
lis=items.children('.active')
print(lis)

#查找父节点
doc=pq('html')
items=doc('.list')
container=items.parent()
print(container)

#查找祖先节点
doc=pq('html')
items=doc('.list')
parents=items.parents()
print(parents)

#查找兄弟节点
doc=pq('html')
li=doc('.list .item-0.active')
print(li.siblings())
print(li.attr('href'))#获取属性
print(li.attr.href)
print(li.text())#获取文本
print(li.html())#获取html文本

