# -*- coding:utf-8 -*-
#功能：计算人体的BMI指数

import math
height = input('Your height:')
weight = input('Your weight:')

bmi = float(weight)/(float(height)*float(height))

if bmi<18.5:
    print(u'过轻')
elif bmi<25 and bmi>=18.5:
    print(u'正常')
elif bmi<28 and bmi>=25:
    print(u'过重')
elif bmi<32 and bmi>=28:
    print(u'肥胖')
else:
    print(u'严重肥胖')