# 问题引入： 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
# 判断对象类型，使用type()函数，type()函数返回的是对应的Class类型：
'''
>>> type(123)
<class 'int'>
>>> type('str')
<class 'str'>
>>> type(None)
<type(None) 'NoneType'>
>>> type(abs)
<class 'builtin_function_or_method'>
'''

'''
判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：

>>> import types
>>> def fn():
...     pass
...
>>> type(fn)==types.FunctionType
True
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))==types.GeneratorType
True
'''

# 要判断class的类型，可以使用isinstance()函数

# 二者的联系
'''
能用type()判断的基本类型也可以用isinstance()判断
并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
>>> isinstance([1, 2, 3], (list, tuple))
True
>>> isinstance((1, 2, 3), (list, tuple))
True

注意： 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
'''

# 要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态

# 小结
# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。
# 要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。

# Demo1 完整代码
# type()

print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
print('type(abs) =', type(abs))
print('type(\'abc\')==str?', type('abc')==str)

# Attrs
class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x')) # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y')) # 获取属性'y'
print('obj.y =', obj.y) # 获取属性'y'

print('getattr(obj, \'z\') =',getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

f = getattr(obj, 'power') # 获取属性'power'
print(f)
print(f())

# 实例属性 & 类属性
# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：

class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

# 给类绑定属性可以直接在class中定义属性，这种属性是类属性，归Student类所有：
class Student(object):
    name = 'Student'
# 小结
'''
实例属性属于各个实例所有，互不干扰；
类属性属于类所有，所有实例共享一个属性；
不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
'''

# Demo2 完整代码
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')