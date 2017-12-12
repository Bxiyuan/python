# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
os.getcwd()
x=1
x = x + 1
x
x +=1
x
x=[1]
x = x + [1]
x
x += [1]
x
#对不可变对象进行添加元素的操作，
#会让变量指向对象地址发生改变，
#而可变对象地址则不会改变。 

#内置对象中，中可变对象 list, dict. 不可变对象 str, int, tuple, float
a=1.0
b=1
a is b
a == b
id(a)
id(b)
isinstance (a,float)
isinstance(b,int) #判断实例是否是这个类
#is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
type(a) == type(b)
type(a) is type(b)
list1=[1,0]
list2=[2,3]

matrix=[]
for i in range(2):
    tmp=input().split(' ')
    tmp=[int(x) for x in tmp]
    matrix.append(tmp)

print(matrix)

for i in range(2):
    for j in range(2):
        print(matrix[i][j],end=" ")
    print()
    
print('%d %d\n%d %d' % (matrix[0][0],matrix[0][1],matrix[1][0],matrix[1][1]))

import os
ls = os.linesep
while True:
    
if os.path.exists(fname):
    print "ERROR: '%s' already exists" % fname
else:
    break

all=[]
print "nEnter lines ('.' by itself to quit) . \n"

while True:
    entry = raw_input('> ')
    if entry =='.':
    break
else:
    all.append(entry)
    
fobj = open (fname, 'w')
fobj.writelines(['%s%s' $ (x,ls) for x in all])
fobj.close()
print'DONE!'

fname = raw_input('Enter filename: ')
print

try:
    fobj = open (fname, 'r')
except IOError, e:
    print"*** file open error:",e
else:
    for eachLine in fobj:
        print eachLine,
        fobj.close()



































       