if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QLineEdit,QVBoxLayout,QLabel, QWidget, QPushButton, QHBoxLayout, QApplication, QMainWindow,QDesktopWidget  # 创建任何应用程序都需要QApplication
    class Print_Input(QMainWindow):
        def __init__(self):
            super(Print_Input,self).__init__()
            self.setWindowTitle('打印输出内容')

            self.enditline=QLineEdit()#输入框
            button1 = QPushButton('打印')#添加按钮
            button1.clicked.connect(self.print_input)
            self.label1 = QLabel()#显示文本标签

            self.Vlayout=QVBoxLayout()
            self.Vlayout.addWidget(self.enditline)
            self.Vlayout.addWidget(button1)
            self.Vlayout.addWidget(self.label1)

            mainFrame=QWidget()
            mainFrame.setLayout(self.Vlayout)
            self.setCentralWidget(mainFrame)

        def print_input(self):
            self.label1.setText(self.enditline.text())

    if __name__=='__main__':
        app=QApplication(sys.argv)
        main=Print_Input()
        main.show()
        sys.exit(app.exec_())







