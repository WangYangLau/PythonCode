#!usr/bin/env python3
# -*- coding:utf-8 -*-
#功能：根据用户的输入来执行后端的操作

from Inherited_Polymorphic_practice import Dog
dog = Dog()

def run(x):
    inp = input('method>')
    method = hasattr(dog,inp)
    if method:
        geta = getattr(dog,inp)
        geta()
    else:
        setattr(dog,inp,lambda x:x*x)
        fn = getattr(dog,inp)
        print(fn(x))

if __name__ == '__main__':
    run(10)