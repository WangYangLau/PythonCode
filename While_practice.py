# -*- conding:utf-8 -*-
#功能：循环打印出List的名字

count = 0
names = ['Mike','John','Amy']
for name in names:
    print('Hello,%s'%name)

while count <= (len(names)-1):
    print('Hello,%s'%names[count])
    count = count+1