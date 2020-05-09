# -*- coding: utf-8 -*-


#1.示例：第一个窗口程序
if 'FirstMainWin'=='FirstMainWin':
    """
    "主窗口类型"
    QMainWindow#主窗口栏，包含菜单栏和状态栏
    QDialog#对话窗口基类，用于各种功能弹出的小对话框
    Qwidget#窗口基类，不确定使用窗口形式时使用
    """
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow#创建任何应用程序都需要QApplication
    from PyQt5.QtGui import QIcon

    class FirstMainWin(QMainWindow):
        def __init__(self,parent=None):
            super(FirstMainWin, self).__init__(parent)#继承主窗口基类属性
            self.setWindowTitle('第一个主窗口应用')#设置窗口标题
            self.resize(400,300)#改变窗口尺寸
            self.status=self.statusBar()#设置状态栏
            self.status.showMessage('只存在5秒消息',5000)#显示'只存在5秒消息'5秒

    if __name__=='__main__':
        app=QApplication(sys.argv)
        app.setWindowIcon(QIcon('./images/Dragon.icon'))#调用pyqt自带的小龙图标
        main=FirstMainWin()
        main.show()#显示窗口
        sys.exit(app.exec_())

#2.让主窗口居中
if '主窗口居中'=='主窗口居中':
    #利用QDesktopWidget
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow,QDesktopWidget  # 创建任何应用程序都需要QApplication
    from PyQt5.QtGui import QIcon

    class CenterForm(QMainWindow):
        def __init__(self, parent=None):
            super(CenterForm, self).__init__(parent)  # 继承主窗口基类属性
            self.setWindowTitle('第一个主窗口应用')  # 设置窗口标题
            self.resize(400, 300)  # 改变窗口尺寸
            self.status = self.statusBar()  # 设置状态栏
            self.status.showMessage('只存在5秒消息', 5000)  # 显示'只存在5秒消息'5秒

        def center(self):#使窗口居中的函数
            screen=QDesktopWidget().screenGeometry()#获取屏幕尺寸
            size=self.geometry()#获取屏幕尺寸
            newLeft=(screen.width()-size.width())/2
            newTop=(screen.height()-size.height())/2

            self.move(newLeft,newTop)

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon('./images/Dragon.icon'))  # 调用pyqt自带的小龙图标
        main = CenterForm()
        main.show()  # 显示窗口
        sys.exit(app.exec_())
    
#3.退出应用程序:通过手工代码关闭窗口
if '退出应用程序'=='退出应用程序':
    import sys
    from PyQt5.QtWidgets import QLabel,QWidget,QPushButton,QHBoxLayout,QApplication, QMainWindow, QDesktopWidget  # 创建任何应用程序都需要QApplication

    class QuitApplication(QMainWindow):
        def __init__(self):
            super(QuitApplication, self).__init__()  # 继承主窗口基类属性
            self.setWindowTitle('退出应用程序')  # 设置窗口标题
            self.resize(300, 120)  # 改变窗口尺寸
            self.button1=QPushButton('退出')#添加“退出”按钮
            self.button1.clicked.connect(self.onclick_button)#将点击信号于退出槽绑定

            layout=QHBoxLayout()#创建一个水平布局
            layout.addWidget(self.button1)#在水平布局中添加按钮

            mainFrame=QWidget()#窗口主布局
            mainFrame.setLayout(layout)#将水平布局放在主布局中
            self.setCentralWidget(mainFrame)

        #按钮单击事件的方法，相当于一个自定义的槽
        def onclick_button(self):
            sender=self.sender()
            print(sender.text()+'按钮被按下')
            app=QApplication.instance()
            app.quit()#退出应用程序

    if __name__ == '__main__':
            app = QApplication(sys.argv)
            main = QuitApplication()
            main.show()  # 显示窗口
            sys.exit(app.exec_())

#4.获得屏幕坐标系和尺寸
if '屏幕坐标系'=='屏幕坐标系':
    import sys
    from PyQt5.QtWidgets import QLabel,QWidget, QPushButton, QHBoxLayout, QApplication, QMainWindow, \
        QDesktopWidget  # 创建任何应用程序都需要QApplication

    def onclick_button():
        print('1')
        print('窗口的x轴坐标为%d' % widget.x())  # 查看窗口位于的横坐标值
        print('窗口的y轴坐标为%d' % widget.y())  # 查看窗口位于的纵坐标值，只有工作区，不包含菜单栏
        print('窗口的宽度为%d' % widget.width())  # 查看窗口位于的横坐标值
        print('窗口的高度为%d' % widget.height())  # 查看窗口位于的纵坐标值

        print('2')
        print('窗口的x轴坐标为%d' % widget.geometry().x())  # 查看窗口位于的横坐标值
        print('窗口的y轴坐标为%d' % widget.geometry().y())  # 查看窗口位于的纵坐标值，包含菜单栏
        print('窗口的宽度为%d' % widget.geometry().width())  # 查看窗口位于的横坐标值
        print('窗口的高度为%d' % widget.geometry().height())  # 查看窗口位于的纵坐标值

        print('3')
        print('窗口的x轴坐标为%d' % widget.frameGeometry().x())  # 查看窗口位于的横坐标值
        print('窗口的y轴坐标为%d' % widget.frameGeometry().y())  # 查看窗口位于的纵坐标值
        print('窗口的宽度为%d' % widget.frameGeometry().width())  # 查看窗口位于的横坐标值
        print('窗口的高度为%d' % widget.frameGeometry().height())  # 查看窗口位于的纵坐标值,包含菜单栏

    app=QApplication(sys.argv)
    widget=QWidget()
    button=QPushButton(widget)
    button.setText('按钮')
    button.move(24,24)#将按钮向下向右移动24个像素
    button.clicked.connect(onclick_button)

    widget.resize(300,240)
    widget.setWindowTitle('屏幕坐标系')
    widget.show()
    sys.exit(app.exec_())

