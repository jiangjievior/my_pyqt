# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 781, 511))
        self.tabWidget.setObjectName("tabWidget")
        self.SingleTab = QtWidgets.QWidget()
        self.SingleTab.setObjectName("SingleTab")
        self.widget = QtWidgets.QWidget(self.SingleTab)
        self.widget.setGeometry(QtCore.QRect(120, 20, 551, 411))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_picture = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_picture.setObjectName("lineEdit_picture")
        self.gridLayout.addWidget(self.lineEdit_picture, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_txt = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_txt.setObjectName("lineEdit_txt")
        self.gridLayout.addWidget(self.lineEdit_txt, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_select_txt = QtWidgets.QPushButton(self.widget)
        self.pushButton_select_txt.setObjectName("pushButton_select_txt")
        self.gridLayout.addWidget(self.pushButton_select_txt, 0, 1, 1, 1)
        self.pushButton_select_picture = QtWidgets.QPushButton(self.widget)
        self.pushButton_select_picture.setObjectName("pushButton_select_picture")
        self.gridLayout.addWidget(self.pushButton_select_picture, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_creat_txt = QtWidgets.QPushButton(self.widget)
        self.pushButton_creat_txt.setObjectName("pushButton_creat_txt")
        self.horizontalLayout.addWidget(self.pushButton_creat_txt)
        self.pushButton_creat_picture = QtWidgets.QPushButton(self.widget)
        self.pushButton_creat_picture.setObjectName("pushButton_creat_picture")
        self.horizontalLayout.addWidget(self.pushButton_creat_picture)
        self.pushButton_show_picture = QtWidgets.QPushButton(self.widget)
        self.pushButton_show_picture.setObjectName("pushButton_show_picture")
        self.horizontalLayout.addWidget(self.pushButton_show_picture)
        self.pushButton_show_txt = QtWidgets.QPushButton(self.widget)
        self.pushButton_show_txt.setObjectName("pushButton_show_txt")
        self.horizontalLayout.addWidget(self.pushButton_show_txt)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.screen_single = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screen_single.sizePolicy().hasHeightForWidth())
        self.screen_single.setSizePolicy(sizePolicy)
        self.screen_single.setText("")
        self.screen_single.setObjectName("screen_single")
        self.verticalLayout.addWidget(self.screen_single)
        self.tabWidget.addTab(self.SingleTab, "")
        self.MultipleTab = QtWidgets.QWidget()
        self.MultipleTab.setObjectName("MultipleTab")
        self.tabWidget.addTab(self.MultipleTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "图片文件路径"))
        self.label.setText(_translate("MainWindow", "TxT文件路径"))
        self.pushButton_select_txt.setText(_translate("MainWindow", "选择文件"))
        self.pushButton_select_picture.setText(_translate("MainWindow", "选择图片"))
        self.pushButton_creat_txt.setText(_translate("MainWindow", "生成txt"))
        self.pushButton_creat_picture.setText(_translate("MainWindow", "生成图片"))
        self.pushButton_show_picture.setText(_translate("MainWindow", "显示图片"))
        self.pushButton_show_txt.setText(_translate("MainWindow", "显示TxT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SingleTab), _translate("MainWindow", "单图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MultipleTab), _translate("MainWindow", "多图"))

