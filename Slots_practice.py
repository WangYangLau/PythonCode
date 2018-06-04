#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from types import MethodType

class Student(object):
    pass

def set_score(self,score):
    self.score = score

Student.set_score = MethodType(set_score,Student)

s=Student()
s.set_score(9)

print(s.score)
print(Student.score)
print(dir(Student))

class Slot_Student(object):
    __slots__ = ('name','age')

s = Slot_Student
s.name='Adam'
s.age=18

class Grand_Student(Student):
    pass

g = Grand_Student()
g.score = 100