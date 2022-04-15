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

plt.figure(figsize=(10,10))

data=pd.read_csv('accidents.csv')
data.drop_duplicates()
data.drop(['数学建模','Year'],axis=1,inplace=True)
print(data)
print(data.info())

class Gradient:
    def __init__(self,alpha,times):
        '''

        :param alpha: 学习率
        :param times:最大迭代次数
        '''
        self.alpha=alpha
        self.times=times
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
            #Calculate the predicted value
            y_predict=np.dot(X,self.w_[1:])+self.w_[0]
            #Calculate the difference between the true value and the predicted value
            gap=y-y_predict
            #Add the loss value to the loss list
            self.loss_.append(np.sum(gap**2)/2)
            #Adjust weights based on gap
            self.w_[0]+=self.alpha*np.sum(gap)
            self.w_[1:]+=self.alpha*np.dot(X.T,gap)
    def predict(self,X):
        '''
        Predict the sample data based on the sample passed by the parameter
        :param X:类数组类型。形状：[样本数量，特征数量]
                 待测试的样本
        :return:result:数组类型
                预测的结果
        '''
        X=np.asarray(X)
        result=np.dot(X,self.w_[1:])+self.w_[0]
        return result

class StandardScaler:
    '''
    This class normalizes the data
    '''
    def fit(self,X):
        '''
        Calculate the mean and standard deviation of each feature column based on the passed samples
        :param X:类数据类型
                 训练数据，用来计算均值与标准差
        :return:
        '''
        X=np.asarray(X)
        self.std_=np.std(X,axis=0)
        self.mean_=np.mean(X,axis=0)
    def transform(self,X):
        '''
        Standardize the given data, (turn each column of x into standard normally distributed data)
        :param X:类数组类型
                 待转换的数据
        :return:result:类数组类型
                参数x转换成标准正态分布后的结果
        '''
        return (X-self.mean_)/self.std_
    def fit_transform(self,X):
        '''
        Train and transform the data, and return the transformed result
        :param X:类数组类型
                 待转换的数据
        :return:result:类数组类型
                参数x转换成标准正态分布后的结果
        '''
        self.fit(X)
        return self.transform(X)

# gd=Gradient(alpha=0.001,times=20)
# t=data.sample(len(data),random_state=0)
# train_X=t.iloc[:400,:-1]
# train_y=t.iloc[:400,-1]
# test_X=t.iloc[400:,:-1]
# test_y=t.iloc[400:,-1]
# gd.fit(train_X,train_y)
# result=gd.predict(test_X)
# print(result)
# print(np.mean((result-test_y)**2.csv))
# print(gd.w_)
# print(gd.loss_)

'''In order to avoid the difference in the order of magnitude of each feature, which will affect the gradient descent process, 
we now consider normalizing each feature
'''
gd=Gradient(alpha=0.0005,times=20)
t=data.sample(len(data),random_state=0)
train_X=t.iloc[:40,:-1]
train_y=t.iloc[:40,-1]
test_X=t.iloc[40:,:-1]
test_y=t.iloc[40:,-1]

#normalize data
s=StandardScaler()
train_X=s.fit_transform(train_X)
test_X=s.transform(test_X)

s2=StandardScaler()
train_y=s2.fit_transform(train_y)
test_y=s2.transform(test_y)
gd.fit(train_X,train_y)
result=gd.predict(test_X)
print(result)
print(test_y.values)
print(np.mean((result-test_y)**2))
print(gd.w_)
print(gd.loss_)

plt.plot(result,'ro-',label='预测值')
plt.plot(test_y.values,'go--',label='真实值')
plt.xlabel('样本序号')
plt.ylabel('事故数')
plt.title('梯度下降')
plt.legend(loc='best')
plt.show()

# #Plot cumulative error values
# plt.plot(range(1,gd.times+1),gd.loss_,'o-')
# plt.show()
#
# gd=Gradient(alpha=0.0005,times=50)
# t=data.sample(len(data),random_state=0)
# train_X=t.iloc[:400,5:6]
# train_y=t.iloc[:400,-1]
# test_X=t.iloc[400:,5:6]
# test_y=t.iloc[400:,-1]
# #normalize data
# s=StandardScaler()
# train_X=s.fit_transform(train_X)
# test_X=s.transform(test_X)
#
# s2=StandardScaler()
# train_y=s2.fit_transform(train_y)
# test_y=s2.transform(test_y)
# gd.fit(train_X,train_y)
# result=gd.predict(test_X)
# print(result)
# print(np.mean((result-test_y)**2))
# print(gd.w_)
# print(gd.loss_)
#
# plt.scatter(train_X['rm'],train_y)
# x=np.arange(-5,5,0.01)
# plt.plot(x,gd.predict(x.reshape(-1,1)),'r')
# plt.show()