#5.设置窗口和应用程序图标，用于设置主窗口的图标（未成功）
if '应用程序图标'=='应用程序图标':
    import sys
    from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QHBoxLayout, QApplication, QMainWindow, \
        QDesktopWidget  # 创建任何应用程序都需要QApplication
    from PyQt5.QtGui import QIcon

    class IconForm(QMainWindow):
        def __init__(self):
            super(IconForm,self).__init__()
            self.initUI()

        def initUI(self):
            self.setGeometry(300,300,250,250)
            self.setWindowTitle('设置窗口图标')
            self.setWindowIcon(QIcon('./images/Dragon.icon'))

    if __name__=='__main__':
        app=QApplication(sys.argv)
        main=IconForm()
        main.show()

        sys.exit(app.exec_())

#6.显示控件的提示信息:QToolTip
if '提示信息'=='提示信息':
    import sys
    from PyQt5.QtWidgets import QToolTip,QLabel, QWidget, QPushButton, QHBoxLayout, QApplication, QMainWindow, \
        QDesktopWidget  # 创建任何应用程序都需要QApplication
    from PyQt5.QtGui import QFont

    class TooltipForm(QMainWindow):#只有继承QMainWindow类才能使用setCentralWidget
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            QToolTip.setFont(QFont('SanSerif', 12))
            self.setToolTip('今天是</b>')#在屏幕上出现提示信息
            self.setGeometry(300,300,500,500)
            self.setWindowTitle('设置控件提示信息')

            self.button1=QPushButton('按钮1')
            self.button1.setToolTip('这是一个按钮')#将鼠标放在按钮上将出现提示信息
            layout=QHBoxLayout()
            layout.addWidget(self.button1)

            mainFrame = QWidget()  # 窗口主布局
            mainFrame.setLayout(layout)  # 将水平布局放在主布局中
            self.setCentralWidget(mainFrame)

    if __name__=='__main__':
        app=QApplication(sys.argv)
        main=TooltipForm()
        main.show()
        sys.exit(app.exec_())

#7.Qlabel控件的基本用法
if 'Qlabel'=='Qlabel':
    """
    setAlignment():设置文本的对齐方式
    setIndent():设置文本描述
    text()：获取文本内容
    setBuddy():设置伙伴关系
    setText():设置文本内容
    selectedText():返回所选择的字符
    setWordWrap():设置是否允许换行
    setPixmap(QPixmap(图片路径)):显示图片
    QLalbel常用的信号（事件）：1.当鼠标划过Qlabel控件时触发：linkHovered
                             2.当鼠标单击QLabel控件时触发：linkActivated
    """
    import sys
    from PyQt5.QtWidgets import QVBoxLayout,QMainWindow,QApplication,QPushButton,QWidget,QLabel
    from PyQt5.QtGui import  QPalette,QPixmap
    from PyQt5.QtCore import Qt

    class QLabelDemo(QWidget):
        def __init__(self):
            super(QLabelDemo, self).__init__()
            self.initUI()
            self.setGeometry(300,300,450,450)

        def initUI(self):
            label1=QLabel(self)
            label2 = QLabel(self)
            label3 = QLabel(self)
            label4 = QLabel(self)

            label1.setText("<font color=yellow>显示图片.</font>")#设置文本
            label1.setAutoFillBackground(True)#填充整个屏幕
            palette=QPalette()#设置调色板显示图片或规整的字体
            palette.setColor(QPalette.Window,Qt.blue)#设置背景色
            label1.setPalette(palette)
            label1.setAlignment(Qt.AlignCenter)#设置文字居中方式，字体居中

            label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")#网页

            label3.setAlignment(Qt.AlignCenter)#居中
            label3.setToolTip('这是一个图片标签')
            label3.setPixmap(QPixmap('F:/python笔记/my_pyqt/随心练习/_20200427_动态绘图/数据/图片/图片.jpg'))#显示图片出来

            label4.setOpenExternalLinks(True)#True打开浏览器指定网页，Flase则调用槽函数
            label4.setText("<a href='https://map.baidu.com/@12819555,4375706,13z'>百度地图网页</a>")
            label4.setAlignment(Qt.AlignRight)
            label4.setToolTip('这是一个超级链接')

            vbox=QVBoxLayout()
            vbox.addWidget(label1)
            vbox.addWidget(label2)
            vbox.addWidget(label3)
            vbox.addWidget(label4)

            label2.linkHovered.connect(self.linkHovered)
            label4.linkActivated.connect(self.linkClicked)

            self.setLayout(vbox)
            self.setWindowTitle('Label控件展示')

        def linkHovered(self):
            print('当鼠标划过label2时，触发事件')

        def linkClicked(self):
            print('当鼠标划过label4时，触发事件')

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = QLabelDemo()
        main.show()
        sys.exit(app.exec_())

