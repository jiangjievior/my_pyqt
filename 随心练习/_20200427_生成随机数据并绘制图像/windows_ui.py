# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(407, 317)
        Form.setStyleSheet("background-color: rgb(169, 230, 255);")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(95, 141, 91, 18))
        self.label_5.setObjectName("label_5")
        self.lineEdit_file_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_file_name.setGeometry(QtCore.QRect(206, 141, 101, 20))
        self.lineEdit_file_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_file_name.setObjectName("lineEdit_file_name")
        self.lineEdit_path = QtWidgets.QLineEdit(Form)
        self.lineEdit_path.setGeometry(QtCore.QRect(206, 114, 101, 20))
        self.lineEdit_path.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.lineEdit_specol = QtWidgets.QLineEdit(Form)
        self.lineEdit_specol.setGeometry(QtCore.QRect(206, 87, 101, 20))
        self.lineEdit_specol.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_specol.setObjectName("lineEdit_specol")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 30, 51, 21))
        self.label.setStyleSheet("font: 12pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(95, 114, 91, 18))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(105, 87, 71, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_cols = QtWidgets.QLineEdit(Form)
        self.lineEdit_cols.setGeometry(QtCore.QRect(206, 60, 101, 20))
        self.lineEdit_cols.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_cols.setObjectName("lineEdit_cols")
        self.lineEdit_rows = QtWidgets.QLineEdit(Form)
        self.lineEdit_rows.setGeometry(QtCore.QRect(206, 32, 101, 20))
        self.lineEdit_rows.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_rows.setObjectName("lineEdit_rows")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 60, 51, 18))
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(102, 204, 93, 28))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(202, 204, 93, 28))
        self.pushButton_2.setStyleSheet("background-color: rgb(75, 255, 75);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(302, 204, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(179, 179, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(2, 204, 93, 28))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        self.pushButton_4.clicked.connect(Form.creat_random_data)
        self.pushButton_3.clicked.connect(Form.plot_plt)
        self.pushButton_2.clicked.connect(Form.scatter_plt)
        self.pushButton.clicked.connect(Form.to_excel)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">文件名称</span></p></body></html>"))
        self.lineEdit_file_name.setText(_translate("Form", "随机数据表"))
        self.lineEdit_specol.setText(_translate("Form", "2"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">  行数  </span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">保存路径</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">指定列</span></p></body></html>"))
        self.lineEdit_cols.setText(_translate("Form", "8"))
        self.lineEdit_rows.setText(_translate("Form", "8"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">列数</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "折线图"))
        self.pushButton_2.setText(_translate("Form", "散点图"))
        self.pushButton.setText(_translate("Form", "保存"))
        self.pushButton_4.setText(_translate("Form", "数据生成"))

#import 454_rc
