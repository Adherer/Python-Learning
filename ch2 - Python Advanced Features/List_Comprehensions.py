# 如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
# 方法一是循环：
'''
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
结果: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
# 利用列表生成式则可以用一行语句代替循环生成上面的list: [x * x for x in range(1, 11)]
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：[x * x for x in range(1, 11) if x % 2 == 0]
# 还可以使用两层循环，可以生成全排列：[m + n for m in 'ABC' for n in 'XYZ']

# 列表生成式也可以使用两个变量来生成list：
'''
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])
结果: ['y=B', 'x=A', 'z=C']
'''