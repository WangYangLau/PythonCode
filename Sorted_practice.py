#!/usr/bin/python
# -*- coding:utf-8 -*-
#功能:我们用一组tuple表示学生名字和成绩,用sorted()对列表分别按名字排序：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
t=('Bob',75)

def by_name(t):
    return t[0]
def by_score(t):
    return t[1]

L2 = sorted(L,key=by_name)
L3 = sorted(L,key=by_score)
print(L2)
print(L3)