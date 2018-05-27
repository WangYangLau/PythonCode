#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#功能：继承和多态

class Animal(object):
    def run(self):
        print("Animal is running...")

class Dog(Animal):
    def run(self):
        print("Dog is running...")

class Cat(Animal):
    def run(self):
        print("Cat is running...")

class Tortoise(Animal):
    def run(self):
        print("Tortoise is running...")

def run_twice(animal):
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())