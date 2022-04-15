import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

#Set the font to bold to support Chinese display
mpl.rcParams['font.sans-serif']=['SimHei']
#Set the Chinese font to be able to display symbols normally
mpl.rcParams['axes.unicode_minus']=False

data=pd.read_csv('accidents.csv')
#show all rows
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
#Set the display length of value, the default is 50
pd.set_option('display.max_colwidth',100)
pd.set_option('display.width',1000)
#delete duplicate records
data.drop_duplicates(inplace=True)
data.drop(['数学建模','Year'],axis=1,inplace=True)
print(data)

class KNN:
    def __init__(self,k):
        self.k=k
    def fit(self,X,y):
        self.X=np.asarray(X)
        self.y=np.asarray(y)
    def predict(self,X):
        X=np.asarray(X)
        result=[]
        for x in X:
            dis=np.sqrt(np.sum((x-self.X)**2,axis=1))
            index=dis.argsort()
            index=index[:self.k]
            count=np.mean(self.y[index])
            result.append(count)
        return np.asarray(result)

    #Consider weights，Use the inverse of the distance as a weight
    def predict2(self,X):
        X=np.asarray(X)
        result=[]
        for x in X:
            dis=np.sqrt(np.sum((x-self.X)**2,axis=1))
            index=dis.argsort()
            index=index[:self.k]
            s=np.sum(1/(dis[index]+0.0000000000001))
            weight=(1/(dis[index]+0.0000000000001))/s
            result.append(np.sum(self.y[index]*weight))
        return np.asarray(result)

t=data.sample(len(data),random_state=0)
train_X=t.iloc[:40,:-1]
train_y=t.iloc[:40,-1]
test_X=t.iloc[40:,:-1]
test_y=t.iloc[40:,-1]

#Create KNN objects for training and testing
knn=KNN(k=3)
# to train
knn.fit(train_X,train_y)
#Test, get test results
result=knn.predict(test_X)
result2=knn.predict2(test_X)
print(result)
print(np.mean((result-test_y)**2))
print(test_y.values)

print(result2)
print(np.mean((result2-test_y)**2))
print(test_y.values)

plt.figure(figsize=(10,10))
#Plot predicted values
plt.plot(result,'ro-',label='预测值')
#plot the true value
plt.plot(test_y.values,'go--',label='真实值')
plt.title('KNN回归')
plt.xlabel('序号')
plt.ylabel('事故数')
plt.legend(loc='best')
plt.show()
