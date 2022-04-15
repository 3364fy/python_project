import random
price=random.randint(1,2)
print('今日竞猜的价格在1到10之间',price)
a=0
try:
    while a<9:
        guess = float(input('输入竞猜价格：\n'))
        if guess==price:
            print('竞猜正确')
            break
        else:
            a+=1
            print('竞猜错误')
except:
    print('不能这样输入哟')