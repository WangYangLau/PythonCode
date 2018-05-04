#!/usr/bin/python
# -*- coding:utf-8 -*-
#功能：把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字

def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)