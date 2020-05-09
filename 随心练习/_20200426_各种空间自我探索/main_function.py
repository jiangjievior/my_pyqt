from screen import *
from PyQt5.QtWidgets import *
import sys

class ScreenShow(QWidget,Ui_Form):
    def __init__(self):
        super(ScreenShow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('数值屏幕')
        self.setupUi(self)
        self.allInputValues = [0.001]  # 所有输入的值


    #保存所有输入的数值
    def saveInputValue(self):
        self.inputValue = self.lineEdit_input.text()  # 获取输入值
        self.allInputValues.append(float(self.inputValue))

    #展示所有输入保存的数值
    def show_all_data(self):
        str_=''
        for i in self.allInputValues:
            str_+=str(i)+'\n'
        self.screen.setText(str_)

    #lcd屏和进度条展示数字
    def show_number(self):
        self.lcdNumber.display(str(self.inputValue))
        self.screen.setText('输入数字：\n'+str(self.inputValue))
        percent=round(self.allInputValues[-1]/sum(self.allInputValues),2)*100
        self.progressBar.setValue(percent)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ScreenShow()
    main.show()
    sys.exit(app.exec_())
























