import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

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
data.drop_duplicates()
data['Species']=data['Species'].map({'Iris-setosa':1,'Iris-versicolor':2,'Iris-virginica':3})
data = data[data['Species']!=3]

class LogisticRegression:
    '''
    Implementing the logistic regression algorithm
    '''
    def __init__(self,alpha,times):
        '''

        :param alpha: 学习率
        :param times:最大迭代次数
        '''
        self.alpha=alpha
        self.times=times
    def sigmoid(self,z):
        '''
        Implementation of sigmoid function
        :param z:float (independent variable)
                 value:z=w.T*x
        :return:the probability value that the sample belongs to category 1, which is used as the prediction of the result
        '''
        return 1.0 / ( 1.00000001 + np.exp(-z) )
    def fit(self,X,y):
        '''
        Train the model on the provided training data
        :param X:类数组类型。形状：[样本数量，特征数量]
                 带训练的样本特征属性。（特征矩阵）
        :param y:类数组类型。形状：[样本数量]
                 目标值 （标签信息）
        :return:
        '''
        X=np.asarray(X)
        y=np.asarray(y)
        #Create a vector of weights with initial values of zero
        self.w_=np.zeros(1+X.shape[1])
        #Create a loss list to hold the loss value after each iteration. 1/2.csv sum (predicted value - true value)^2.csv
        self.loss_=[]
        '''Carry out a loop, iterate multiple times, and continuously adjust the weight value during each iteration, 
        so that the loss value is continuously reduced'''
        for i in range(self.times):
            z=np.dot(X,self.w_[1:])+self.w_[0]
            #Calculate the probability value
            p=self.sigmoid(z)
            cost=-np.sum(y*np.log(p)+(1-y)*np.log(1-p))
            self.loss_.append(cost)
            #Adjust the weight value
            self.w_[0] += self.alpha * np.sum(y-p)
            self.w_[1:] += self.alpha * np.dot(X.T, y-p)
    def predict_proba(self,X):
        '''
        Predict the sample data based on the sample passed by the parameter
        :param X:类数组类型。形状：[样本数量，特征数量]
                 待测试的样本(属性)
        :return:result:数组类型
                预测的结果(概率值)
        '''
        X = np.asarray(X)
        z = np.dot(X, self.w_[1:]) + self.w_[0]
        p = self.sigmoid(z)
        #Convert the prediction results to a 2D array，Easy for subsequent splicing
        p=p.reshape(-1,1)
        #concatenate two arrays
        return np.concatenate([1-p,p],axis=1)
    def predict(self,X):
        '''
        Predict the sample data based on the sample passed by the parameter
        :param X:类数组类型。形状：[样本数量，特征数量]
                 待测试的样本
        :return:result:数组类型
                预测的结果
        '''
        return np.argmax(self.predict_proba(X),axis=1)

t1=data[data['Species']==1]
t2=data[data['Species']==2]
t1=t1.sample(len(t1),random_state=0)
t2=t2.sample(len(t2),random_state=0)
train_X=pd.concat([t1.iloc[:40,:-1],t2.iloc[:40,:-1]],axis=0)
train_y=pd.concat([t1.iloc[:40,-1],t2.iloc[:40,-1]],axis=0)
test_X=pd.concat([t1.iloc[40:,:-1],t2.iloc[40:,:-1]],axis=0)
test_y=pd.concat([t1.iloc[40:,-1],t2.iloc[40:,-1]],axis=0)

lr=LogisticRegression(alpha=0.01,times=50)
lr.fit(train_X,train_y)
lr.predict_proba(test_X)
result=lr.predict(test_X)
print(result)
#calculation accuracy
print(np.sum((result==test_y)/len(test_y)))

plt.figure(figsize=(10,10))
plt.plot(result, 'ro',ms=15, label="预测值") # ms指定圆圈大小
plt.plot(test_y.values, 'go', label="预测值") # pandas读取时serise类型，我们需要转为ndarray
plt.title('逻辑回归预测')
plt.xlabel('样本序号')
plt.ylabel('预测值')
plt.show()

# 绘制目标函数的损失值
plt.plot(range(1,lr.times+1), lr.loss_, 'go-')
plt.xlabel('迭代次数')
plt.ylabel('损失值loss')
plt.show()