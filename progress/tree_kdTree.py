# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:41:15 2017

@author: dell
"""

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
        if currentlabel not in laelcounts.keys():labelcounts[currentlabel]=0
        labelcounts[currentlabel]+=1
    shannonent=0.0
    for key in labelcounts:
        prob=float(labelcounts[key])/numentries
        shannonent-=prob*log(prob,2)
        return shannonent
     
def calconditionalentropy(dataset,i,featlist,uniquevals):     
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
        subdataset=splitdataset(dataset,l,value)
        prob=len(subdataset)/float(len(dataset))
        ce+=prob*calcshannonent(subdataset)
    return ce
