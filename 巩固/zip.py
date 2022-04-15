a=['白羊座','金牛座','双子座']
b=['积极乐观','固执内向','圆滑世故']
c=dict(zip(a,b))
print(c)#迭代器
'''for i in c:
    print(i)'''
for item in c:
    print(item,c[item])
key=input('请输入星座')
print(key,c.get(key,'hhhhh'))