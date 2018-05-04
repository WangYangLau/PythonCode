#!/usr/bin/python
# -*- coding:utf-8 -*-
#功能：去除字符串首尾的空格

from collections import Iterable
def trim(s):
    if not isinstance(s,Iterable):
        raise TypeError('Error Input')
    while s[:1] == " ":
        s = s[1:]
    while s[-1:] == " ":
        s = s[:-1]
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