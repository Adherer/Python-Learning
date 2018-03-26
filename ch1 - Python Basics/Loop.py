#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python中有两种循环,分别为:for循环和while循环
# for循环 demo
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。

# Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。
# range(index)生成的序列是从0开始小于index的整数，整数范围是[0,index)
# demo
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# while循环 demo
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)