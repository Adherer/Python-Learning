# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
# Python的for循环抽象程度要高于C的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，
# 如果要同时迭代key和value，可以用for k, v in d.items()。
# 字符串也是可迭代对象，因此，也可以作用于for循环：
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：isinstance([1,2,3], Iterable) 输出: True

# 如何对list实现类似Java那样的下标循环操作？
# 答： Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身，下面是一个例子：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)

    min = L[0]
    max = L[0]

    for val in L:
        if val > max:
            max = val
        if val < min:
            min = val

    return (min, max)