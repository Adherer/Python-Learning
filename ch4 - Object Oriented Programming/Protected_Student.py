# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，
# 就变成了一个私有变量（private），只有内部可以访问，外部不能访问(即在类的外部无法通过实例变量.属性名访问该内部属性)

'''
注意：1. 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的
     2. 以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
        当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
     3. 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为
        Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
        >>> bart._Student__name
            'Bart Simpson'
'''
'''
特别注意一个易错点：
    >>> bart = Student('Bart Simpson', 59)
    >>> bart.get_name()
        'Bart Simpson'
    >>> bart.__name = 'New Name' # 设置__name变量！
    >>> bart.__name
        'New Name'

    表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
    内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。 
'''

# Demo完整代码
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

print('DO NOT use bart._Student__name:', bart._Student__name)