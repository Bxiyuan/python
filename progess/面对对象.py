# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:08:32 2017

@author: dell
"""

import sys
print ("命令参数如下：")
for i in sys.argv:
    print(i)
print("\n\nPython 路径为：",sys.path,"\n")

# Filename: support.py

def print_func( par ):
    print ("Hello : ", par)
    return
# Filename: test.py
 
# 导入模块
import support
 
# 现在可以调用模块里包含的函数了
support.print_func("Runoob")

import fibo
fibo.fib(1000)
fibo.fib2(100)
fibo.__name__

from fibo import fib,fib2
from fibo import *
fib(100)
#这个声明不会把整个fibo模块导入到当前的命名空间中，它只会将fibo里的fib函数引入进来。
import fibo,sys
dir(fibo)
dir(sys)

# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。
s="hello"
str(s)
repr(s)
str(1/7)
x=10*3.25
y=200**2
s="x="+repr(x)+",y="+repr(y)
S="x="+str(x)+",y="+str(y)
hello="hello python\n"
hellos=repr(hello)
print(hellos)
h=str(hello)
repr((x,y,"python"))

for x in range(1,101):
    print(repr(x).rjust(3),repr(x*x).rjust(5),end=" ")
    print(repr(x*x*x).rjust(7))
# rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
for x in range(1,11):
    print("{0:2d} {1:3d} {2:4d}".format(x,x*x,x*x*x))
# zfill(), 它会在数字的左边填充 0
"12".zfill(4)
"12334134".zfill(6)
"-1.1".zfill(5)
print('{}:"{}"'.format("python","homework"))
print('{1}:"{0}"'.format("python","homework"))
print('{0}:"{1}"'.format("python","homework"))
import math
print("PI:{}".format(math.pi))
print("PI:{!r}".format(math.pi))
print("PI:{0:.3f}".format(math.pi))
print("PI:%5.3f" % math.pi)
table={"taobao":1,"jingdong":2,"tianmao":3}
for name,number in table.items():
    print("{0:10}--{1:5d}".format(name,number))
print()    
str=input("请输入：")
print("你输入的是：",str)

import pickle
data={"a":[1,2],"b":("python",u'a'),"c":None}
list1=[1,2,3]
list1.append(list1)

  输入和输出

try:
    KeyboardInterrupt
finally:
    print("goodbye,world!")

def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is",result)
    finally:
        print("executing finally clause")
divide(2,1)
divide(2,0)
divide("2",2)
for line in open("python.txt"):
    print(line,end=" ")
# with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法
with open("python.txt") as f:
    for line in f:
        print(line, end=" ")

class myclass:
    i=12345
    def f(self):
        return "hello world!"
x=myclass()
print(x.i)
print(x.f())

def __init__(self):
    self.data=[]
MyClass

class Complex:
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart
x=Complex(3,-2)
print(x.i,x.r)

class test:
    def prt(self):
        print(self)
        print(self.__class__)
t=test()
t.prt()
#类定义
class people:
    name=""
    age=0
    __weight=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print("%s 说：\"我 %d 岁了,现在 %d kg。\"" %(self.name,self.age,self.__weight))
p=people("tom",10,50)
p.speak()
#单继承示例        
class student(people):
    grade=0 #grade=""
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w) #调用父类的构函
        self.grade=g
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" %(self.name,self.age,self.grade))
s=student("tom",10,30,3)
s.speak()
#多继承
#另一个类，多重继承之前的准备
class speaker():
    topic=""
    name=""
    def __init__(self,n,t):
        self.name=n
        self.topic=t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
#多重继承
class sample(speaker,student):
     a=""
     def __init__(self,n,a,w,g,t):
         student.__init__(self,n,a,w,g)
         speaker.__init__(self,n,t)

#class sample(student,speaker):
#     a=""
#     def __init__(self,n,a,w,g,t):
#         student.__init__(self,n,a,w,g)
#         speaker.__init__(self,n,t)
     
test=sample("Tom",25,80,4,"Python")       
test.speak() #方法名同，默认调用的是在括号中排前地父类的方法
#方法重写
class parent:
    def mymethod(self):
        print('调用父类方法')
class child(parent):
    def mymethod(self):
        print('调用子类方法')
c=child()
c.mymethod() # 子类调用重写方法
p=parent()
p.mymethod()

class justcounter:
    __secretCount=0
    publicCount=0
    def count(self):
        self.__secretCount+=1
        self.publicCount+=1
        print(self.__secretCount)
counter=justcounter()
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__secretCount)  # 报错，实例不能访问私有变量

class site:
    def __init__(self,name,url):
        self.name=name
        self.__url=url
    def who(self):
        print("name:",self.name)
        print("url:",self.__url)
    def __foo(self):
        print('这是私有方法')
    def foo(self):
        print('这是公共方法')
        self.__foo()
s=site("python","www.python.com")
s.who()
s.foo()
s.__foo()

class vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return "vector(%d,%d)"%(self.a,self.b)
    def __add__(self,other):
        return vector(self.a+other.a,self.b+other.b)
v1=vector(2,10)
v2=vector(5,-2)
print(v1+v2)    

    __init__ : 构造函数，在生成对象时调用
    __del__ : 析构函数，释放对象时使用
    __repr__ : 打印，转换
    __setitem__ : 按照索引赋值
    __getitem__: 按照索引获取值
    __len__: 获得长度
    __cmp__: 比较运算
    __call__: 函数调用
    __add__: 加运算
    __sub__: 减运算
    __mul__: 乘运算
    __div__: 除运算
    __mod__: 求余运算
    __pow__: 乘方



























































