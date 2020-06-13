# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bmicalc.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(620, 411)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 60, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.weightEdit = QtWidgets.QLineEdit(Form)
        self.weightEdit.setGeometry(QtCore.QRect(190, 71, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.weightEdit.setFont(font)
        self.weightEdit.setObjectName("weightEdit")
        self.heightEdit = QtWidgets.QLineEdit(Form)
        self.heightEdit.setGeometry(QtCore.QRect(190, 160, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.heightEdit.setFont(font)
        self.heightEdit.setObjectName("heightEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 340, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.bmiButton = QtWidgets.QPushButton(Form)
        self.bmiButton.setGeometry(QtCore.QRect(200, 320, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bmiButton.setFont(font)
        self.bmiButton.setObjectName("bmiButton")
        self.bmiCalcButton = QtWidgets.QPushButton(Form)
        self.bmiCalcButton.setGeometry(QtCore.QRect(200, 230, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bmiCalcButton.setFont(font)
        self.bmiCalcButton.setObjectName("bmiCalcButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BMI Calculator"))
        self.label.setText(_translate("Form", "Weight"))
        self.label_2.setText(_translate("Form", "Height"))
        self.label_3.setText(_translate("Form", "BMI"))
        self.bmiButton.setText(_translate("Form", "BMI"))
        self.bmiCalcButton.setText(_translate("Form", "Calculate"))
