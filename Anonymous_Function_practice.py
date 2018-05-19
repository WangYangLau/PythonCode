#!/usr/bin/python
# -*- coding:utf-8 -*-
#功能：用匿名函数改造下面的代码
#源代码：
def is_odd(n):
    return n%2 == 1

#修改后
L=list(filter( lambda n:n%2==1,range(1,20)))
print(L)