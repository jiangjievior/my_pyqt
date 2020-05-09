# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Spacer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(726, 487)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 40, 72, 15))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(42, 90, 498, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(130, 180, 117, 172))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.widget1)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        spacerItem1 = QtWidgets.QSpacerItem(30, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout.addWidget(self.radioButton_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "分割线"))
        self.pushButton.setText(_translate("Form", "PushButton1"))
        self.pushButton_2.setText(_translate("Form", "PushButton2"))
        self.pushButton_3.setText(_translate("Form", "PushButton3"))
        self.pushButton_4.setText(_translate("Form", "PushButton4"))
        self.radioButton.setText(_translate("Form", "RadioButton"))
        self.radioButton_3.setText(_translate("Form", "RadioButton"))
        self.radioButton_2.setText(_translate("Form", "RadioButton"))
        self.radioButton_4.setText(_translate("Form", "RadioButton"))
        self.radioButton_5.setText(_translate("Form", "RadioButton"))

