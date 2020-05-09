import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

class DataProcess():

    def creat_random_data(self,rows,cols):
        """生成指定行和列的随机数据"""
        data=np.random.rand(rows,cols)
        return data

    def plot_plt(self,rows,cols,specol):
        """绘制指定列的折线图"""
        data=self.creat_random_data(rows,cols)
        spe_data=data[:,specol]
        fig=plt.figure(figsize=(15,10))
        plt.plot(range(len(spe_data)),spe_data)
        plt.grid(True)
        plt.show()

    def scatter_plt(self,rows,cols,specol):
        """绘制指定列的散点图"""
        data = self.creat_random_data(rows, cols)
        spe_data = data[:, specol]
        fig = plt.figure(figsize=(15, 10))
        plt.scatter(range(len(spe_data)), spe_data)
        plt.grid(True)
        plt.show()

    def to_excel(self,rows,cols,path="",file_name="随机数据"):
        """将数据保存至指定文件路径为指定文件名excel表格"""
        data=self.creat_random_data(rows,cols)

        if path=="":
            path=os.getcwd()
        paths=os.path.join(path,file_name+'.xlsx')
        data=pd.DataFrame(data)
        data.to_excel(paths)




if __name__=='__main__':
    Data=DataProcess()
    Data.creat_random_data(6,7)
    Data.plot_plt(6,7,4)
    Data.scatter_plt(6,8,3)
    Data.to_excel(6,6)