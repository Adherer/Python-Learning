# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
# 函数本身也可以赋值给变量，即：变量可以指向函数。原因在于函数名其实就是指向函数的变量

# 高阶函数的定义(本质上就是传入函数作为参数)
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

# demo
def add(x, y, f):
    return f(x) + f(y)

print(add(5, 6, abs))
'''
当我们调用add(-5, 6, abs)时，参数x，y和f分别接收-5，6和abs，根据函数定义，我们可以推导计算过程为：

x = -5
y = 6
f = abs
f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
return 11
'''

# map() / reduce()
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# demo
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，
# 因此通过list()函数让它把整个序列都计算出来并返回一个list。

# map()的作用
# map()作为高阶函数，事实上它把运算规则抽象了，如上所示，把f(x)作用在list的每一个元素并把结果生成一个新的list

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
# 其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# demo
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

print(str2int('13579'))

# filter()
# filter()函数用于过滤序列，filter()接收一个函数和一个序列。
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
# demo 把一个序列中的空字符串删掉，可以这么写(为什么?这个代码没有看懂，问题暂时留着)
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# sorted()(默认情况下，对字符串排序，是按照ASCII的大小比较的)
# sorted()函数也是一个高阶函数，它可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))
# 给sorted传入key函数，即可实现忽略大小写的排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))