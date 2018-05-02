#!/usr/bin/python
# -*- coding:utf-8 -*-
#功能：去除字符串首尾的空格

from collections import Iterable
def trim(s):
    if not isinstance(s,Iterable):
        raise TypeError('Error Input')
    count = 0
    if len(s) != 0:
        while s[count] == " ":
            if count == len(s)-1:
                return ""
            count = count + 1
        begin = count
        while s[count] != " ":
            if count == len(s)-1:
                count = count + 1
                break
            count = count + 1
            sum = count
        while sum != len(s)-1:
            if s[sum] != " ":
                count = sum
                count = count + 1
            sum = sum + 1
        end = count
        s = s[begin:end]
    return s

if trim('hello  ') != 'hello':
    print(trim('hello  '))
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print(trim('  hello'))
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print(trim('  hello  '))
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print(trim('  hello  world  '))
    print('测试失败4!')
elif trim('') != '':
    print(trim(''))
    print('测试失败5!')
elif trim('    ') != '':
    print(trim('    '))
    print('测试失败6!')
else:
    print('测试成功!')