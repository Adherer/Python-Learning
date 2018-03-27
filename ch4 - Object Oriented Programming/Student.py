# 在Python中，定义类是通过class关键字，例如：

'''
class Student(object):
    pass
class后面紧接着是类名，即Student，类名通常是大写开头的单词，
紧接着是(object)，表示该类是从哪个类继承下来的，
通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
'''

'''
由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

注意：1.__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，
       就可以把各种属性绑定到self，因为self就指向创建的实例本身。
     2.有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
       但self不需要传，Python解释器自己会把实例变量传进去。
     3.和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
'''

'''
特别注意：和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，
         对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
例如：
>>> bart = Student('Bart Simpson', 59)
>>> lisa = Student('Lisa Simpson', 87)
>>> bart.age = 8
>>> bart.age
8
>>> lisa.age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'
'''

# Demo完整代码
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name =', bart.name)
print('bart.score =', bart.score)
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())