#8.Qlabel与伙伴关系
if '伙伴关系'=='伙伴关系':
    """
    伙伴关系：通过热键利用label控制其他控件，并通过Tab键切换选中
    """
    import sys
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import QPalette, QPixmap
    from PyQt5.QtCore import Qt

    class QlabelBuddy(QDialog):#继承对话框
        def __init__(self):
            super(QlabelBuddy, self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('Qlabel与伙伴控件')

            nameLabel=QLabel('&Name',self)#建立账号标签
            nameLineEdit=QLineEdit(self)#建立账号输入框
            nameLabel.setBuddy(nameLineEdit)#将账号标签和账号输入框建立伙伴关系

            passwordlabel=QLabel('&Password',self)#建立密码标签
            passwordLineEdit=QLineEdit(self)#建立密码输入框
            passwordlabel.setBuddy(passwordLineEdit)#将密码标签与密码输入框建立伙伴关系

            btnOK=QPushButton('&OK')#确认按钮
            btnCancel=QPushButton('&Cancel')#取消按钮

            mainLayout=QGridLayout(self)
            mainLayout.addWidget(nameLabel,0,0)
            mainLayout.addWidget(nameLineEdit,0,1,1,2)#将账号输入框放在第二行第一列，长占据一行，宽占据两列
            mainLayout.addWidget(passwordlabel,1,0)
            mainLayout.addWidget(passwordLineEdit,1,1,1,2)
            mainLayout.addWidget(btnOK,2,1)
            mainLayout.addWidget(btnCancel,2,2)

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = QlabelBuddy()
        main.show()
        sys.exit(app.exec_())

#9.QLineEdit控件与回显模式
if 'QLineEdit'=='QLineEdit':
    """
    基本功能：输入单行的文本
    回显模式：1.Normal正常模式：输入然后显示
             2.NoEcho不回显：输入但是并不显示
             3.Password密码模式：输入密码时会用***加密覆盖
             4.PasswordEchonWdit:输入后过一会儿就会变成***
    """

    import sys
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import QPalette, QPixmap
    from PyQt5.QtCore import Qt

    class QLineEditEchoMode(QWidget):
        def __init__(self):
            super(QLineEditEchoMode, self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('文本输入框的回显模式')

            formLayout=QFormLayout()#使用表单布局,建立四种输入模式的输入框
            normalLineEdit=QLineEdit()
            noEchoLineEdit=QLineEdit()
            passwordLineEdit=QLineEdit()
            passwordEchoOnLineEdit=QLineEdit()

            formLayout.addRow('Normal',normalLineEdit)#在表单布局中添加'Normal：normalLineEdit'，添加四种输入框
            formLayout.addRow('noEcho',noEchoLineEdit)
            formLayout.addRow('password',passwordLineEdit)
            formLayout.addRow('passwordEcho',passwordEchoOnLineEdit)

            # 设置输入框中的原存提示字符
            normalLineEdit.setPlaceholderText('Normal')
            noEchoLineEdit.setPlaceholderText('NoEcho')
            passwordLineEdit.setPlaceholderText('Password')
            passwordEchoOnLineEdit.setPlaceholderText('PasswordEchoOnEdit')

            # 为四种输入框选择四种不的输入模式
            normalLineEdit.setEchoMode(QLineEdit.Normal)
            noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
            passwordLineEdit.setEchoMode(QLineEdit.Password)
            passwordEchoOnLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

            self.setLayout(formLayout)

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = QLineEditEchoMode()
        main.show()
        sys.exit(app.exec_())

#10.限制QLineEdit控件得输入（校验器）
if '校验器'=='校验器':
    """
    校验器：要求只能输入整数，浮点数或满足一定条件得字符串
    """

    import sys
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator#各种校验器
    from PyQt5.QtCore import QRegExp#校验正则表达式

    class QlineEditValidator(QWidget):
        def __init__(self):
            super(QlineEditValidator, self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('校验器')
            formLayout=QFormLayout()

            intLineEdit=QLineEdit()
            doubleLineEdit=QLineEdit()
            validatorLineEdit=QLineEdit()

            formLayout.addRow('整数类型',intLineEdit)
            formLayout.addRow('浮点类型',doubleLineEdit)
            formLayout.addRow('数字和字母',validatorLineEdit)

            intLineEdit.setPlaceholderText('整型')#设置提示字符
            doubleLineEdit.setPlaceholderText('浮点型')
            validatorLineEdit.setPlaceholderText('字母和数字')

            #整数校验器
            intValidator=QIntValidator(self)
            intValidator.setRange(1,99)#只能输入1——99之间的整数

            #浮点校验器[-360,360],精度：小数点后2位
            doubleValidator=QDoubleValidator(self)
            doubleValidator.setRange(-360,360)#设置范围
            doubleValidator.setNotation(QDoubleValidator.StandardNotation)
            doubleValidator.setDecimals(2)#设置精度，小数点2位

            #字符和数字
            reg=QRegExp('[a-zA-Z0-9]')#匹配数字和字母的正则表达式
            validator=QRegExpValidator(self)
            validator.setRegExp(reg)#通过带入正则表达式制作数字和字母的校验器

            #设置校验器
            intLineEdit.setValidator(intValidator)#将整型校验器设置到第一个输入框中
            doubleLineEdit.setValidator(doubleValidator)
            validatorLineEdit.setValidator(validator)

            self.setLayout(formLayout)

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = QlineEditValidator()
        main.show()
        sys.exit(app.exec_())

#11.使用掩码限制QLineEdit控件的输入
if '掩码'=='掩码':
    from PyQt5.QtWidgets import *
    import sys

    class QLineEditMask(QWidget):
        def __init__(self):
            super(QLineEditMask, self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('用掩码限制输入控件的输入')
            formLayout=QFormLayout()

            ipLineEdit=QLineEdit()
            maclineEdit=QLineEdit()
            dateLineEdit=QLineEdit()
            licenseLineEdit=QLineEdit()

            ipLineEdit.setInputMask('000.000.000.000;_')#限制IP只能输入类似于“192.168.21.45”格式的输入
            maclineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')
            dateLineEdit.setInputMask('0000-00-00')
            licenseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA-;#')

            # 依次将控件添加到表单布局中
            formLayout.addRow('数字掩码',ipLineEdit)
            formLayout.addRow('Mac掩码',maclineEdit)
            formLayout.addRow('日期掩码',dateLineEdit)
            formLayout.addRow('许可证掩码',licenseLineEdit)

            self.setLayout(formLayout)


    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = QLineEditMask()
        main.show()
        sys.exit(app.exec_())

#12.QLineEdit的综合案例
if '综合案例'=='综合案例':
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import Qt
    import sys

    class QLineEditApply(QWidget):
        def __init__(self):
            super(QLineEditApply, self).__init__()
            self.initUI()

        def initUI(self):
            edit1=QLineEdit()
            edit1.setValidator(QIntValidator())#设置校验器，限制输入位整数
            edit1.setMaxLength(4)#限制输入最多四位数，不超过9999
            edit1.setAlignment(Qt.AlignRight)#设置右对齐
            edit1.setFont(QFont('Arial',20))

            edit2=QLineEdit()
            edit2.setValidator(QDoubleValidator(0.99,99.99,2))

            edit3=QLineEdit()
            edit3.setInputMask('99_9999_999999;#')

            edit4=QLineEdit()
            edit4.textChanged.connect(self.text_change)#当输入栏4文本改变时，触发此函数

            edit5=QLineEdit()
            edit5.setEchoMode(QLineEdit.Password)
            edit5.editingFinished.connect(self.enterPress)#当输入完成时，触发此函数

            edit6=QLineEdit('Hello PyQt5')
            edit6.setReadOnly(True)#设置为只读模式

            formLayout=QFormLayout()
            formLayout.addRow('整数校验',edit1)
            formLayout.addRow('浮点校验',edit2)
            formLayout.addRow('Input Mask',edit3)
            formLayout.addRow('文本变化',edit4)
            formLayout.addRow('密码',edit5)
            formLayout.addRow('只读',edit6)

            self.setLayout(formLayout)
            self.setWindowTitle('输入框综合案例')

        def text_change(self,text):
            print('输入的内容'+text)

        def enterPress(self):
            print('已输入值')

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = QLineEditApply()
        main.show()
        sys.exit(app.exec_())

#13.QTextEdit控件:可以输入多行文本
if 'QTextEdit控件'=='QTextEdit控件':
    """
    
    """
    from PyQt5.QtWidgets import *
    import sys

    class QTextEditDemo(QWidget):
        def __init__(self):
            super(QTextEditDemo, self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('QTextEdit控件演示')
            self.resize(300,200)
            self.textEdit=QTextEdit()
            self.buttonText=QPushButton('显示文本')
            self.buttonHTML=QPushButton('显示HTML')
            self.buttonToText = QPushButton('获取文本')
            self.buttonToHTML = QPushButton('获取HTML')

            

            Layout=QVBoxLayout()
            Layout.addWidget(self.textEdit)
            Layout.addWidget(self.buttonText)
            Layout.addWidget(self.buttonHTML)
            Layout.addWidget(self.buttonToText)
            Layout.addWidget(self.buttonToHTML)
            self.setLayout(Layout)

            #绑定信号与槽函数
            self.buttonText.clicked.connect(self.onClick_ButtonText)
            self.buttonHTML.clicked.connect(self.onClick_ButtonHTML)
            self.buttonToText.clicked.connect(self.onClick_ButtonToText)
            self.buttonToHTML.clicked.connect(self.onClick_ButtonToHTML)

        def onClick_ButtonText(self):
            self.textEdit.setPlainText('Hello World,世界你好吗？')#设置文本

        def onClick_ButtonToText(self):
            print(self.textEdit.toPlainText())#获取文本

        def onClick_ButtonHTML(self):
            self.textEdit.setHtml('<font color="blue" size="5">Hello World</font>')#设置HTML

        def onClick_ButtonToHTML(self):
            print(self.textEdit.toHtml())#获取HTML

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = QTextEditDemo()
        main.show()
        sys.exit(app.exec_())

#14.按钮控件QPushButton
if '按钮控件'=='按钮控件':
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    import sys
    from PyQt5.QtGui import *

    class PushButtonDemo(QDialog):
        def __init__(self):
            super(PushButtonDemo, self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('按钮控件使用')
            self.setGeometry(300,300,400,400)
            layout=QVBoxLayout()#设置垂直布局

            self.button1=QPushButton('第一个按钮')
            self.button1.setText('first button')
            self.button1.setCheckable(True)#使按钮出于可选中状态，像开关一样处于某种状态
            self.button1.toggle()#像开关一样处于某种状态

            self.button1.clicked.connect(lambda :self.whichButton(self.button1))#通过lambda表达式调用按钮button1
            self.button1.clicked.connect(self.buttonState)
            layout.addWidget(self.button1)
            self.setLayout(layout)

            #在文本面前显示图像
            self.button2=QPushButton('图像按钮')#设置按钮名称
            self.button2.setIcon(QIcon(QPixmap(r'E:\图片\103840-15009503208823.jpg')))#使得按钮2显示图像
            self.button2.clicked.connect(lambda:self.whichButton(self.button2))
            layout.addWidget(self.button2)

            #设置按钮3不可用
            self.button3=QPushButton('不可用按钮')
            self.button3.setEnabled(False)
            layout.addWidget(self.button3)

            self.button4=QPushButton('&MyButton')
            self.button4.setDefault(True)#默认按钮
            self.button4.clicked.connect(lambda:self.whichButton(self.button4))
            layout.addWidget(self.button4)

        def buttonState(self):
            if self.button1.isChecked():#判断按钮1被选中
                print('按钮1被选中')
            else:
                print('按钮1未被选中')

        def whichButton(self,btn):
            print('被单击的按钮是<'+btn.text()+'>')

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = PushButtonDemo()
        main.show()
        sys.exit(app.exec_())

#15.单选按钮QRadioButton:在多个按钮中只能选中一个按钮
if '单选按钮'=='单选按钮':
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    import sys
    from PyQt5.QtGui import *

    class RadioButtonDemo(QWidget):
        def __init__(self):
            super(RadioButtonDemo, self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('单选按钮')
            layout=QHBoxLayout()
            self.button1=QRadioButton('单选按钮1')
            self.button1.setChecked(True)
            self.button1.toggled.connect(self.buttonState)#按钮的切换状态将触发此函数
            layout.addWidget(self.button1)

            self.button2=QRadioButton('单选按钮2')
            self.button2.toggled.connect(self.buttonState)
            layout.addWidget(self.button2)

            self.setLayout(layout)

        #判断按钮的被选中的状态
        def buttonState(self):
            radioButton=self.sender()#获得所有按钮信息
            if radioButton.text() == '单选按钮1':
                if radioButton.isChecked()==True:#判断按钮是否被选中
                    print("<"+radioButton.text()+'>被选中')
                else:
                    print('<'+radioButton.text()+'>被取消选中状态')

            if radioButton.text()=='单选按钮2':
                if radioButton.isChecked()== True:
                    print("<" + radioButton.text() + '>被选中')
                else:
                    print('<' + radioButton.text() + '>被取消选中状态')

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = RadioButtonDemo()
        main.show()
        sys.exit(app.exec_())

#16.复选框控件QCheckBox:同时选中多个控件
if '复选框'=='复选框':
    """
    三种状态：未选中0，半选中1，选中2
    """

    import sys
    from PyQt5.QtWidgets import  *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import Qt

    class CheckBoxDemo(QWidget):
        def __init__(self):
            super(CheckBoxDemo, self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('复选框控件')

            layout=QHBoxLayout()
            self.checkBox1=QCheckBox("复选框控件1")
            self.checkBox1.setChecked(False)#默认不选中
            self.checkBox1.stateChanged.connect(lambda :self.checkboxState(self.checkBox1))#当按钮一的被选中状态改变时，触发此函数
            layout.addWidget(self.checkBox1)

            self.checkBox2 = QCheckBox("复选框控件2")
            self.checkBox2.setChecked(True)#默认选中
            self.checkBox2.stateChanged.connect(lambda: self.checkboxState(self.checkBox2))  # 当按钮2的被选中状态改变时，触发此函数
            layout.addWidget(self.checkBox2)

            self.checkBox3 = QCheckBox("复选框控件3")
            self.checkBox3.setChecked(True)
            self.checkBox3.stateChanged.connect(lambda: self.checkboxState(self.checkBox3))  # 当按钮3的被选中状态改变时，触发此函数
            self.checkBox3.setTristate(True)#按钮3处于半选中状态
            self.checkBox3.setChecked(Qt.PartiallyChecked)##按钮3处于半选中状态
            layout.addWidget(self.checkBox3)

            self.setLayout(layout)


        def checkboxState(self,cb):
            check1Status=self.checkBox1.text()+',isChecked'+str(self.checkBox1.isChecked())+',checkState='+str(self.checkBox1.checkState())+'\n'
            check2Status = self.checkBox2.text() + ',isChecked' + str(self.checkBox2.isChecked())+',checkState='+str(self.checkBox2.checkState())+'\n'
            check3Status = self.checkBox3.text() + ',isChecked' + str(self.checkBox3.isChecked())+',checkState='+str(self.checkBox3.checkState())+'\n'
            print(check1Status+check2Status+check3Status)

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = CheckBoxDemo()
        main.show()
        sys.exit(app.exec_())

#17.下拉列表控件
if '下拉列表'=='下拉列表':
    import sys
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import Qt

    class QComboxDemo(QWidget):
        def __init__(self):
            super(QComboxDemo, self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('下拉列表控件')
            self.resize(300,300)

            layout=QVBoxLayout()
            self.label=QLabel('请选择编程语言')
            self.cb=QComboBox()
            self.cb.addItem('C++')#添加单个项目
            self.cb.addItem('Python')
            self.cb.addItems(['Java','C#','Rubby'])#添加多个项目

            self.cb.currentIndexChanged.connect(self.selectionChange)#当选择的项目改变时，触发函数

            layout.addWidget(self.label)
            layout.addWidget(self.cb)
            self.setLayout(layout)

        def selectionChange(self):
            self.label.setText(self.cb.currentText())#显示当前选中的项目的内容
            self.label.adjustSize()

            for count in range(self.cb.count()):
                print('item'+str(count)+'='+self.cb.itemText(count))#显示当前选中项目的序号和内容
                print('current inddex',count,'selection changed',self.cb.currentText())

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = QComboxDemo()
        main.show()
        sys.exit(app.exec_())

#18.滑块控件（QSlider）
if '滑块'=='滑块':
    import sys
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import Qt

    class SliderDemo(QWidget):
        def __init__(self):
            super(SliderDemo, self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('滑块控件展示')
            self.resize(300,100)

            layout=QVBoxLayout()
            self.label=QLabel('你好')
            self.label.setAlignment(Qt.AlignCenter)
            layout.addWidget(self.label)

            self.slider=QSlider(Qt.Horizontal)#创建横向滑块
            self.slider.setMaximum(48)#设置滑块最大值
            self.slider.setMinimum(12)#设置滑块最小值
            self.slider.setSingleStep(3)#设置滑块步长
            self.slider.setValue(18)#设置默认值
            self.slider.setTickInterval(QSlider.TicksBelow)#设置刻度的位置，刻度在下方
            self.slider.setTickInterval(6)#设置刻度间隔

            layout.addWidget(self.slider)
            self.slider.valueChanged.connect(self.valueChange)#滑块数值改变，触发此函数
            self.setLayout(layout)

        def valueChange(self):#显示滑块改变的数值
            print('当前值：%s'%self.slider.value())#展示当前滑块数值
            size=self.slider.value()#获得滑块的数值
            self.label.setFont(QFont('Arial',size))#为标签设置字体

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = SliderDemo()
        main.show()
        sys.exit(app.exec_())

#19.计数器控件QSpinBox
if '计数器'=='计数器':
    import sys
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import Qt

    class SpinBoxDemo(QWidget):
        def __init__(self):
            super(SpinBoxDemo,self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('计数器演示')
            self.resize(300,100)

            layout=QVBoxLayout()
            self.label=QLabel('当前值')
            self.label.setAlignment(Qt.AlignCenter)#设置居中

            layout.addWidget(self.label)

            self.sb=QSpinBox()#创建计数器
            self.sb.valueChanged.connect(self.valueChange)#计数器数值改变触发此函数
            self.sb.setRange(0,1000)
            layout.addWidget(self.sb)
            self.setLayout(layout)

        def valueChange(self):#显示改变的值
            self.label.setText('当前值：'+str(self.sb.value()))

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = SpinBoxDemo()
        main.show()
        sys.exit(app.exec_())

#20.对话框QDialog:用于显示普通的基类对话框
if '对话框'=='对话框':
    """
    QMessageBox消息对话框
    QColorDialog颜色对话框
    QFileDialog文件选择对话框
    QFontDialog设置字体对话框
    QInputDialog输入对话框
    
    QMainWindow
    QWidget
    QDialog
    """
    import sys
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import Qt

    class DialogDemo(QMainWindow):
        def __init__(self):
            super(DialogDemo, self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('QDialog演示')
            self.resize(300,200)

            self.button=QPushButton(self)
            self.button.setText('弹出对话框')
            self.button.move(50,50)
            self.button.clicked.connect(self.showDialog)#点击按钮将触发弹出对话框函数
            self.label=QLabel()


        def showDialog(self):
            dialog=QDialog()#创建对话框
            button=QPushButton('确定',dialog)
            button.clicked.connect(dialog.close)#点击按钮将关闭对话框
            button.move(50,50)#移动按钮
            line_edit=QLineEdit()

            layout2=QVBoxLayout()
            layout2.addWidget(button)
            layout2.addWidget(line_edit)
            dialog.setLayout(layout2)
            dialog.setWindowTitle('对话框')
            #dialog.setWindowModality(Qt.ApplicationModal)#将对话框以模式显示使用，当对话框弹出，其他功能都不可使用
            dialog.exec_()#对话框持续显示

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = DialogDemo()
        main.show()
        sys.exit(app.exec_())

#21.消息对话框QMessageBox:
if '消息对话框'=='消息对话框':
    """
    1.关于对话框
    2.错误对话框
    3.警告对话框
    4.提问对话框
    5.消息对话框
    
    有两点差异：显示的图标可能不一样，显示的按钮不一样
    """
    import sys
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import Qt

    class MessageBoxDemo(QWidget):
        def __init__(self):
            super(MessageBoxDemo,self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('QMessageBox案例')
            self.resize(300,400)

            layout=QVBoxLayout()
            self.button1=QPushButton()
            self.button1.setText('显示关于对话框')
            self.button1.clicked.connect(self.showDialog)#点击按钮1将触发显示对话框的函数

            self.button2=QPushButton()
            self.button2.setText('显示消息对话框')
            self.button2.clicked.connect(self.showDialog)#点击按钮2将触发显示消息对话框的函数

            self.button3 = QPushButton()
            self.button3.setText('显示警告对话框')
            self.button3.clicked.connect(self.showDialog)  # 点击按钮3将触发显示警告对话框的函数

            self.button4 = QPushButton()
            self.button4.setText('显示错误对话框')
            self.button4.clicked.connect(self.showDialog)  # 点击按钮4将触发显示错误对话框的函数

            self.button5 = QPushButton()
            self.button5.setText('显示提问对话框')
            self.button5.clicked.connect(self.showDialog)  # 点击按钮5将触发显示提问对话框的函数，比如提示是否保存文件

            layout.addWidget(self.button1)
            layout.addWidget(self.button2)
            layout.addWidget(self.button3)
            layout.addWidget(self.button4)
            layout.addWidget(self.button5)
            self.setLayout(layout)

        def showDialog(self):
            text=self.sender().text()#获得点击的按钮上的文字
            if text=='显示关于对话框':
                QMessageBox.about(self,'关于','这是一个关于对话框')#弹出的对话框，名字为“关于”，内容为“这是一个关于对话框”
            elif text=='显示消息对话框':
                reply=QMessageBox.information(self,'消息','这是一个消息对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
                #创建消息对话框，并用reply捕获点击按钮得到的消息，用QMessageBox.Yes|QMessageBox.No在两边放置Yes和No按钮
                print(reply==QMessageBox.Yes)#如果点击Yes将返回True
            elif text=='显示警告对话框':
                QMessageBox.warning(self,'警告','这是一个警告对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            elif text=='显示错误对话框':
                QMessageBox.critical(self,'错误','这是一个错误对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            elif text=='显示提问对话框':
                QMessageBox.question(self,'提问','这是一个提问对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = MessageBoxDemo()
        main.show()
        sys.exit(app.exec_())

#22.输入对话框QInputDialog
if '消息对话框'=='消息对话框':
    """
    QInputDialog.getItem
    QInputDialog.getText
    QInputDialog.getInt
    """

    import sys
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import Qt

    class InputDialogDemo(QWidget):
        def __init__(self):
            super(InputDialogDemo, self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('输入对话框')
            layout=QFormLayout()
            self.setLayout(layout)

            self.button1=QPushButton('获取列表中的选项')
            self.button1.clicked.connect(self.getItem)
            self.lineEdit1=QLineEdit()
            layout.addRow(self.button1,self.lineEdit1)

            self.button2 = QPushButton('获取字符串')
            self.button2.clicked.connect(self.getText)
            self.lineEdit2 = QLineEdit()
            layout.addRow(self.button2, self.lineEdit2)

            self.button3 = QPushButton('获取整数')
            self.button3.clicked.connect(self.getInt)
            self.lineEdit3 = QLineEdit()
            layout.addRow(self.button3, self.lineEdit3)

        def getItem(self):
            items=('C','C++','Ruby','Python','Java')
            item,ok=QInputDialog.getItem(self,'请选择编程语言','语言列表',items)#获得输入的列表等各种对象
            if ok and item:#如果item和ok有值
                self.lineEdit1.setText(item)

        def getText(self):
            Text,ok=QInputDialog.getText(self,'文本输入框','输入姓名')#获得文本型输入框
            if ok and Text:#如果Text和ok有值
                self.lineEdit2.setText(Text)#显示输入的文本

        def getInt(self):
            num,ok=QInputDialog.getInt(self,'整数输入框','输入数字')#获得输入的数字
            if ok and num:#如果num和ok有值
                self.lineEdit3.setText(str(num))


    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = InputDialogDemo()
        main.show()
        sys.exit(app.exec_())

#23.字体对话框QFontDialog
if '字体对话框'=='字体对话框':
    import sys
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import Qt

    class FontDialogDemo(QWidget):
        def __init__(self):
            super(FontDialogDemo, self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('字体对话框')
            layout=QVBoxLayout()
            self.setLayout(layout)

            self.fontButton=QPushButton('选择字体')
            self.fontButton.clicked.connect(self.getFont)
            layout.addWidget(self.fontButton)

            self.fontLabel=QLabel()
            self.fontLabel.setText('Hello')
            layout.addWidget(self.fontLabel)

        def getFont(self):#改变字体形式的函数
            font,ok=QFontDialog.getFont()
            if ok:
                self.fontLabel.setFont(font)#将选好的字体格式应用于显示标签
                print(str(ok))

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = FontDialogDemo()
        main.show()
        sys.exit(app.exec_())

#23.颜色对话框QColorDialog
if '颜色对话框'=='颜色对话框':
    import sys
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import Qt

    class ColorDialogDemo(QWidget):
        def __init__(self):
            super(ColorDialogDemo, self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('颜色对话框')
            layout=QVBoxLayout()
            self.setLayout(layout)

            self.colorButton=QPushButton('选择颜色')
            self.colorButton.clicked.connect(self.getColor)
            layout.addWidget(self.colorButton)

            self.colorButton1 = QPushButton('设置背景颜色')
            self.colorButton1.clicked.connect(self.getBGColor)
            layout.addWidget(self.colorButton1)

            self.colorLabel=QLabel()
            self.colorLabel.setText('Hello')
            layout.addWidget(self.colorLabel)

        def getColor(self):#改变字体形式的函数
            color=QColorDialog.getColor()
            p=QPalette()#创建调色板
            p.setColor(QPalette.WindowText,color)#将字体颜色加入调色板
            self.colorLabel.setPalette(p)#利用调色板为标签文字上色

        def getBGColor(self):#改变背景颜色的函数
            color=QColorDialog.getColor()
            p=QPalette()#创建调色板
            p.setColor(QPalette.Window,color)#QPalette.Window将背景颜色加入调色板
            self.colorLabel.setPalette(p)#利用调色板为背景颜色上色
            self.colorLabel.setAutoFillBackground(True)

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = ColorDialogDemo()
        main.show()
        sys.exit(app.exec_())

#24.文件对话框QFileDialog：打开文件和保存文件
if '文件对话框'=='文件对话框':
    import sys
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import Qt

    class FileDialogDemo(QWidget):
        def __init__(self):
            super(FileDialogDemo, self).__init__()
            self.initUI()

        def initUI(self):
            layout=QVBoxLayout()
            self.button1=QPushButton('加载图片')
            self.button1.clicked.connect(self.loadImage)#点击按钮触发加载图片的函数
            layout.addWidget(self.button1)

            self.labelImage=QLabel()#用于显示图片的标签
            layout.addWidget(self.labelImage)

            self.button2=QPushButton('加载文本文件')
            self.button2.clicked.connect(self.loadText)#点击图片触发加载文本文件的函数
            layout.addWidget(self.button2)

            self.contents=QTextEdit()#用文本输入板作为文本显示板
            layout.addWidget(self.contents)

            self.setLayout(layout)
            self.setWindowTitle('文件对话框演示')

        def loadImage(self):
            frame,_=QFileDialog.getOpenFileName(self,'打开文件','.','图像文件(*.jpg *.png)')#打开文件，'打开文件'为标题，'.'为默认打开的目录，'图像文件(*.jpg*.png)'表示可以打开这两种格式图片,使用frame获得图片内容
            #frame代表所获得的文件目录
            self.labelImage.setPixmap(QPixmap(frame))#在标签上打开图片

        def loadText(self):
            dialog= QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)#设定可以选择多个文件
            dialog.setFilter(QDir.Files)

            if dialog.exec():#如果对话框打开状态
                filenames=dialog.selectedFiles()#获得对话框选择的文件名
                f=open(filenames[0],mode='r',encoding='utf-8')#打开指定文件
                with f:
                    data=f.read()
                    self.contents.setText(data)


    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = FileDialogDemo()
        main.show()
        sys.exit(app.exec_())

#25.绘图Api:绘制文本
if '绘制文本'=='绘制文本':
    """
    1.绘制文本
    2.各种图形（直线，点，椭圆，弧，扇形，多边形）
    3.图像
    
    QPainter#必须使用的绘制图像类
    painter=QPainter()#首先需要实例化类
    painter.begin()
    painter.drawText(...)
    painer.end()
    必须在painterEvent事件方法中绘制各种元素
    """
    import sys
    from PyQt5.QtWidgets import  QApplication,QWidget
    from PyQt5.QtGui import QPainter,QColor,QFont
    from PyQt5.QtCore import Qt

    class DrawText(QWidget):
        def __init__(self):
            super(DrawText, self).__init__()
            self.setWindowTitle('在窗口上绘制文本')
            self.resize(300,200)
            self.text='Python从菜鸟'

        def paintEvent(self, event):
            painter=QPainter(self)#实例化事件
            painter.begin(self)#事件开始

            painter.setPen(QColor(150,43,5))#设置画笔的颜色为红，绿，蓝
            painter.setFont(QFont('SimSun',25))#设置字体
            painter.drawText(event.rect(),Qt.AlignCenter,self.text)#event.rect()设置绘图区域为整个窗口，居中，绘制的文本为self.text

            painter.end()#事件结束

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = DrawText()
        main.show()
        sys.exit(app.exec_())

#26.用像素点绘制正弦曲线
if '绘制正弦曲线'=='绘制正弦曲线':
    """
    drawPoints(x,y)#使用此方法绘制曲线
    """
    import sys,math
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    class DrawPoints(QWidget):
        def __init__(self):
            super(DrawPoints, self).__init__()
            self.resize(300,300)
            self.setWindowTitle('绘制正弦曲线')

        def paintEvent(self, event):
            painter=QPainter()
            painter.begin(self)
            painter.setPen(Qt.blue)#设置画笔为蓝色
            size=self.size()#获得窗口尺寸

            for i in range(1000):#采用循环方式逐点绘制图像
                x=100*(-1+2.0*i/1000)+size.width()/2.0#横轴坐标,size.width()/2.0表示窗口宽一半，保证从窗口中心开始绘制
                y=-50*math.sin((x-size.width()/2.0)*math.pi/50)+size.height()/2.0#纵轴坐标，从-2pi到2pi
                painter.drawPoint(x,y)#绘制其中一个点

            painter.end()

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = DrawPoints()
        main.show()
        sys.exit(app.exec_())































































