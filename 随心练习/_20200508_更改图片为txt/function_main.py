from picture_process import *
from window_main import *
from PyQt5.Qt import QMainWindow,QFileDialog,QPixmap,QApplication
import sys

class Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.UI()

    def UI(self):
        self.setupUi(self)
        self.picture=PictureProcess()
        self.pushButton_creat_picture.clicked.connect(self.to_picture)
        self.pushButton_creat_txt.clicked.connect(self.to_txt)
        self.pushButton_show_picture.clicked.connect(self.show_picture)
        self.pushButton_show_txt.clicked.connect(self.show_txt)
        self.pushButton_select_picture.clicked.connect(self.select_picture)
        self.pushButton_select_txt.clicked.connect(self.select_file)

    def select_picture(self):
        self.frame, _ = QFileDialog.getOpenFileName(self, '打开文件', '.','图像文件(*.jpg *.png)')  # 打开文件，'打开文件'为标题，'.'为默认打开的目录，'图像文件(*.jpg*.png)'表示可以打开这两种格式图片,使用frame获得图片内容
        self.lineEdit_picture.setText(self.frame)

    def select_file(self):
        frame,_=QFileDialog.getOpenFileName(self,'打开文件','.','文本文件(*.txt *.ini)')#打开文件，'打开文件'为标题，'.'为默认打开的目录，'图像文件(*.jpg*.png)'表示可以打开这两种格式图片,使用frame获得图片内容
        self.lineEdit_txt.setText(frame)

    def to_txt(self):
        """将图片转化为txt文件"""
        self.picture.to_txt(self.lineEdit_picture.text(),self.lineEdit_txt.text())

    def to_picture(self):
        """将txt文件转化为图片"""
        self.picture.to_picture(self.lineEdit_picture.text(),self.lineEdit_txt.text())

    def show_picture(self):
        """展示图片"""
        self.screen_single.setPixmap(QPixmap(self.frame))

    def show_txt(self):
        """展示转换成的txt"""
        str=self.picture.to_str(self.lineEdit_picture.text())
        self.screen_single.setText(str)

if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = Window()
        main.show()
        sys.exit(app.exec_())
























