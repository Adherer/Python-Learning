#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list
# Python内置的一种数据类型是列表：list。
# list是一种有序的集合，可以随时添加和删除其中的元素。(list可看成一个一维数组)
# 形式: classmates = ['Michael', 'Bob', 'Tracy']
# list里面的元素的数据类型也可以不同
# list元素也可以是另一个list(即list可以嵌套,此时list可看成一个多维数组)

# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
# 以此类推，可以获取倒数第2个(-2)、倒数第3个(-3)

'''
list常用方法：
append('xxx')   往list中追加元素到末尾
insert(index, 'xxx') 把元素插入到指定的位置
pop() 删除list末尾的元素 删除指定位置的元素：用pop(index)

要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
'''

# demo
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
# 注意记录一下这个print与交互式环境下的不同之处 (交互式应该输出s'len is 4)
print("s'len is", len(s))
print(s[2][1])

# tuple
# 另一种有序列表叫元组：tuple。tuple和list非常类似
# 但是tuple一旦初始化就不能修改，这也是tuple和list的不同之处
# 形式: classmates = ('Michael', 'Bob', 'Tracy')
# 由于classmates这个tuple不能变了，因此它也没有append()，insert()这样的方法

# tuple的意义
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

# tuple的缺陷：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来

# tuple的一个需要注意的问题(与小()的混淆)
'''
要定义一个只有1个元素的tuple，如果你这么定义：

>>> t = (1)
>>> t
1
定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，
这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。

所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：

>>> t = (1,)
>>> t
(1,)

Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。
'''

# tuple的变与不变
'''
最后来看一个“可变的”tuple：

>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])

这个tuple定义的时候有3个元素，分别是'a'，'b'和一个list。不是说tuple一旦定义后就不可变了吗？怎么后来又变了？
解答：表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
     tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，
     tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，
     指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
     
理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。
'''
