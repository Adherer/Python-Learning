import numpy as np
i2 = np.eye(2)       # 创建一个单位矩阵，参数用于指定矩阵中1的元素个数
print(i2)
np.savetxt("eye.txt", i2)      # 将数据存储到文件中
# 利用loadtxt()函数可以处理CSV文件
# 利用average()函数可以用于计算加权平均值
# 利用mean()函数可以用于计算算术平均值
# 利用max()和min()函数可以计算最大值和最小值，ptp()函数可以用于计算数组元素最大值和最小值之间的差值(极差)
# 利用median()函数可以求得数组的中位数，msort()可以将数组排序，var()函数可以求得数组的方差，std()函数计算标准差