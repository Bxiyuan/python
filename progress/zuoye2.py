# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:38:05 2017

@author: dell
"""
import os
os.getcwd()
Q1：已知有序列week=['Monday','Tuseday','Wednesday','Thursday','Friday','Saturday','Sunday'],
请写出两种切片命令，使得它可以得到序列['Monday','Tuseday','Wednesday','Thursday','Friday']。

week=['Monday','Tuseday','Wednesday','Thursday','Friday','Saturday','Sunday']
print(week[0:5])
print(week[-7:-2])

Q2：若想要生成如下的列表x（1-100之间）：[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
请写出相应的列表解析表达式

xlist=[(x+1)*5 for x in range(20)]
print(xlist)

Q3：熟悉并自行构造例子测试序列类型函数和方法的使用：
（1）序列：enumerate(),reversed(),sorted(),zip()
（2）字符串:join(),split(),replace(),upper()
（3）列表：append(),count(),extend(),insert()
注：元组没有自己专用的操作符和内建函数。

#enumerate
seasons=["spring","summer","fall","winter"]
list(enumerate(seasons))
list(enumerate(seasons,start=1))
seq=["one","two","three"]
for i,element in enumerate(seq):
    print(i+1,seq[i])

#reversed
string="python"
print(list(reversed(string)))
tup=('p','y','t','h','o','n')
print(list(reversed(tup)))
range1=range(5,9)
print(list(reversed(range1)))
list1=[1,2,3,4,5]
print(list(reversed(list1)))

#sorted
m=[2,1,4,6,7,3,5]
print(sorted(m))
k=[('b',2),('a',1),('c',3),('d',4)]
sorted(k, key=lambda x:x[1])
students=[('tom','A',14),('jane','C',16),('dave','B',13)]
sorted(students,key=lambda x:x[2])
sorted(students,key=lambda x:x[2],reverse=True)

#zip
a1=[1,2,3]
b1=[4,5,6]
c1=[4,5,6,7,8]
zipped=list(zip(a1,b1))
list(zip(a1,c1))
list(zip(*zipped))

#join
s1="-"
s2=""
seq=("p","y","t","h","o","n")
print(s1.join(seq))
print(s2.join(seq))

#split
str="today is breakfast is egg"
print(str.split())
print(str.split("is",1))
print(str.split("is"))

#replace
str ="python"
print("学习:",str)
print("学习:",str.replace("python","homework"))
str="this is string example!"
print(str.replace("is","was",1))
str="this is string example!"
print(str.replace("is","was",2))

#upper
breakfast="coffee"
print("breakfast.upper:",breakfast.upper())

#append()
list1=[1,2,3]
list1.append(4)
print("更新后的列表：",list1)

#count()
list2=["a","a","s","d","a",1,2,3,1,2,2]
print("a元素的个数：",list2.count("a"))
print("2元素的个数：",list2.count(2))

#extend()
list1=["taobao","tianmao"]
list2=list(range(5))
list1.extend(list2)
print("扩展后的列表：",list1)

#insert()
list1=["taobao","tianmao","sougou"]
list1.insert(2,"baidu")
print("列表插入元素后：",list1)