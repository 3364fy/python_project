year=[82,98,65,00,78,97]
year.sort()
print(year)
for index,value in enumerate(year):
    print(index,value)
    if value!=0:
        year[index]=int('19'+str(value))
    else:
        year[index] = int('200' + str(value))
year.sort()
print(year)
print('=============================================================================')
scores=(('广州恒大',72),('北京国安',70),('上海上港',66),('江苏苏宁',53))
for index,item in enumerate(scores):
    print(index+1,'.',end=' ')
    for a in item:
        print(a,end=' ')
    print()
    


