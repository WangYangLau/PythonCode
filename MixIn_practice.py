#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#多重继承

class Animal(object):
    def run1(self):
        print('Animal is running ...')

class MammalMixIn(object):
    def run2(self):
        print('Mammal is running ...')

class Dog(Animal,MammalMixIn):
    pass

Dog().run1()
Dog().run2()