# 装饰器(Decorator)的定义
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 本质上，decorator就是一个返回函数的高阶函数

# demo
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
    print('2018-3-27')

now()

# 把@log放到now()函数的定义处，相当于执行了语句：
# now = log(now)

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
# 比如，要自定义log的文本：
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2017-3-27')

now()
# 和两层嵌套的decorator相比，3层嵌套的效果是这样的:now = log('execute')(now)
'''
来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，
再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
'''

print(now.__name__)  # wrapper 因为返回的那个wrapper()函数名字就是'wrapper'
# 针对以上__name__的解决方法: 在定义wrapper()的前面加上@functools.wraps(func)即可。
# 这时执行print(now.__name__) 结果则为 now

# Partial function
# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
# 偏函数也可用于降低函数调用的难度
# demo
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
# 64
print(int2('1010101'))
# 85
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单,注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，
# 但也可以在函数调用时传入其他值，如：int2('1000000', base=10)

# 偏函数本质说明
'''
创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：

int2 = functools.partial(int, base=2)
实际上固定了int()函数的关键字参数base，也就是：

int2('10010')
相当于：

kw = { 'base': 2 }
int('10010', **kw)

又例如当传入：

max2 = functools.partial(max, 10)
实际上会把10作为*args的一部分自动加到左边，也就是：

max2(5, 6, 7)
相当于：

args = (10, 5, 6, 7)
max(*args)
结果为10。
'''
