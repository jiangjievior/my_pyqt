import sys#导入系统模块
from PyQt5.QtWidgets import  QApplication,QMainWindow
import HorizontalButton
import VerticalButton,FrameButton
import GridButton,HVButton,GridButton2,FormButton,ContainerButton,Spacer


if __name__=='__main__':#运行水平布局
    app=QApplication(sys.argv)#
    mainWindow=QMainWindow()#创建主窗口基类
    ui=HorizontalButton.Ui_Form()#创建显示窗口实例化对象
    ui.setupUi(mainWindow)#将主窗口基类传入显示窗口实例化对象
    mainWindow.show()#显示主窗口
    sys.exit(app.exec_())#通过界面监听退出程序
    
if __name__=='__main__':#运行垂直布局
    app=QApplication(sys.argv)#
    mainWindow=QMainWindow()#创建主窗口基类
    ui=VerticalButton.Ui_Form()#创建显示窗口实例化对象
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

if __name__=='__main__':#运行栅格布局
    app=QApplication(sys.argv)#
    mainWindow=QMainWindow()#创建主窗口基类
    ui=GridButton.Ui_Form()#创建显示窗口实例化对象
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

if __name__=='__main__':#运行栅格布局2:计算器页面
    app=QApplication(sys.argv)#
    mainWindow=QMainWindow()#创建主窗口基类
    ui=GridButton2.Ui_Form()#创建显示窗口实例化对象
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

if __name__=='__main__':#运行复合布局
    app=QApplication(sys.argv)#
    mainWindow=QMainWindow()#创建主窗口基类
    ui=HVButton.Ui_Form()#创建显示窗口实例化对象
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

if __name__=='__main__':#运行表单布局
    app=QApplication(sys.argv)#
    mainWindow=QMainWindow()#创建主窗口基类
    ui=FormButton.Ui_Form()#创建显示窗口实例化对象
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

if __name__=='__main__':#运行容器布局
    app=QApplication(sys.argv)#
    mainWindow=QMainWindow()#创建主窗口基类
    ui=ContainerButton.Ui_Form()#创建显示窗口实例化对象
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

if __name__=='__main__':#运行绝对布局
    app=QApplication(sys.argv)#
    mainWindow=QMainWindow()#创建主窗口基类
    ui=FrameButton.Ui_Form()#创建显示窗口实例化对象
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

if __name__=='__main__':#运行分割线
    app=QApplication(sys.argv)#
    mainWindow=QMainWindow()#创建主窗口基类
    ui=Spacer.Ui_Form()#创建显示窗口实例化对象
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

if __name__=='__main__':#18.控件最大尺寸和最小尺寸
    import sys  # 导入系统模块
    from PyQt5.QtWidgets import QApplication, QMainWindow
    import _18_MaxMin

    app=QApplication(sys.argv)#
    mainWindow=QMainWindow()#创建主窗口基类
    ui=_18_MaxMin.Ui_Form()#创建显示窗口实例化对象
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

if __name__=='__main__':#19.尺寸策略
    import sys  # 导入系统模块
    from PyQt5.QtWidgets import QApplication, QMainWindow
    import _19_sizePolicy

    app=QApplication(sys.argv)#
    mainWindow=QMainWindow()#创建主窗口基类
    ui=_19_sizePolicy.Ui_Form()#创建显示窗口实例化对象
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__=='__main__':#20.设置模块伙伴关系，点击快捷键相连接
    import sys  # 导入系统模块
    from PyQt5.QtWidgets import QApplication, QMainWindow
    import _20_connection

    app=QApplication(sys.argv)#
    mainWindow=QMainWindow()#创建主窗口基类
    ui=_20_connection.Ui_Form()#创建显示窗口实例化对象
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__=='__main__':#21.修改输入栏之间的Tab切换顺序
    import sys  # 导入系统模块
    from PyQt5.QtWidgets import QApplication, QMainWindow
    import _21_changeTab

    app=QApplication(sys.argv)#
    mainWindow=QMainWindow()#创建主窗口基类
    ui=_21_changeTab.Ui_Form()#创建显示窗口实例化对象
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

if __name__=='__main__':#22.信号与槽函数的使用
    import sys  # 导入系统模块
    from PyQt5.QtWidgets import QApplication, QMainWindow
    import _22_Slot

    app=QApplication(sys.argv)#
    mainWindow=QMainWindow()#创建主窗口基类
    ui=_22_Slot.Ui_Form()#创建显示窗口实例化对象
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

if __name__=='__main__':#23.添加菜单栏和工具栏
    import sys  # 导入系统模块
    from PyQt5.QtWidgets import QApplication, QMainWindow
    import _23_Menu

    app=QApplication(sys.argv)#
    mainWindow=QMainWindow()#创建主窗口基类
    ui=_23_Menu.Ui_MainWindow()#创建显示窗口实例化对象
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())









