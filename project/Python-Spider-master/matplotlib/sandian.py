#简单实例
# import numpy as np
# import matplotlib.pyplot as plt
#
# height = [161,162,163,164,165]
# weight = [50,60,70,80,90]
#
# plt.scatter(height,weight)
# plt.show()

#股票涨幅
import numpy as np
import matplotlib.pyplot as plt

#收盘和开盘的数据
open,close = np.loadtxt('01.csv',delimiter=',',skiprows=1,usecols=(1,4),unpack=True)
#收盘和开盘的涨幅度
change = close - open
#比较今天和昨天涨幅的差异，画散点图分析之间的相关性
yesterday = change[:-1]
today = change[1:]

plt.scatter(yesterday,today,s=50,c='r',marker='*',alpha=0.5)
plt.show()




