import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import openpyxl

#Set the font to bold to support Chinese display
mpl.rcParams['font.sans-serif']=['SimHei']
#Set the Chinese font to be able to display symbols normally
mpl.rcParams['axes.unicode_minus']=False

data=pd.read_csv('IT_3.csv')
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

#Set the display length of value, the default is 50
pd.set_option('display.max_colwidth',100)
pd.set_option('display.width',1000)

data.drop_duplicates()
data['Gender']=data['Gender'].map({'F':1,'M':2})
data['Marital_Status']=data['Marital_Status'].map({'Married':1,'Single':2})
data['type']=data['type'].map({'Car':1,'Van':2,'Truck':3,'Utility':4})
data['credit']=data['credit'].map({'Fair':1,'Good':2,'Very Good':3,'Exceptional':4,'Very Poor':5})
print(data)
print(data.info())

class LinearRegression():
    def fit(self,X,y):
        X=np.asmatrix(X.copy())
        y=np.asmatrix(y).reshape(-1,1)
        self.w_=(X.T*X).I*X.T*y
    def predict(self,X):
        X = np.asmatrix(X.copy())
        result=X*self.w_
        return np.array(result).ravel()

#The case where the intercept is not considered
t=data.sample(len(data),random_state=0)
train_X=t.iloc[:4000,:-1]
train_y=t.iloc[:4000,-1]
test_X=t.iloc[4000:,:-1]
test_y=t.iloc[4000:,-1]

dr=LinearRegression()
dr.fit(train_X,train_y)
result=dr.predict(test_X)
print(result)
print(test_y.values)
print(np.mean((result-test_y)**2))
print(dr.w_)

# #Consider the intercept
# t=data.sample(len(data),random_state=0)
# # t['Intercept']=1
# # print(t)
# new_columns=t.columns.insert(0,'Intercept')
# t=t.reindex(columns=new_columns,fill_value=1)
# #print(t)
# train_X=t.iloc[:400,:-1]
# train_y=t.iloc[:400,-1]
# test_X=t.iloc[400:,:-1]
# test_y=t.iloc[400:,-1]
#
# dr=LinearRegression()
# dr.fit(train_X,train_y)
# result=dr.predict(test_X)
# print(result)
# print(test_y.values)
# print(np.mean((result-test_y)**2.csv))
# print(dr.w_)

plt.figure(figsize=(15,10))
plt.plot(result,'ro-',label='预测值')
plt.plot(test_y.values,'go--',label='真实值')
plt.xlabel('样本序号')
plt.ylabel('预测')
plt.title('最小二乘法')
plt.legend(loc='best')
plt.show()
