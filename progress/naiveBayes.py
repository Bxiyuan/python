# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 21:37:20 2018

@author: dell
"""


def loadData():
    postingList=[['my','dog','has','flea','problems','help','please'],
     ['maybe','not','take','him','to','dog','park','stupid'],
     ['my','dalmation','is','so','chte','I','love','him'],
     ['stop','posting','stupid','worthless','garbage'],
     ['mr','licks','ate','my','steak','how','to','stop','him'],
     ['quit','buying','worthless','dog','food','stupid']]
    classVector=[0,1,0,1,0,1]
    return postingList,classVector

def createVocabularyList(data):
    Vocabulary=set([])
    for document in data:
        Vocabulary=Vocabulary|set(document)
        return list(Vocabulary)