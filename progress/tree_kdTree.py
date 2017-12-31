# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:41:15 2017

@author: dell
"""
from math import log
def majoritycnt(classlist):
    """
返回出现次数最多的分类名称
    :param classList: 类列表
    :return: 出现次数最多的类名称
    """
    
    classcount={}
    for vote in classlist:
        if vote not in classcount.keys():classcount[vote]=0
        classcount[vote]+=1
    sortedclasscount=sorted(classcount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedclasscount[0][0]    

def createtree(dataset, labels, choosebestfeaturetosplitfunc=choosebestfeaturetosplitbyID3):
    """
    创建决策树
    :param dataSet:数据集
    :param labels:数据集每一维的名称
    :return:决策树
    """
    
    classlist=[example[-1] for example in dataset]
    if classlist.count(classlist[0])==len(classlist):
        return classlist[0]
    if len(dataset[0])==1:
        return majoritycnt(classlist)
    bestfeat=choosebestfeaturetosplitfunc(dataset)
    bestfeatlabel=labels[bestfeat]
    mytree={bestfeatlabel:{}}
    del (labels[bestfeat])
    featvalues=[example[bestfeat] for example in dataset]
    uniquevals=set(featvalues)
    for value in uniquevals:
        sublabels=labels[:]
        mytree[bestfeatlabel][value]=createtree(splitdataset(dataset,bestfeat,value),sublabels)
    return mytree    
    
def createdataset():
    """
创建数据集
    
    ：return:
    """
    dataset=[[u"young",u"F",u"F",u"general",u"F"],
             [u'young',u'F',u'F',u'good',u'F'],
             [u'young',u'T',u'F',u'good',u'T'],
             [u'young',u'T',u'T',u'general',u'T'],
             [u'young',u'F',u'F',u'general',u'F'],
             [u'middle',u'F',u'F',u'general',u'F'],
             [u'middle',u'F',u'F',u'good',u'F'],
             [u'middle',u'T',u'T',u'good',u'T'],
             [u'middle',u'F',u'T',u'outstanding',u'T'],
             [u'middle',u'F',u'T',u'outstanding',u'T'],
             [u'old',u'F',u'T',u'outstanding',u'T'],
             [u'old',u'F',u'T',u'good',u'T'],
             [u'old',u'T',u'F',u'good',u'T'],
             [u'old',u'T',u'F',u'outstanding',u'T'],
             [u'old',u'F',u'F',u'general',u'F'],
             ]
    labels=[u"年龄",u"有工作",u"有房子",u"信贷情况"]
    return dataset,labels
print(createdataset())

def splitdataset(dataset,axis,value):
    """
按照给定特征划分数据集
    :param dataSet: 待划分的数据集
    :param axis: 划分数据
    :retdataset.appe集的特征的维度
    :param value: 特征的值
    :return: 符合该特征的所有实例（并且自动移除掉这维特征）
    """
    
    retdataset=[]
    for featvec in dataset:
        if featvec[axis]==value:
            reducedfeatvec=featvec[:axis]
            reducedfeatvec.extend(featvec[axis+1:])
            retdataset.append(reducedfeatvec)
    return retdataset
print(splitdataset())

def calcshannonent(dataset):   
    """
计算训练数据集中的Y随机变量的香农熵
    :param dataSet:
    :return:
    """
    
    numentries=len(dataset)
    labelcounts={}
    for featvec in dataset:
        currentlabel=featvec[-1]
        if currentlabel not in labelcounts.keys():labelcounts[currentlabel]=0
        labelcounts[currentlabel]+=1
    shannonent=0.0
    for key in labelcounts:
        prob=float(labelcounts[key])/numentries
        shannonent-=prob * log(prob,2)
        return shannonent
     
def calcconditionalentropy(dataset,i,featlist,uniquevals):     
    '''
    计算X_i给定的条件下，Y的条件熵
    :param dataSet:数据集
    :param i:维度i
    :param featList: 数据集特征列表
    :param uniqueVals: 数据集特征集合
    :return:条件熵
    ''' 

    ce=0.0
    for value in uniquevals:
        subdataset=splitdataset(dataset,i,value)
        prob=len(subdataset)/float(len(dataset))
        ce+=prob*calcshannonent(subdataset)
    return ce

def calcinformationgain(dataset,baseentropy,i):
    """
    计算信息增益
    :param dataSet:数据集
    :param baseEntropy:数据集中Y的信息熵
    :param i: 特征维度i
    :return: 特征i对数据集的信息增益g(dataSet|X_i)
    """
    
    featlist=[example[i] for example in dataset]
    uniquevals=set(featlist)
    newentropy=calcconditionalentropy(dataset,i,featlist,uniquevals)
    infogain=baseentropy-newentropy
    return infogain
    
def calcinformationgainrate(dataset,baseentropy,i):
    """
    计算信息增益比
    :param dataSet:数据集
    :param baseEntropy:数据集中Y的信息熵
    :param i: 特征维度i
    :return: 特征i对数据集的信息增益g(dataSet|X_i)
    """
    
    return calcinformationgain(dataset,baseentropy,i)/baseentropy
#ID3特征选择算法的Python实现
def choosebestfeaturetosplitbyID3(dataset):
    """
    选择最好的数据集划分方式
    :param dataSet:
    :return:
    """
    
    numfeatures=len(dataset[0])-1
    baseentropy=calcshannonent(dataset)
    bestinfogain=0.0
    bestfeature=-1
    for i in range(numfeatures):
        infogain=calcinformationgain(dataset,baseentropy,i)
        if (infogain>bestinfogain):
            bestinfogain=infogain
            bestfeature=i
    return bestfeature

dataset,lables=createdataset()
mytree=createtree(dataset,lables)  
   
        
import matplotlib.pyplot as plt
 
# 定义文本框和箭头格式
decisionNode = dict(boxstyle="round4", color='#3366FF')  #定义判断结点形态
leafNode = dict(boxstyle="circle", color='#FF6633')  #定义叶结点形态
arrow_args = dict(arrowstyle="<-", color='g')  #定义箭头
 
#绘制带箭头的注释
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
                            xytext=centerPt, textcoords='axes fraction',
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)
 
 
#计算叶结点数
def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs
 
 
#计算树的层数
def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth
 
 
#在父子结点间填充文本信息
def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)
 
 
def plotTree(myTree, parentPt, nodeTxt):
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = myTree.keys()[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)  #在父子结点间填充文本信息
    plotNode(firstStr, cntrPt, parentPt, decisionNode)  #绘制带箭头的注释
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD
 
 
def createPlot(inTree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5 / plotTree.totalW;
    plotTree.yOff = 1.0;
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()    
    
    
    
    
    
    
    
    