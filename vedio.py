# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vedio.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_vedio(object):
    def setupUi(self, vedio):
        vedio.setObjectName("vedio")
        vedio.resize(400, 300)
        self.widget = QtWidgets.QWidget(vedio)
        self.widget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(40, 40, 311, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 150, 311, 91))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(vedio)
        QtCore.QMetaObject.connectSlotsByName(vedio)

    def retranslateUi(self, vedio):
        _translate = QtCore.QCoreApplication.translate
        vedio.setWindowTitle(_translate("vedio", "Dialog"))
        self.pushButton.setText(_translate("vedio", "开始录屏"))
        self.pushButton_2.setText(_translate("vedio", "结束录屏"))

