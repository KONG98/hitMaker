# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seprateUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5 import QtCore

filedic = {}


class Ui_seg(object):
    def setupUi(self, seg):
        seg.setObjectName("seg")
        seg.resize(800, 500)
        self.listWidget = QtWidgets.QListWidget(seg)
        self.listWidget.setGeometry(QtCore.QRect(40, 40, 711, 181))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(seg)
        self.pushButton.setGeometry(QtCore.QRect(40, 420, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.buttonBox = QtWidgets.QDialogButtonBox(seg)
        self.buttonBox.setGeometry(QtCore.QRect(515, 422, 241, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.progressBar = QtWidgets.QProgressBar(seg)
        self.progressBar.setGeometry(QtCore.QRect(40, 380, 711, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.textBrowser = QtWidgets.QTextBrowser(seg)
        self.textBrowser.setGeometry(QtCore.QRect(40, 250, 711, 111))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton.clicked.connect(self.openVideoFile)

        self.retranslateUi(seg)
        self.buttonBox.accepted.connect(seg.accept)
        self.buttonBox.rejected.connect(seg.reject)
        QtCore.QMetaObject.connectSlotsByName(seg)

    def retranslateUi(self, seg):
        _translate = QtCore.QCoreApplication.translate
        seg.setWindowTitle(_translate("seg", "Dialog"))
        self.pushButton.setText(_translate("seg", "Add"))
        self.textBrowser.setHtml(_translate("seg",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LOG:</p></body></html>"))

    def openVideoFile(self):
        filepath = QFileDialog.getOpenFileName()[0]
        filename = filepath.split('/')[-1:][0]
        url = QtCore.QUrl(filepath)
        self.listWidget.addItem(filename)
        global filedic
        filedic[filename] = url
