#!/usr/bin/python
# -*- coding:utf-8 -*-
#功能：利用闭包返回一个计数器函数，每次调用它返回递增整数：
#方法一：
def createCounterA():
    def counter(L=[]):
        L.append(0)
        return len(L)
    return counter

#方法二：
def createCounterB():
    i = 0
    def counter():
        nonlocal i
        i = i + 1
        return i
    return counter

counterA = createCounterA()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounterB()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
