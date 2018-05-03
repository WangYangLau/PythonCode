#!/usr/bin/python
# -*- coding:utf-8 -*-
#功能：如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，修改列表生成式，保证列表生成式能正确地执行：

L1 = ['Hello','World',18,'Apple',None]
L2 = [n.lower() for n in L1 if isinstance(n,str)]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')