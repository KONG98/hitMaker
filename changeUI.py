# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changeUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_change(object):
    def setupUi(self, change):
        change.setObjectName("change")
        change.resize(800, 500)
        self.widget = QtWidgets.QWidget(change)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.widget.setObjectName("widget")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 781, 201))
        self.listWidget.setObjectName("listWidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 220, 781, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setGeometry(QtCore.QRect(0, 390, 801, 41))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.add = QtWidgets.QPushButton(self.widget)
        self.add.setGeometry(QtCore.QRect(30, 440, 111, 41))
        self.add.setObjectName("add")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(200, 440, 141, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.ok = QtWidgets.QPushButton(self.widget)
        self.ok.setGeometry(QtCore.QRect(640, 440, 111, 41))
        self.ok.setObjectName("ok")

        self.retranslateUi(change)
        QtCore.QMetaObject.connectSlotsByName(change)

    def retranslateUi(self, change):
        _translate = QtCore.QCoreApplication.translate
        change.setWindowTitle(_translate("change", "Dialog"))
        self.textBrowser.setHtml(_translate("change",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LOG:</p></body></html>"))
        self.add.setText(_translate("change", "Add"))
        self.ok.setText(_translate("change", "OK"))
