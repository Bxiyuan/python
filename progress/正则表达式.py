# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 20:30:35 2017

@author: dell
"""

re.match(pattern,string,flags=0)
import re
print(re.match("www","www.python.com").span()) 
print(re.match("com","www.python.com"))
print(re.match("www","www.python.com"))
line='Cates are smarter than dogs'
matchObj=re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
if matchObj:
    print("matchObj.group():",matchObj.group())
    print("matchObj.group(1):",matchObj.group(1))
    print("matchObj.group(2):",matchObj.group(2))
else:
    print("No match")
matchobj=re.match(r"dogs",line,re.M|re.I)
if matchobj:
    print("match-->matchobj.group():",matchobj.group())
else:
    print("No match!")
matchobJ=re.search(r"dogs",line,re.M|re.I)
if matchobJ:
    print("match-->matchobJ.group():",matchobJ.group())
else:
    print("No match!")
phone="2017-121-232#这是一个电话号码"
num=re.sub(r"#.*$","",phone) # 删除注释
print("电话号码：",num)
num=re.sub(r"\D","",phone) # 移除非数字的内容
print("电话号码：",num)
def double(matched):
    value = int(matched.group("value"))
    return str(value*2)
s="AHNE39EEW332U"
print(re.sub("(?P<value>\d+)",double,s)) # 将匹配的数字乘于 2

























