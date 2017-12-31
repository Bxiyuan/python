# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 16:18:06 2017

@author: dell
"""

from math import log
def CreateData():
    data=[[0, 0, 0, 0, 'no'],         
         [0, 0, 0, 1, 'no'],  
         [0, 1, 0, 1, 'yes'],  
         [0, 1, 1, 0, 'yes'],  
         [0, 0, 0, 0, 'no'],  
         [1, 0, 0, 0, 'no'],  
         [1, 0, 0, 1, 'no'],  
         [1, 1, 1, 1, 'yes'],  
         [1, 0, 1, 2, 'yes'],  
         [1, 0, 1, 2, 'yes'],  
         [2, 0, 1, 2, 'yes'],  
         [2, 0, 1, 1, 'yes'],  
         [2, 1, 0, 1, 'yes'],  
         [2, 1, 0, 2, 'yes'],  
         [2, 0, 0, 0, 'no']] 
    labels=['年龄', '有工作', '有自己的房子', '信贷情况']
    return data,labels
def calShannonEnt(data):
    num=len(data)
    labelsCount={}
    for feature in data:
        currentlabel=feature[-1]  #取最后一列
        if currentlabel not in labelsCount.keys(): #如果Label没有放入统计次数的字典,添加进去
            labelsCount[currentlabel]=1   
        else:    
            labelsCount[currentlabel]+=1
    shannonEnt=0.0
    for key in labelsCount:
        P=float(labelsCount[key])/num
        shannonEnt-=P*log(P,2)
    return shannonEnt
if __name__=="__main__":
    data,features=CreateData()
    print(data)
    print(calShannonEnt(data))
               
def splitData(data,axis,value):
    returnData=[]
    for feature in data:
        if feature[axis]==value:
            reduceFeature=feature[:axis]
            reduceFeature.extend(feature[axis+1:])
            returnData.append(reduceFeature)
    return returnData

def chooseBestFeatureToSplit(data):
    numFeatures=len(data[0])-1
    baseEntropy=calShannonEnt(data)
    bestInformationGain=0.0
    bestFeature=-1
    for i in range(numFeatures):
        featureList=[example[i] for example in data] #选取某一列
        uniqueValue=set(featureList)
        newEntropy=0.0
        for value in uniqueValue:
            subData=splitData(data,i,value)
            P=len(subData)/float(len(data))
            newEntropy += P*calShannonEnt(subData)
        informationGain=baseEntropy-newEntropy
        print("第%d个特征的增益为%.3f" % (i,informationGain))
        if (informationGain>bestInformationGain):
            bestInformationGain=informationGain
            bestFeature=i
    return bestFeature
if __name__=="__main__":
    data,features=CreateData()
    print("最优特征索引值:"+str(chooseBestFeatureToSplit(data)))

import operator     
def majorityCount(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def CreateTree(data,labels,featurelabels):
    classList=[example[-1] for example in data]
    if classList.count(classList[0])==len(classList):
        return classList[0]
    if len(data[0])==1:
        return majorityCount(classList)
    bestFeature=chooseBestFeatureToSplit(data)
    bestFeatureLabel=labels[bestFeature]
    featurelabels.append(bestFeatureLabel)
    myTree = {bestFeatureLabel:{}}
    del (labels[bestFeature])
    featureValues=[example[bestFeature] for example in data]
    uniqueValue=set(featureValues)
    for value in uniqueValue:
        myTree[bestFeatureLabel][value]=CreateTree(splitData(data,bestFeature,value),labels,featurelabels)
    return myTree
if __name__== "__main__":
    data,labels=CreateData()
    featureLabels=[]
    myTree=CreateTree(data,labels,featureLabels)
    print(myTree)

def classify(myTree,featureLabels,testValue):
    firstStr=next(iter(myTree))
    secondDict=myTree[firstStr]
    featureIndex=featureLabels.index(firstStr)
    for key in secondDict.keys():
        if testValue[featureIndex]==key:
            if type(secondDict[key]).__name__=="dict":
                classLabel=classify(secondDict[key],featureLabels,testValue)
            else:
                classLabel=secondDict[key]
    return classLabel
if __name__=="__main__":
    data,labels=CreateData()
    featureLabels=[]
    myTree=CreateTree(data,labels,featureLabels)
    testValue=[0,1]
    result=classify(myTree,featureLabels,testValue)
    if result == "yes":
        print("paying")
    if result == "no":
        print("dafult")
