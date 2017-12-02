# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:46:12 2017

@author: dell
"""

#abs
print("abs(-40):",abs(-40))
print(abs(100.23))
a=abs(-34)
print(a)

#dict
dict()
dict(a='a',b='b',c='c')
dict(zip(['one','two','three'],[1,2,3]))
list(zip(['one','two','three'],[1,2,3]))
dict([('one',1),('two',2),('three',3)])

#help
help("sys")
help("str")
a=[1,2,3]
help(a)
help(a.append)

#min
print(min(1.2,3,0,-4))
print(min(1,0,1222))

#setattr
class A(object):
    bar=1
a=A()
getattr(a,"bar")#获取属性
setattr(a,"bar",5)#设置属性
a.bar

#all
all(['a','b'])
all(['','a'])
all([0,1,2])
all([])
all(())#空元组
a=(1,2,3,4)
def all(a):
    for element in a:
        if not element:
            return False
    return True

#dir 获得参数信息
dir({})
dir()
dir([])
dir(())

#hex  10进制转换为16进制
hex(10)
hex(16)

#next
it=iter([1,2,3,4,5])
while True:
    try:
        x=next(it)
        print(x+1)
    except StopIteration:
        break

#slice  切片
myslice=slice(5)
myslice
arr =list(range(10))
arr[myslice]      
arr[slice(1,10,3)]    
 
#any
a=(1,2,3,4,5)
def any(a):
    for element in a:
        if element:
            return True
    return False
any(())
any([])   
any({})    
any([0,"",False])    
any(["a",1,2,0])    

#divmod 把除数和余数运算结果结合起来
divmod(7,2)   
divmod(100,5)  

#id
a="python"
id(a)
b=100
id(b)    

#sorted
a=(2,3,6,1,7,8,7,4)
sorted(a)
l=[('a',2),('b',1),('d',3),('c',4)]
sorted(l,key=lambda x:x[1])    
sorted(l,key=lambda x:x[0],reverse=True)    
sorted(l,key=lambda x:x[0])    

#ascii 返回一个表示对象的字符串
ascii(1)    
ascii(a)   
ascii('python')   

#enumerate
elements=('a','b','c')    
list(enumerate(elements,start=1))    
seq=['one','two','three']    
for i, element in enumerate(seq):
    print(i+1,seq[i])

#input
a=input("input:")
type(a)    

#oct 将一个整数转换成8进制字符串
oct(10)
oct(10000)
divmod(10000,8)
divmod(1250,8)
divmod(156,8)
divmod(19,8)

#staticmethod 返回函数的静态方法
class c(object):
    @staticmethod
    def f():
        print("python");
c.f();
cobj=c()
cobj.f()

#bin  二进制表示
bin(10)
bin(3)

#eval 执行一个字符串表达式，并返回表达式的值
x=7
eval('3*x')
eval("pow(2,2)")
eval("2+3")
pow(3,4) #pow() 方法返回 xy（x的y次方） 的值。

#int
int()
int(3.924)
int("12",base=16) #12要以字符串的形式进行输入，12 为 16进制
int('0xf',base=16)
int("10",base=8)

#open
f=open("liyuan.py")
f.read()

#str  返回对象的字符串的格式
s="python"
str(s)
dict={"python":"homework","one":"1"}
str(dict)
dict

#bool 布尔类型对象可以被赋予文字值true或者false
bool(0)
bool()
bool(100)
issubclass(bool,int) #bool 是 int 子类

#exec
exec('print("hello world!")')
exec("print('python')")
exec("""for i in range(5):
    print ("iter time: %d" %i)
    """)

expr="""
z=30
sum=x+y+z
print(sum,x,y,z)
"""
def func():
    x=10
    y=20
    exec(expr)
    exec(expr,{'x':1,'y':2}) #必须是一个字典对象
    exec(expr,{'x':1,'y':2},{'y':5,'x':4})    
func()

#isinstance
a=2
isinstance(a,int)
a=1.2
isinstance(a,float)
a=[1,1,2]
isinstance(a,(int,str,list))
class A:
    pass
class B(A):
    pass
isinstance(A(),A)
type(A())==A
isinstance(B(),A)
type(B())==A
#type() 不会认为子类是一种父类类型，不考虑继承关系。
#isinstance() 会认为子类是一种父类类型，考虑继承关系。

#ord 返回对应的 ASCII 数值
ord("1")
ord('A')
ord('0')
ord('!')
ord('(')
ord(" ")

#sum
sum([1,2,3])
sum((1,2,3),1)
sum([0,1,2,3],2)

#bytearray
bytearray()
bytearray([1,2,3])
bytearray('python','utf-8')

#filter
def is_odd(n):
    return n % 2 == 1
newlist=list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10]))
print(newlist)

import math
def is_sqr(x):
    return math.sqrt(x)%1==0
list1=list(filter(is_sqr,range(1,101)))
print(list1)    

#issubclass
class A:
 pass
class B(A):
 pass
print(issubclass(B,A))    

class a:
 x
class v(a):
 x
issubclass(v,a)    

#pow
import math  # 导入 math 模块   
print(math.pow(100,2))    
print(pow(100,2))    
print(math.cos(3.14))
print(math.pow(100,-2))
print(math.pow(3,0))
pow(100,-2)
print(math.pow(2,10))
pow(2,4,3) #pow(x,y) %z

#super
class fooparent(object):
    def __init__(self):
        self.parent="I\'m the parent"
        print("parent")
    def bar(self,message):
        print("%s from parent" % message)
class foochild(fooparent):
    def __init__(self):
        super(foochild,self).__init__()
        print("child")
    def bar(self,message):
        super(foochild,self).bar(message)
        print("child bar function")
        print(self.parent)
if __name__ =='__main__':
    fooChild=foochild()
    fooChild.bar("hello world!")

#bytes
a=bytes([1,2,3,4])
a
type(a)
a=bytes('hello',"ascii")
a
type(a)

#float
float(1)
float("12314.32423")
float(-12314.32423)

#iter   函数用来生成迭代器
list1=[0,1,2,3,4,5]
for i in iter(list1):
    print(i+1)

#print
print("python")    
a="python"
b='homework'
print(a,b)
print('a''b')
print('a','c')
print("www","taobao","com",sep=".")

#tuple
list1=["taobao","jindong"]
tuple1=tuple(list1)
tuple1

#callable 对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True
callable(0)
callable("python")
def add(a,b):
    return a+b
callable(add) #检查一个对象是否是可调用的
class A:
    def method(self):
        return 0
callable(A)
a=A()  
callable(a)  # 没有实现 __call__, 返回 False
class B:
    def __call__(self):
        return 0
callable(B)
b=B()  
callable(b)   # 实现 __call__, 返回 True

#format
"{} {}".format("hello","world")
"{0} {1}".format("python","homework")
"{1} {4} {2}".format(0,1,2,3,4,5)
print("软件名：{a},作业:{b}".format(a="python",b="homework"))
site={"a":"python","b":"homework"}
print("软件名：{a},作业:{b}".format(**site))
list1=["python","homework"]
print("软件名：{0[0]},作业:{0[1]}".format(list1))
class assignvalue(object):
    def __init__(self,value):
        self.value =value
my_value=assignvalue(6)
print("value 为:{0.value}".format(my_value))
print("{:.2f}".format(3.1415926))
"{:b}".format(11)  #b、d、o、x 分别是二进制、十进制、八进制、十六进制
"{:d}".format(11)
"{:o}".format(11)
"{:x}".format(11)
"{:#X}".format(11)
print("{}对应的位置是{{0}}".format("python"))

#len
a="python"
len(a)
l=[1,2,3,4,5]
len(l)

#property
    fget -- 获取属性值的函数
    fset -- 设置属性值的函数
    fdel -- 删除属性值函数
    doc -- 属性描述信息
class c(object):
    def __init__(self):
        self._x =None
    def getx(self):
        return self._x
    def setx(self,value):
        self._x = value
    def delx(self):
        del self._x
x=property(getx,setx,delx,"I\'m the \'x\' property")
???

#type
type(1)
type("python")       
type({"one":1})
type([1,2,3])
x=[1,3,5]
type(x)==list
class x(object):
    a=1
type("x",(object,),dict(a=1))  # 产生一个新的类型 X
type(x)

#chr 返回值是当前整数对应的ascii字符。
print(chr(0x30),chr(0x31),chr(0x61))
print(chr(48),chr(49),chr(97))
ord("1")

#frozenset 冻结后集合不能再添加或删除任何元素
a=frozenset(range(10))
a
b=frozenset("python")
b

#list
tup=(123,"python","taobao")
list1=list(tup)
print(list1)
str="hello"
print(list(str))
list(str)

#range
range(10)
list(range(1,10))
list(range(0,30,5))
list(range(0,-10,-2))
list(range(1,0))
list(range(0))
x="python"
for i in range(len(x)):
    print(x[i])

#vars 返回对象object的属性和属性值的字典对象
 print(vars())   
class x:
    a=1
print(vars(x))
X=x()
print(vars(x))

#classmethod
class x(object):
    bar=1
    def func1(self):
        print("foo")
    @classmethod
    def func2(cls):
        print("func2")
        print(cls.bar)
        cls().func1()
x.func2()

#getattr
class x(object):
    bar=1
X=x()
getattr(X,"bar")
getattr(X,"bar2",3) # 属性 bar2 不存在，但设置了默认值

#locals
def python(arg):  # 两个局部变量：arg、z
    z=1
    print(locals())
python(4)  # 返回一个名字/值对的字典

#repr   返回一个对象的 string 格式。
s="python"
repr(s)
dict={"one":1}
repr(dict)

#zip
a=[1,2,3]
b=[2,3,4]
c=[1,2,3,4,5,6]
l=list(zip(a,b))
list(zip(*l))
list(zip(b,c))
#compile
str="for i in range(0,10): print(i)"

#compile
str="for i in range(0,10):print(i)"
c=compile(str,'','exec')
c
exec(c)
str="3*4+4"
a=compile(str,'','eval')
eval(a)

#globals   以字典类型返回当前位置的全部全局变量。
a="python"
print(globals())

#map
def square(x):
    return x**2
list(map(square,[1,2,3,4,5]))
list(map(lambda x,y:x+y,[1,3,5,7,9],[2,4,6,8,10]))
list(map(lambda x:x**2,[2,3,4]))

#reversed
a="python"
b=("h",'o','m','e')
c=range(1,10)
d=[1,2,3,4,5]
print(list(reversed(a)))
print(list(reversed(b)))
print(list(reversed(c)))
print(list(reversed(d)))

#_import_
import os
print('python.%s' % id(os))
import sys
__import__('内置函数-练习')

#complex
complex(1,2)
complex(1,0)
complex("1")
complex("1+2j")

#hasattr  判断对象是否包含对应的属性。
class coordinate:
    x=10
    y=-5
    z=0
point1=coordinate()
print(hasattr(point1,'x'))
print(hasattr(point1,'y'))
print(hasattr(point1,'z'))
print(hasattr(point1,'yes'))
print(hasattr(point1,'x=10'))

#max
print(max(1,2,3,0))
print(max(-19,1,2,-100))

#round
print(round(1458175410.355132546543234))
print(round(1458175410.355132546543234,1))
print(round(1458175410.355132546543234,2))
print(round(1458175410.355132546543234,3))
print(round(1458175410.355132546543234,-2))
print(round(10.0000009,3))

#delattr
class coordinate:
    x=10
    y=-5
    z=0
point1=coordinate()
print(hasattr(point1,'x'))
print(hasattr(point1,'y'))
print(hasattr(point1,'z'))
delattr(coordinate,'z')
print("x=",point1.x)
print('y=',point1.y)
print('z=',point1.z)

#hash
hash("test")
hash(1)
hash(tuple([1,2]))
hash(tuple(sorted({'1':1})))

#memoryview    返回给定参数的内存查看对象
v = memoryview(b"asdfghjkl")
v[1]
v[1:4].tobytes()

#set
x=set("python")
y=set("homework")
x,y  # 重复的被删除
x&y # 交集
x|y # 并集
x-y  # 差集
