import matplotlib.pyplot as plt
#正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
date=[1,2,3,4,5,6,7]
hebei=[45,78,2,54,656,21,44]
shanxi=[458,41,25,85,52,23,48]
#折线图
plt.plot(date,hebei,label='河北')
plt.plot(date,shanxi,label='山西')
plt.xlabel('日期')
plt.ylabel('车次')
plt.title('每日入库对比')
plt.legend()
plt.show()

#柱状图
plt.bar(date,hebei,label='河北')
plt.bar(date,shanxi,label='山西')
plt.xlabel('日期')
plt.ylabel('车次')
plt.title('每日入库对比')
plt.legend()
plt.show()

#水平柱状图
plt.barh(date,hebei,label='河北')
plt.barh(date,shanxi,label='山西')
plt.xlabel('日期')
plt.ylabel('车次')
plt.title('每日入库对比')
plt.legend()
plt.show()

#饼图
number=[654,463]
province=['河北','山西']
colors=['#999fff','#fff999']
plt.pie(x=number,labels=province,colors=colors)
plt.show()
