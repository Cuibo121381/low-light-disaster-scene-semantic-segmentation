import csv
from matplotlib import pyplot as plt
import pandas as pd
# 读取CSV文件数据
filename = pd.read_csv('C:/Users/cui/Desktop/code/DSLR-release-861429482faf50ee3d6570948af8c48df1fc7f43/data/temp/log/loss.csv')
xdata = []
ydata = []
xdata = filename.loc[:,'Epoch']   #将csv中列名为“列名1”的列存入xdata数组中
							#如果ix报错请将其改为loc
ydata = filename.loc[:,'Loss']   #将csv中列名为“列名2”的列存入ydata数组中


# 根据数据绘制图形
plt.plot(xdata, ydata, color='r', linewidth = 2, mec='r', mfc='w', label='Train Loss')
#plt.title("a",size=10)   #设置表名为“表名”
plt.grid(True)
plt.xlabel('Epoch',size=10)   #设置x轴名为“x轴名”
plt.ylabel('Loss',size=10)   #设置y轴名为“y轴名”
plt.show()
