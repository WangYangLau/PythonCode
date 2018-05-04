#!/usr/bin/python
# -*- coding:utf-8 -*-
#功能：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

from functools import reduce


def str2float(s):
    str = s.split(".",1)
    def str2num(s):
        Digits = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 }
        return Digits[s]
    def function(x,y):
        return x * 10 + y
    return reduce(function,list(map(str2num,str[0]))) + reduce(function,list(map(str2num,str[1])))/10 ** (len(str[1]))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')