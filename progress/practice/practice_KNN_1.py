# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 16:25:00 2017

@author: dell
"""

from numpy import *
import operator
def createData():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=["A","A","B","B"]
    return group,labels
if __name__=="__main__":
    group,labels=createData()
    print(group)
    print(labels)

def classity(test,data,labels,k):
    dataSize=data.shape[0]
    Mat=tile(test,(dataSize,1))-data
    squareMat=Mat**2
    D=squareMat.sum(axis=1)
    sqrtD=D**0.5
    sortedSqrtD=sqrtD.argsort()
    print(sortedSqrtD)
    classCount={}
    for i in range(k):
        votelabels=labels[sortedSqrtD[i]]
        classCount[votelabels]=classCount.get(votelabels,0)+1
        print(classCount)
        sortClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
        print(sortClassCount)
        return sortClassCount[0][0]
if __name__=="__main__":
    data,labels=createData()
    test=[0,0.2]
    test_1=classity(test,data,labels,4)
    print(test_1)
    
#1key函数的运用
students=[('join','A',15),('jane','B',12),('dave','B',10)]
sorted(students,key=lambda x:x[2],reverse=False)
sorted(students,key=lambda x:x[2],reverse=True)
#多个字符的排序
s="asdf234DSdsf23"    
#排序：小写-大写-奇数-偶数
print("".join(sorted(s,key=lambda x:(x.isdigit(),x.isdigit() and int(x) % 2==0,x.isupper(),x))))        
#x.isdigit  把数字放后面，字母放前面
#isdigit() and int(X) % 2==0  把奇数放前面，偶数放后面
#x.isupper 把字母小写的放前面，大写放后面
#x  对所有的字符串进行排序

#特殊需求的排序
list1=[7,-8,5,4,0,-2,-5]
#正数在前，由小到大；负数在后，由大到小
print("".join(sorted(list1,key=lambda x:(x<0,x<0 and -x,x))))
sorted(list1,key=lambda x:(x<0,x<0 and -x,x))
sorted(list1,key=lambda x:(x<0,abs(x)))
