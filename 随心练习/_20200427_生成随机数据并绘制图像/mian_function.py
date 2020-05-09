from PyQt5.Qt import *
from windows_ui import Ui_Form#从由QTdesigner生成的ui文件转化而来的py文件中导入类Ui_Form
from basic_function import *

class Window(QWidget,Ui_Form):#创建类window，并继承基础类QWidget，以及由QTdesigner生成的类Ui_Form
      def __init__(self):
          super().__init__()
          self.setWindowTitle("登陆界面")
          #self.resize(500,500)
          self.setupUi(self)#由于同时继承了两个类，故可以直接只用类中的方法setupUi(),并传入参数self
          self.Data=DataProcess()

      def setup_ui(self):
          pass
      
      def creat_random_data(self):
          self.Data.creat_random_data(int(self.lineEdit_rows.text()),int(self.lineEdit_cols.text()))

      def plot_plt(self):
          self.Data.plot_plt(int(self.lineEdit_rows.text()),int(self.lineEdit_cols.text()),int(self.lineEdit_specol.text()))

      def scatter_plt(self):
          self.Data.scatter_plt(int(self.lineEdit_rows.text()),int(self.lineEdit_cols.text()),int(self.lineEdit_specol.text()))

      def to_excel(self):
          self.Data.to_excel(int(self.lineEdit_rows.text()),int(self.lineEdit_cols.text()),self.lineEdit_path.text(),self.lineEdit_file_name.text())

if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())




















