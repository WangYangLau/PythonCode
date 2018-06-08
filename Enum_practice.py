#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#功能：把Student的gender属性改造为枚举类型，可以避免使用字符串

from enum import  Enum

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self,name,value):
        self.name = name
        self.gender = Gender(value)

bart = Student('Bart', 0)
print(bart.gender)
print(Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')