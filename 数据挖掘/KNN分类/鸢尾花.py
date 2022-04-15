import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

#Set the font to bold to support Chinese display
mpl.rcParams['font.sans-serif']=['SimHei']
#Set the Chinese font to be able to display symbols normally
mpl.rcParams['axes.unicode_minus']=False

#show all rows
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
#Set the display length of value, the default is 50
pd.set_option('display.max_colwidth',100)
pd.set_option('display.width',1000)

data=pd.read_csv('Iris.csv')
print(data.head(149))
print(data.tail(10))
print(data.sample(10))
data['Species']=data['Species'].map({'Iris-setosa':1,'Iris-virginica':2,'Iris-versicolor':3})
print(data)
#delete
#data.drop(['id'],axis=1,inplace=True)
#Check duplicates

print(data.duplicated().any())

data.drop_duplicates(inplace=True)
print(data)

print(data['Species'].value_counts())

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
            count=np.bincount(self.y[index])
            result.append(count.argmax())
        return np.asarray(result)

    #Consider weights，Use the inverse of the distance as a weight
    def predict2(self,X):
        X=np.asarray(X)
        result=[]
        for x in X:
            dis=np.sqrt(np.sum((x-self.X)**2,axis=1))
            index=dis.argsort()
            index=index[:self.k]
            count=np.bincount(self.y[index],weights=1/dis[index])
            result.append(count.argmax())
        return np.asarray(result)
# Extract iris data for each category
i1=data[data['Species']==1]
i2=data[data['Species']==2]
i3=data[data['Species']==3]
#Shuffle the data for each category
i1=i1.sample(len(i1),random_state=0)
i2=i2.sample(len(i2),random_state=0)
i3=i3.sample(len(i3),random_state=0)
# Build training and test sets
train_X=pd.concat([i1.iloc[:40,:-1],i2.iloc[:40,:-1],i3.iloc[:40,:-1]])
train_y=pd.concat([i1.iloc[:40,-1],i2.iloc[:40,-1],i3.iloc[:40,-1]])
test_X=pd.concat([i1.iloc[40:,:-1],i2.iloc[40:,:-1],i3.iloc[40:,:-1]])
test_y=pd.concat([i1.iloc[40:,-1],i2.iloc[40:,-1],i3.iloc[40:,-1]])
#Create KNN objects for training and testing
knn=KNN(k=3)
# to train
knn.fit(train_X,train_y)
#Test, get test results
result=knn.predict(test_X)
result2=knn.predict2(test_X)
print(result)
print(result2)
print(test_y)
print(result==test_y)
print(np.sum(result==test_y))
print(len(result))
print(np.sum(result==test_y)/len(result))

#Plot the test set scatterplot
plt.figure(figsize=(10,10))
plt.scatter(x=i1['SepalLengthCm'][:40],y=i1['PetalLengthCm'][:40],color='r',label='Iris-virginica')
plt.scatter(x=i2['SepalLengthCm'][:40],y=i2['PetalLengthCm'][:40],color='g',label='Iris-setosa')
plt.scatter(x=i3['SepalLengthCm'][:40],y=i3['PetalLengthCm'][:40],color='b',label='Iris-versicolor')
#Plot the training set scatterplot
right=test_X[result==test_y]
wrong=test_X[result!=test_y]
plt.scatter(x=right['SepalLengthCm'],y=right['PetalLengthCm'],color='c',marker='x',label='right')
plt.scatter(x=wrong['SepalLengthCm'],y=wrong['PetalLengthCm'],color='m',marker='>',label='wrong')
plt.xlabel('花瓣长度')
plt.ylabel('花萼长度')
plt.title('KNN分类结果')
plt.legend(loc='best')
plt.show()