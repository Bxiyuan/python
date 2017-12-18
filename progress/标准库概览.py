# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 20:57:32 2017

@author: dell
"""

import os
os.getcwd()
os.chdir("D:\git\python\progress")
os.system("fibo")
os.system("mkdir today")
dir(os)
help(os)
import shutil
# ?  shutil.copyfile("data.db","archive.db")

#glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:
import glob
glob.glob("*.py")

import sys
print(sys.argv)

import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
"tea for too".replace("too","two")
import math
math.cos(math.pi/4)
math.log(1024,2)

import random
random.choice(["apple","pear","banana"])
random.sample(range(100),10)
random.random()
random.randrange(6)   # # random integer chosen from range(6)

#访问 互联网
from urllib.request import urlopen
for line in urlopen("http://tycho.usno.navy.mil/cgi-bin/timer.pl"):
    line = line.decode("utf-8")
    if "EST" in line or "EDT" in line:
        print(line)

import smtplib
server=smtplib.SMTP("localhost")
server.sendmail("932245547@qq.com","M201770026@hust.edu.cn",
                """To:M201770026@hust.edu.cn
                From:932245547@qq.com
                
                Beware the Ides of March.
                """)
server.quit()

#日期和时间
from datetime import date
now = date.today()
now
now.strftime("%m-%d-%y.%d %b %Y is a %A on the %d day of %B.")
birthday=date(1993,7,18)
age=now-birthday
age.days

#数据压缩
import zlib
s = b"witch which has which witches wrist watch"
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(t)
a=b"asd"
len(a)

#性能度量
#有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。
from timeit import Timer
Timer("t=a;a=b;b=t","a=1;b=2").timeit()
Timer("a,b=b,a","a=1;b=2").timeit()

#测试模块
def average(values):
    """Computes the arithmetic mean of a list of numbers.
    
    >>>print (average([20,30,70]))
    40.0
    """
    return sum(values)/len(values)
    import doctest
    doctest.testmod()

import unittest
class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20,30,70]),40.0)
        self.assertEqual(round(average([1,5,7]),1),4.3)
        self.assertRaises(ZeroDiviisionError,average,[])
        self.assertRaises(TypeError,average,20,30,70)
unittest.main()









