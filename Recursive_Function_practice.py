#!/usr/bin/python
# -*- coding:utf-8 -*-
#功能：汉诺塔的移动

def move(n,a,b,c):
    if n == 1:
        print(a,"-->",c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
    return 'done'

print(move(3,'A','B','C'))