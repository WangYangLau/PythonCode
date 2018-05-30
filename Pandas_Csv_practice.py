#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#功能:使用Pandas模块对CSV进行读写

import pandas as pd
import csv

def main():
    total_info=[[u'1',u'j',u'Adam'],
                [u'2', u'k', u'Kate'],
                [u'3', u'l', u'John']]
    df = pd.DataFrame(data = total_info,columns=[u'序号',u'代号',u'名字'])
    df.to_csv('C:\\Users\\ASUS\\Desktop\\test.csv',index=False,encoding="gb2312")
    print('保存成功！！')

if __name__ == '__main__':
    main()