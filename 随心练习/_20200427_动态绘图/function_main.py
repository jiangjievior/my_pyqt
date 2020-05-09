import os
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from window_show_picture import Ui_MainWindow
from PyQt5.QtGui import  QPixmap
import numpy as np
import matplotlib.pyplot as plt

class ShowPicture(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(ShowPicture, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('绘制正态分布随机数图像')
        os.getcwd()

        if os.path.exists('.\数据\图片')==False:
            os.makedirs('.\数据\图片')

        #滑动条设置
        self.Slider_numbers.setRange(0,10000)
        self.Slider_numbers.setSingleStep(1)
        self.Slider_mean.setRange(-1000,1000)
        self.Slider_mean.setSingleStep(1)
        self.Slider_var.setRange(0,10000)
        self.Slider_var.setSingleStep(1)
        
        self.Slider_numbers.valueChanged.connect(lambda :self.lineEdit_numbers.setText(str(self.Slider_numbers.value())))
        self.Slider_mean.valueChanged.connect(lambda :self.lineEdit_mean.setText(str(self.Slider_mean.value())))
        self.Slider_var.valueChanged.connect(lambda :self.lineEdit_var.setText(str(self.Slider_var.value())))

        self.lineEdit_numbers.textChanged.connect(lambda :self.Slider_numbers.setValue(int(self.lineEdit_numbers.text())))
        self.lineEdit_mean.textChanged.connect(lambda :self.Slider_mean.setValue(int(self.lineEdit_mean.text())))
        self.lineEdit_var.textChanged.connect(lambda :self.Slider_var.setValue(int(self.lineEdit_var.text())))

    def make_data(self):
        data = np.random.normal(int(self.Slider_mean.value()),int(self.Slider_var.value()),int(self.Slider_numbers.value()))
        np.random.normal()
        return data

    def show_data(self):
        info='数据个数为'+str(self.Slider_numbers.value())+'\n'+'数据均值为'+str(self.Slider_mean.value())+'\n'+'数据方差为'+str(self.Slider_var.value())+'\n'
        self.screen_text.setText(info)
        #pd.DataFrame(self.make_data()).to_excel('.\数据\图片\data_.xlsx')

    def show_picture(self):
        plt.figure(num=1,figsize=(5,4))
        plt.plot(self.make_data())
        if os.path.exists('.\数据\图片\图片.jpg')==True:        
            os.remove('.\数据\图片\图片.jpg')
            plt.savefig('.\数据\图片\图片.jpg')
        else:
            plt.savefig('.\数据\图片\图片.jpg')
        self.screen_picture.setPixmap(QPixmap('./数据/图片/图片.jpg'))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ShowPicture()
    main.show()
    sys.exit(app.exec_())





