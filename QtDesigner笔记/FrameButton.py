# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrameButton.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1078, 759)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(100, 130, 181, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(40, 40, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 30, 441, 16))
        self.label.setObjectName("label")
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(320, 180, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(450, 180, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(580, 180, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(Form)
        self.webEngineView.setGeometry(QtCore.QRect(100, 460, 871, 201))
        self.webEngineView.setUrl(QtCore.QUrl("https://www.baidu.com/"))
        self.webEngineView.setObjectName("webEngineView")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 410, 261, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.label.setText(_translate("Form", "绝对布局：在窗口中添加一个窗口，放入的控件大小可以任意调控"))
        self.label_2.setText(_translate("Form", "通过改变url输入网址，打开指定网页"))

from PyQt5 import QtWebEngineWidgets
