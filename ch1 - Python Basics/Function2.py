#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 可变参数
# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# demo
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，
# 因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
print(calc(1, 2))
# 5
print(calc())
# 0

# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3]
print(calc(*nums))
# 14

# 关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# 函数person除了必选参数name和age外，还接受关键字参数kw。

# 1.只传入必选参数
person('Michael', 30)
# name: Michael age: 30 other: {}

# 2.传入任意个数的关键字参数
person('Bob', 35, city='Beijing')
# name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer')
# name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

# 关键字参数的作用
'''
它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，
但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，
除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
'''
# 扩展内容
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
# name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
'''
如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：

def person(name, age, *, city, job):
    print(name, age, city, job)
和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
调用方式如下：
>>> person('Jack', 24, city='Beijing', job='Engineer')
Jack 24 Beijing Engineer

如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：

def person(name, age, *args, city, job):
    print(name, age, args, city, job)

命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错。

命名关键字参数可以有缺省值，从而简化调用：

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
    
使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
'''

# 总结
'''
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数(不可以变的)和关键字参数(可以变的)。
'''
# demo
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
# 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。
# 总结几个小点
'''
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
要注意定义可变参数和关键字参数的语法：
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''