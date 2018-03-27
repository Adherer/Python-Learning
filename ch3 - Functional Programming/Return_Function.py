# demo
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
# 调用函数f时，才真正计算求和的结果
print(f())
'''
在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
'''
# 注意: 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数

# 闭包(闭包这块学的不好，后续再返回咀嚼)
# 闭包的一个易错点
# 一是注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用。
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())   # 9
print(f2())   # 9
print(f3())   # 9

# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
# 因此，返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 如果一定要引用循环变量怎么办？
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

# 这个代码片段没看懂
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print(f1())   # 1
print(f2())   # 4
print(f3())   # 9

# 匿名函数
# 在Python中，对匿名函数提供了有限支持。以map()函数为例
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
'''
匿名函数lambda x: x * x实际上就是：

def f(x):
    return x * x
关键字lambda表示匿名函数，冒号前面的x表示函数参数。
'''
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

# 匿名函数的好处
'''
1.函数没有名字，不必担心函数名冲突
2.匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
'''
f = lambda x: x * x
print(f)
print(f(5))

# 3.可以把匿名函数作为返回值返回(返回一个函数)
def build(x, y):
    return lambda: x * x + y * y

f = build(3, 3)
print(f())