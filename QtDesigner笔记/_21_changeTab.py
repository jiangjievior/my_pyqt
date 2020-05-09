# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_21_changeTab.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 427)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 250, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(90, 70, 70, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(90, 110, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(90, 160, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(90, 210, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 20, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 320, 341, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.doubleSpinBox, self.lineEdit)
        Form.setTabOrder(self.lineEdit, self.dateEdit)
        Form.setTabOrder(self.dateEdit, self.timeEdit)
        Form.setTabOrder(self.timeEdit, self.dateTimeEdit)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "修改TAB键顺序"))
        self.label_2.setText(_translate("Form", "通过“Edit-编辑Tab顺序”，双击数字改变顺序"))

