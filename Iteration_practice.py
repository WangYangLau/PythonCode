#!/usr/bin/python
# -*- coding:utf-8 -*-
#功能：使用迭代查找一个list中最小和最大值，并返回一个tuple

from collections import Iterable
def findMinAndMax(L):
    if not isinstance(L,Iterable):
        raise TypeError("Error Input")
    if L == []:
        return (None,None)
    elif len(L) == 1:
        return (L[0],L[0])
    else:
        Min = L[0]
        Max = L[0]
        count = 0
        while count < len(L)-1 :
            count = count + 1
            if L[count] > Max:
                Max = L[count]
            elif L[count] < Min:
                Min = L[count]
            else:
                pass
        return (Min,Max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
