# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 09:44:41 2017

@author: user
"""
#斐波纳契数列
# 两个元素的总和确定了下一个数
a,b=0,1
while b<100:
    print(b)
    a,b=b,a+b

i=25*25
print("i=",i)

a,b=0,1
while b<500:
    print(b,end=",")
    a,b=b,a+b

a=10;b=20;c="python" 
print(a,b,c,sep="#")

var=100
if var:
    print("1-if表达式条件为T")
    print(var)
var1=0#从结果可以看到由于变量 var2 为 0，所以对应的 if 内的语句没有执行。
if var1:
    print("2-if表达式条件为T")
    print(var1)
print("good bye!")


age=int(input("请输入你家狗狗的年龄："))
print('')
if age<=0:
    print("你是在逗我吧!")
elif age==1:
    print('相当于 14 岁的人。')
elif age==2:
    print("相当于 22 岁的人。")
elif age>2:
    human=22+(age-2)*5
    print("对应人类年龄:",human)
input("点击 enter 键退出")

print(3==4)
x=2
y=1
print(x==y)
n=7
guess=-1
print("数字猜谜游戏!")
while guess!=n:
    guess=int(input("请输入你猜的数字："))
    if guess==n:
        print("恭喜，你猜对了！")
    elif guess<n:
        print("猜的数字小了...")
    elif guess>n:
        print("猜的数字大了...")

num=int(input("输入一个数字："))
if num%2==0:
    if num%3==0:
        print("你输入的数字可以整除 2 和 3")
    else:
        print("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print("输入的数字可以整除 3，但不能整除2")
    else:
        print("你输入的数字不能整除 2 和3 ")

import random
x=random.choice(range(100))

a = 1
i = 0
while a != 20:
   a = int (input ('请输入你猜的数字：'))
   i += 1     
   if a == 20:
      if i<3:
         print('真厉害，这么快就猜对了！')
      else :
         print('总算猜对了，恭喜恭喜！')
   elif a < 20:
      print('你猜的数字小了，不要灰心，继续努力！')
   else :
      print('你猜的数字大了，不要灰心，继续加油！')

n=10
sum=0
counter=1
while counter<=n:
    sum=sum+counter
    counter += 1
print("1 到 %d 之和为: %d" % (n,sum)) 

var=1
while var==1:
    num=int(input("输入一个数字  :"))
    print("你输入的数字是: ", num)
print("good bye!")
    
count=0
while count<6:
    print(count,"<6")
    count+=1#count=count+!
else:
    print(count,">=6")

flag=1
while(flag):print("python")
print("good bye!")

languages=["c","c++","python"]
for x in languages:
    print(x)

sites=["baidu","google","python"]
for site in sites:
    if site=="python":
        print("homework")
        break
    print("循环数据"+site)
else:
    print("没有循环数据!")
print("完成循环!")
    
for i in range(10):
    print(i)
for i in range(3,7):
    print(i)
for i in range(0,100,5):
    print(i)

a=["google","baidu","taobao","python"]
for i in range(len(a)):
    print(i,a[i])

for letter in"python":
    if letter=="n":
        break
    print("当前字母为 :",letter)
var=10
while var>0:
    print("当期变量值为 :",var)
    var-=1
    if var==5:
        break
print("good bey!")

for letter in"python":
    if letter=="t":
        continue
    print("当前字母为 :",letter)
var=10
while var>0:
    var-=1
    if var==5:  # 变量为 5 时跳过输出
       continue 
    print("当期变量值为 :",var)
print("good bey!")

for n in range(2,100):
    for x in range(2,n):
        if n % x==0:
            print(n,"=",x,"*",n//x)
            break
    else:
        print(n,"为质数")

while True:
    pass

class MyEmptyClass:
    pass

for i in "homework":
    if i =="o":
        pass
        print("pass")
    print("当前字母 :",i)
for i in "homework":
    if i =="o":
        break
        print("break")
    print("当前字母 :",i)
for i in "homework":
    if i =="o":
        continue
        print("continue")
    print("当前字母 :",i)

def hello():
    print("hello world!")
hello()

def area(width,height):
    return width*height
def w(name):
    print("welcome",name)
w("python")
w=5
h=23
print("width=",w,"height=",h,"area=",area(w,h))

def printme(str):
    "打印任何传入的字符串"
#选择性地使用文档字符串,用于存放函数说明
    print(str)
    return
printme("我要调用用户自定义函数!")

def c(a):
    a=10
b=3
c(b)
print(b)
def c(mylist):
    mylist.append([1,2,3])
    print(mylist)
    return
mylist=[10,20]
c(mylist)
print(mylist)

def printme(str):
    "打印任何传入的字符串"
    print(str)
    return
printme(str="我要调用用户自定义函数!")

def printinfo( name, age ):
   print ("名字: ", name)
   print ("年龄: ", age)
   return
printinfo( age=50, name="taobao" )

def printinfo(arg1,*vartuple):
    print("输入：")
    print(arg1)
    for var in vartuple:
        print(var)
    return
printinfo(10)
printinfo(10,10,20,30)
sum=lambda a,b:a+b
sum(10,20)
sum(range(1,11))

total = 0; # 这是一个全局变量
# 可写函数说明
total=10
def sum( arg1, arg2 ):
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total
sum( 10, 20 )
print ("函数外是全局变量 : ", total)

n=1
def fun():
    global n
    print(n)
    n=123
    print(n)
fun()

def outer():
    n=20
    def inner():
        nonlocal n
        n=100
        print(n)
    inner()
    print(n)
outer()

a=10
def test():
    #a=0
    a=a+1
    print(a)
test()

a=[3124,13,3124,1,1.32]
print(a.count(2),a.count(3124),a.count(1.32))
a.insert(2,-1)
a.append(2)
a
a.index(-1)
a.remove(-1)
a.reverse()
a.sort()
s=[1,2,3,4,5,6,7,8,9,0]
s.append(1)
s.append(2)
s.pop(1)
s.pop()
from collections import deque
q=deque(['join','tom','june'])
q.append("eric")
q.popleft()
q.pop()
v=[2,3,4,5,6,7]
[3*x for x in v]
[[x,x**2] for x in v]
[3*x for x in v if x>3]
[3*x for x in v if x<4]
f=['banana','pear','apple']
[weapon.strip() for weapon in f]
v1=[2,4,6]
v2=[4,3,-9]
[x*y for x in v1 for y in v2]
[x+y for x in v1 for y in v2]
[v1[i]*v2[i] for i in range(len(v1))]
[str(round(355/113,i)) for i in range(10)]
matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    ]
#转置
[[row[i] for row in matrix] for i in range(4)]
t=[]
for i in range(4):
    t.append([row[i] for row in matrix])

a=[-1,1,66,333,3,3,333,1234.4]
del a[0]
del a[2:4]
del a[:] #清空
del a #删除

t=12333,3141,'hello!'
t[0]
u=t,(1,2,3,4,5)
u

#集合
breakfast={'apple','orange','apple','pear','banana','orange'}
print(breakfast)
'orange' in breakfast
'cherry' in breakfast
a=set('efcwr')
b=set("efvfao")
a-b
a|b
a&b
a^b
[x for x in a if x not in b]

tel={"jack":4098,'sape':4139}
tel['guido']=4127
tel['jack']
del tel['sape']
tel['irv']=4127
list(tel.keys())
sorted(tel.keys())
"guido" in tel
"jack" not in tel
'sape' in tel
dict(sape=4139, guido=4127, jack=4098)

knights={'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)
for i,v in enumerate(['tic','tac','toe']):
    print(i,v)
Q=['name','quest','favorite color']    
A=['june','the holy grail','blue']    
for q, a in zip(Q,A):  
    print('What is your {0}? \n It is {1}.'.format(q,a))
for i in reversed(range(1,100,7)):
    print(i)

for f in sorted(set(breakfast)):    
    print(f)
    
    
    
    