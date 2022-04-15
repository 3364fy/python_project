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
data['Species']=data['Species'].map({'Iris-versicolor':0,'Iris-virginica':1,'Iris-setosa':-1,})
data = data[data['Species']!=0]
class Perception:
    def __init__(self,alpha,times):
        '''

        :param alpha: 学习率
        :param times:最大迭代次数
        '''
        self.alpha=alpha
        self.times=times
    def step(self,z):
        '''

        :param z: 数组类型(或者是标量) 阶跃函数参数。将z映射为1或者-1
        :return: value: int z>0返回1.z<0返回1
        '''
        return np.where(z > 0, 1, -1)  # 一步实现对数值或者数组的计算返回
    def fit(self,X,y):
        '''

        :param X: 特征矩阵，可以是List也可以是Ndarray，形状为： [样本数量,特征数量]
        :param y: 标签数组
        :return:
        '''
        X=np.asarray(X)
        y=np.asarray(y)
        self.w_=np.zeros(1+X.shape[1])
        self.loss_=[]
        for i in range(self.times):
            loss=0
            for x,target in zip(X,y):
                y_hat=self.step(np.dot(x,self.w_[1:])+self.w_[0])
                loss+=y_hat!=target
                self.w_[0]+=self.alpha*(target-y_hat)
                self.w_[1:] += self.alpha * (target - y_hat)*x
                self.loss_.append(loss)
    def predict(self,X):
        '''

        :param X: 特征矩阵，可以是List也可以是Ndarray，形状为： [样本数量,特征数量]
        :return: 数组类型， 分类值[1或-1]
        '''
        return self.step(np.dot(X,self.w_[1:])+self.w_[0])

t1 = data[data["Species"]==1]
t2 = data[data["Species"]==-1]
t1.sample(len(t1), random_state=0)
t2.sample(len(t2), random_state=0)
train_X = pd.concat([t1.iloc[:40,:-1], t2.iloc[:40, :-1]], axis=0)
train_y = pd.concat([t1.iloc[:40,-1], t2.iloc[:40, -1]], axis=0)
test_X = pd.concat([t1.iloc[40:,:-1], t2.iloc[40:, :-1]], axis=0)
test_y = pd.concat([t1.iloc[40:,-1], t2.iloc[40:, -1]], axis=0)

p = Perception(0.1, 10)
p.fit(train_X,train_y)
result = p.predict(test_X)
print(result)
print(test_y.values)
print(p.w_)
print(p.loss_)

plt.plot(test_y.values, "go", ms=15, label="真实值")
plt.plot(result, "rx", ms=15, label="预测值")
plt.title("感知器二分类")
plt.xlabel("样本序号")
plt.xlabel("类别")
plt.show()

plt.plot(range(1, p.times+791), p.loss_, "o-")
plt.show()
