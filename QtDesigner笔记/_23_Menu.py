# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_23_Menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 434)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 30, 371, 61))
        self.label.setStyleSheet("font: 18pt \"Agency FB\";\n"
"color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 271, 131))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1023, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuNew = QtWidgets.QMenu(self.menuBar)
        self.menuNew.setObjectName("menuNew")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_3.setObjectName("toolBar_3")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.menuNew.addSeparator()
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionclose)
        self.menuNew.addAction(self.actionsave)
        self.menuNew.addAction(self.actionopen)
        self.menu.addSeparator()
        self.menuBar.addAction(self.menuNew.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.actionclose)
        self.toolBar.addAction(self.actionsave)
        self.toolBar.addAction(self.actionopen)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "为窗口添加菜单栏和状态栏"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00aa00;\">创建的mainwindow页面默认已经添加了菜单栏和状态栏，通过点击“移除菜单栏”将删除菜单栏，通过右击添加菜单栏，并继续点击添加菜单内容</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00aa00;\">通过“动作编辑器”可以查看菜单栏具体功能，并将功能拖到工具栏</span></p></body></html>"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menu.setTitle(_translate("MainWindow", "视图"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.actionclose.setText(_translate("MainWindow", "close"))
        self.actionclose.setToolTip(_translate("MainWindow", "关闭"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionopen.setText(_translate("MainWindow", "open"))

