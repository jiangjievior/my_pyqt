# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(604, 707)
        Form.setMouseTracking(False)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(60, 20, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.fontComboBox = QtWidgets.QFontComboBox(Form)
        self.fontComboBox.setGeometry(QtCore.QRect(60, 60, 91, 22))
        self.fontComboBox.setObjectName("fontComboBox")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(60, 100, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(60, 140, 104, 51))
        self.textEdit.setObjectName("textEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 210, 104, 87))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(60, 320, 111, 22))
        self.spinBox.setObjectName("spinBox")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(60, 360, 111, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(60, 410, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(60, 450, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dial = QtWidgets.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(60, 490, 50, 64))
        self.dial.setObjectName("dial")
        self.horizontalScrollBar = QtWidgets.QScrollBar(Form)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(40, 580, 160, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
