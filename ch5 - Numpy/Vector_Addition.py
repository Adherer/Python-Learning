import sys
from datetime import datetime
import numpy as np

"""
该段代码演示Python中的向量加法
n为指定向量大小的整数

加法中的第一个向量包含0到n的整数的平方
第二个向量包含0到n的整数的立方
程序将打印出向量加和后的最后两个元素以及运行消耗的时间
"""

def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b

    return c

def pythonsum(n):
    a = list(range(n))
    b = list(range(n))
    c = []

    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])

    return c

size = int(sys.argv[1])

start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum", c[-2:])
print("PythonSum elapsed time in microseconds", delta.microseconds)

start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum", c[-2:])
print("NumPySum elapsed time in microseconds", delta.microseconds)

"""
当n=1000时
The last 2 elements of the sum [995007996, 998001000]
PythonSum elapsed time in microseconds 1168
The last 2 elements of the sum [995007996 998001000]
NumPySum elapsed time in microseconds 423

当n=2000时
The last 2 elements of the sum [7980015996, 7992002000]
PythonSum elapsed time in microseconds 3577
The last 2 elements of the sum [7980015996 7992002000]
NumPySum elapsed time in microseconds 596

当n=10000时
The last 2 elements of the sum [999500079996, 999800010000]
PythonSum elapsed time in microseconds 10719
The last 2 elements of the sum [999500079996 999800010000]
NumPySum elapsed time in microseconds 887

注意以上函数输出的一个小差异：
numpysum()函数的输出不包含逗号，原因是我们使用的是NumPy数组，而非Python自身的list容器
"""