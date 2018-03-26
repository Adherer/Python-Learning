#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
if判断条件可以简写，比如写：

if x:
    print('True')
只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
'''
# demo
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
