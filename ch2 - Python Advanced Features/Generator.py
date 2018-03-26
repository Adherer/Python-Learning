'''
如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
'''
# 创建generator的方法
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))
print(g)
# 如果要一个一个打印出来generator的每一个元素，可以通过next()函数获得generator的下一个返回值
print(next(g))

# 注意:generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

# demo——普通函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b  # 这个是迭代的赋值语句，不必显式写出临时变量t就可以赋值
        n = n + 1
    return 'done'
fib(5)

# 改进版——fib函数变成generator(方法二)
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

# 难点(勤加复习)
'''
最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

举个简单的例子，定义一个generator，依次返回数字1，3，5：

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：

>>> o = odd()
>>> next(o)
step 1
1
>>> next(o)
step 2
3
>>> next(o)
step 3
5
>>> next(o)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''

# 改进版——fib函数变成generator的使用方式
'''
for n in fib(6):
    print(n)

1
1
2
3
5
8
'''

# 了解的点(到异常处理再复习这个点)
'''
用for循环调用generator时，拿不到generator的return语句的返回值。
如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
'''
