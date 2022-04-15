import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
#一维
a=pd.Series(['a','s','d','s','i'])
print(a)
#二维
b=pd.DataFrame({
    '客户名称':['张三','李四','王五','赵六'],
    '车':[1,4,8,6],
    '吨数':[564,84,12,84],
    '总价':[465,845,462,8646]
})
print(b)
#读取Excel
e_file=pd.ExcelFile('E:/office/Excel/58.xls')
data=e_file.parse('58.xls')
print(data)
pt1=pd.pivot_table(data,index='介绍',columns='序号',values='价格',aggfunc=np.sum,margins=True)
pd.set_option('display.max_columns',None)
print(pt1)
print(pt1.iat[1,0])

#pt1.plot()
pt1.plot(kind='bar')
plt.xticks(rotation=90)
plt.show()