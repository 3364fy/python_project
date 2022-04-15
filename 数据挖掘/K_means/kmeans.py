import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from 数据挖掘.geshi import format
#format()

#Set the font to bold to support Chinese display
mpl.rcParams['font.sans-serif']=['SimHei']
#Set the Chinese font to be able to display symbols normally
mpl.rcParams['axes.unicode_minus']=False

#Set the display length of value, the default is 50
pd.set_option('display.max_colwidth',1000)
pd.set_option('display.width',10000)
#show all rows
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

data=pd.read_csv('order.csv')
t=data.iloc[:,-8:]


class KMeans:
    '''Kmeans聚类算法实现'''

    def __init__(self, k, times):
        '''初始化

        Parameters
        -----
        k: int 聚成几个类
        times: int 迭代次数
        '''
        self.k = k
        self.times = times

    def fit(self, X):
        '''根据所给数据训练

        Pararmeters
        ------
        X: 类数组类型，形如：[样本数量，特征数量]
        '''
        X = np.asarray(X)
        # 设置随机数种子，以便于可以相同的随机系列，以便随机结果重现
        np.random.seed(0)
        # 从数组中随机选择K个点作为初始聚类中心
        self.cluster_centers_ = X[np.random.randint(0, len(X), self.k)]
        # 用于存放数据所属标签
        self.labels_ = np.zeros(len(X))
        # 开始迭代
        for t in range(self.times):
            # 循环遍历样本计算每个样本与聚类中心的距离
            for index, x in enumerate(X):
                # 计算每个样本与每个聚类中心的欧式距离
                dis = np.sqrt(np.sum((x - self.cluster_centers_) ** 2, axis=1))
                # 将最小距离的索引赋值给标签数组，索引的值就是当前所属的簇。范围威威（0，K-1）
                self.labels_[index] = dis.argmin()
            # 循环便利每一个数更新聚类中心
            for i in range(self.k):
                # 计算每个簇内所有点的均值，用来更新聚类中心
                self.cluster_centers_[i] = np.mean(X[self.labels_ == i], axis=0)

    def predict(self, X):
        '''预测样本属于哪个簇

        Parameters
        -----
        x: 类数组类型。形如[样本数量。特征数量]

        Reeturn
        -----
        result: 类数组，每一个x所属的簇
        '''
        X = np.asarray(X)
        result = np.zeros(len(X))
        for index, x in enumerate(X):
            # 计算样本与聚类中心的距离
            dis = np.sqrt(np.sum((x - self.cluster_centers_) ** 2, axis=1))
            # 找到距离最近的聚类中中心划分一个类别
            result[index] = dis.argmin()
        return result
kmeans=KMeans(3,50)
kmeans.fit(t)
# print(kmeans.cluster_centers_)
# print(t[kmeans.labels_==0])

t2=data.loc[:,"Food%":"Fresh%"]
kmeans=KMeans(3,50)
kmeans.fit(t2)
plt.figure(figsize=(10,10))
# 绘制每个类别散点图
plt.scatter(t2[kmeans.labels_==0].iloc[:,0], t2[kmeans.labels_==0].iloc[:,1], label="类别1")
plt.scatter(t2[kmeans.labels_==1].iloc[:,0], t2[kmeans.labels_==1].iloc[:,1], label="类别1")
plt.scatter(t2[kmeans.labels_==2].iloc[:,0], t2[kmeans.labels_==2].iloc[:,1], label="类别1")
# 绘制聚类中心
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1], marker="+",s=300)
plt.title("食物与肉类购买聚类分析")
plt.xlabel("食物")
plt.ylabel("肉类")
plt.legend()
plt.show()


