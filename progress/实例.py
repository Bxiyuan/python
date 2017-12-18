# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:09:55 2017

@author: dell
"""

print("hello world!")

num1=input("输入第一个数字：")
num2=input("输入第二个数字：")
sum=float(num1)+float(num2)
print("{0}+{1}={2}".format(num1,num2,sum))
print("两数之和为%0.1f" %(float(input("输入第一个数字："))+float(input("输入第二个数字："))))

num=float(input("请输入一个数字："))
num_sqrt=num**0.5
print("%0.3f的平方根为%0.3f" %(num,num_sqrt))
import cmath
num=int(input("请输入一个数字: "))
num_sqrt=cmath.sqrt(num)
print("{0}的平方根为{1:0.3f}+{2:0.3f}j".format(num,num_sqrt.real,num_sqrt.imag))

import cmath
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print("结果为 {0} 和 {1}".format(sol1,sol2))

import random
print(random.randint(0,9))

C= float(input('输入摄氏温度: '))
F= (C* 1.8) + 32
print('%0.1f 摄氏温度转为华氏温度为 %0.1f'%(C,F))

x = input('输入 x 值: ')
y = input('输入 y 值: ')# 创建临时变量，并交换
temp = x
x = y
y = temp
print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))
x,y=y,x

num = float(input("输入一个数字: "))
if num > 0:
   print("正数")
elif num == 0:
   print("零")
else:
   print("负数")
#---------------------------------------
num = float(input("输入一个数字: "))
if num >= 0:
   if num == 0:
       print("零")
   else:
       print("正数")
else:
   print("负数")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False
 # 测试字符串和数字
print(is_number('foo'))   
print(is_number('1'))     
print(is_number('1.3'))   
print(is_number('-1.37')) 
print(is_number('1e3'))   
 # 测试 Unicode
print(is_number('٥')) # 阿拉伯语 5
print(is_number('๒')) # 泰语 2
print(is_number('四')) # 中文数字
print(is_number('©'))  # 版权号

num = int(input("输入一个数字: "))
if (num % 2) == 0:
   print("{0} 是偶数".format(num))
else:
   print("{0} 是奇数".format(num))

year = int(input("输入一个年份: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
       else:
           print("{0} 不是闰年".format(year))
   else:
       print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
else:
   print("{0} 不是闰年".format(year))

print(max(10,-10,100))
print(max([1,2,3]))

num = int(input("请输入一个数字: "))
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"不是质数")
           print(i,"*",num//i,"=",num)
           break
   else:
       print(num,"是质数")
else:
   print(num,"不是质数")
#————————————————————————————————————
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
 
for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
            
num = int(input("请输入一个数字: "))
factorial = 1
if num < 0:
   print("抱歉，负数没有阶乘")
elif num == 0:
   print("0 的阶乘为 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("%d 的阶乘为 %d" %(num,factorial))            
            
for i in range(1, 10):
        for j in range(1, i+1):
            print('{}x{}={}\t'.format(i, j, i*j), end='')
        print()            

nterms = int(input("你需要几项？"))
n1 = 0
n2 = 1
count = 2
if nterms <= 0:
   print("请输入一个正整数。")
elif nterms == 1:
   print("斐波那契数列：")
   print(n1)
else:
   print("斐波那契数列：")
   print(n1,",",n2,end=" , ")
   while count < nterms:
       nth = n1 + n2
       print(nth,end=" , ")
       n1 = n2
       n2 = nth
       count += 1            
            
num = int(input("请输入一个数字: "))
sum=0
n=len(str(num))       
temp=num
while temp > 0:
    digit = temp %10  #余数
    sum +=digit**n
    temp//=10  #取整
if num==sum:
    print(num,"是阿姆斯特朗数")
else:
    print(num,"不是阿姆斯特朗数")
            
dec=int(input("输入数字："))    
print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))       
            
c=input("请输入一个字符: ") 
a=int(input("请输入一个ASCII码: ")) 
print(c,"的ASCII 码为",ord(c))
print(a,"对应的字符为",chr(a))          
            
def hcf(x,y):
    if x > y :
        smaller =y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if ((x % i==0) and (y % i==0)):
            hcf=i
    return hcf
num1=int(input("输入第1个数字:"))
num2=int(input("输入第2个数字:"))
print(num1,"和",num2,"的最大公约数为",hcf(num1,num2))
        
def lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while (True):
        if ((greater%x ==0) and (greater % y ==0)):
            lcm = greater
            break
        greater +=1
    return lcm
num1=int(input("输入第1个数字:"))
num2=int(input("输入第2个数字:"))
print(num1,"和",num2,"的最小公倍数为",lcm(num1,num2))

def add(x,y):    
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")
choice=input("输入你的选择(1/2/3/4):") 
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))       
if choice =="1":     
    print(num1,"+",num2,"=",add(num1,num2))
elif choice =="2":
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice =="3":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice =="4":
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("非法输入")
     
import calendar            
yy=int(input("输入年份: ")) 
mm=int(input("输入月份: "))
print(calendar.month(yy,mm))          
            
def recur_fibo(n):    
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
nterms=int(input("您要输出几项? "))
if nterms<=0:
    print("输入正数")
else:
    print("斐波那契数列:")
    for i in range(nterms):
        print(recur_fibo(i))
        
with open("test.txt","wt" ) as out_file:
    out_file.write("hello world!!!")
with open("test.txt","rt") as in_file:
    text=in_file.read()
print(text)

str="python"
print(str.isalnum()) # 判断所有字符都是数字或者字母
print(str.isalpha()) # 判断所有字符都是字母          
print(str.isdigit()) # 判断所有字符都是数字
print(str.islower()) # 判断所有字符都是小写
print(str.isupper()) # 判断所有字符都是大写
print(str.istitle()) # 判断所有单词都是首字母大写，像标题
print(str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r            
str1="python.com"
print(str1.isalnum()) # 判断所有字符都是数字或者字母
print(str1.isalpha()) # 判断所有字符都是字母          
print(str1.isdigit()) # 判断所有字符都是数字
print(str1.islower()) # 判断所有字符都是小写
print(str1.isupper()) # 判断所有字符都是大写
print(str1.istitle()) # 判断所有单词都是首字母大写，像标题
print(str1.isspace()) # 判断所有字符都是空白字符、\t、\n、\r            

str = "www.python.com"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写 
            
import calendar
monthrange=calendar.monthrange(2017,12)            
print(monthrange) # 第一天是星期⑤，该月总共有 31 天          
            
import datetime
def getyesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    return yesterday
print(getyesterday())

li=["a","b","python","z","example"]          
li            
li[2]            
li[-1]            
li[-3]            
li[1:3]            
li[1:-1]            
li.append("today")            
li            
li.insert(2,"new")            
li.extend(["c","d","c"])            
li            
li.index("new")            
li.index("x")            
"C" in li            
li.remove("c")            
li            
li.remove("o")            
li.pop()   # pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。
li=li+["example","new"]          
li            
li +=["o"]            
l=[1,2]*5            
l            
params={"a":"one","b":"two","c":"three","d":"four"}            
["%s=%s"%(v,k) for v,k in params.items()]            
s=";".join(["%s=%s" % (v,k) for v,k in params.items()])            
s.split(";")            
s.split("j",1)            
li=[1,3,5,7,9]
[elem*2 for elem in li]
params.keys()
params.values()
params.items()
[k for k,v in params.items()]
[v for k,v in params.items()]
lii=['a', 'b', 'new', 'python', 'z', 'example', 'new', 'c', 'b', 'c']
[elem for elem in lii if len(elem)>1]
[elem for elem in lii if elem !="c"]
[elem for elem in lii if lii.count(elem)==1]
import os
os.getcwd()
