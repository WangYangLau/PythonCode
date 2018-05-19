#!/usr/bin/python
# -*- coding:utf-8 -*-
#功能：请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志

import functools
def log(text):
    if not callable(text) :
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print('begin call')
                func(*args,**kw)
                print('end call')
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args,**kw):
            print('begin call')
            text(*args, **kw)
            print('end call')
        return wrapper

@log
def f():
    print('running')

f()