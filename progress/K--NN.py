# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 15:52:47 2017

@author: dell
"""

import numpy as np
#Numpy是Python的一个科学计算的库，提供了矩阵运算的功能
def Data():
    data=np.array([[1,101],[5,89],[108,5],[115,8]])
    labels=["爱情片","爱情片","动作片","动作片"]
    return data,labels
if __name__=="__main__":
    data,labels=Data()
    print(data)
    print(labels)
import operator    
def KNN(test,data,labels,k):
    dataSize=data.shape[0] #测试数据的行数 
    Mat=np.tile(test,(dataSize,1))-data #把test沿Y轴复制dataSize次，沿X轴复制1次
    squareMat=Mat**2
    Distance=squareMat.sum(axis=1)#sum=0，普通相加，sum(axis=0)每一列相加，sum(axis=1)，每一行相加
    sqrtDistance=Distance**0.5 #欧氏距离
    sortDistance=sqrtDistance.argsort() #元素从小到大排序后的索引值
    classCount={}
    for i in range(k):
        voteLabel=labels[sortDistance[i]]
        classCount[voteLabel]=classCount.get(voteLabel,0)+1
        sortClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
        #key=operator.itemgetter(1)根据字典的值进行排序
        return sortClassCount[0][0]
if __name__=="__main__":
    data,labels=Data()
    test=[101,20]
    test_01=KNN(test,data,labels,4)
    print(test_01)
    
c={}
l=["a","b","a","b","b"] 
for i in range(5):
    v=l[i]
    c[v]=c.get(v,0)+1
c    
c["c"]=c.get("c",0)+1
