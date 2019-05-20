# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seprateUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_seg(object):
    def setupUi(self, seg):
        seg.setObjectName("seg")
        seg.resize(800, 500)
        self.widget_2 = QtWidgets.QWidget(seg)
        self.widget_2.setGeometry(QtCore.QRect(0, -1, 800, 501))
        self.widget_2.setObjectName("widget_2")
        self.listWidget = QtWidgets.QListWidget(self.widget_2)
        self.listWidget.setGeometry(QtCore.QRect(9, 10, 781, 201))
        self.listWidget.setObjectName("listWidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 220, 781, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(self.widget_2)
        self.progressBar.setGeometry(QtCore.QRect(0, 390, 801, 41))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.add = QtWidgets.QPushButton(self.widget_2)
        self.add.setGeometry(QtCore.QRect(20, 440, 111, 40))
        self.add.setObjectName("add")
        self.OK = QtWidgets.QPushButton(self.widget_2)
        self.OK.setGeometry(QtCore.QRect(170, 440, 111, 40))
        self.OK.setObjectName("OK")

        self.retranslateUi(seg)
        QtCore.QMetaObject.connectSlotsByName(seg)

    def retranslateUi(self, seg):
        _translate = QtCore.QCoreApplication.translate
        seg.setWindowTitle(_translate("seg", "Dialog"))
        self.textBrowser.setHtml(_translate("seg",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LOG:</p></body></html>"))
        self.add.setText(_translate("seg", "Add"))
        self.OK.setText(_translate("seg", "OK"))
