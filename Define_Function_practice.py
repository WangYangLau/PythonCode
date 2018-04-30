#!/usr/bin/python
# -*- conding:utf-8 -*-
#功能：定义一个函数，接受3个参数，返回一元二次方程的两个解

import math
def quadratic(a,b,c):
    d = (b*b)-(4*a*c)
    if d >= 0:
        x1 = ((-b)+(math.sqrt(d)))/(a*2)
        x2 = ((-b)-(math.sqrt(d)))/(a*2)
    else:
        x1 = u'无解'
        x2 = u'无解'
    return x1,x2


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
