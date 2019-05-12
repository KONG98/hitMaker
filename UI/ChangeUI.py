# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changeUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5 import QtCore

class Ui_change(object):
    def setupUi(self, change):
        change.setObjectName("change")
        change.resize(800, 500)
        self.buttonBox = QtWidgets.QDialogButtonBox(change)
        self.buttonBox.setGeometry(QtCore.QRect(10, 430, 741, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.listWidget = QtWidgets.QListWidget(change)
        self.listWidget.setGeometry(QtCore.QRect(40, 40, 711, 181))
        self.listWidget.setObjectName("listWidget")
        self.comboBox_2 = QtWidgets.QComboBox(change)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 430, 141, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems([".mp4", ".mp3", ".avi", ".mov"])
        self.pushButton = QtWidgets.QPushButton(change)
        self.pushButton.setGeometry(QtCore.QRect(40, 430, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(change)
        self.textBrowser.setGeometry(QtCore.QRect(40, 250, 711, 111))
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(change)
        self.progressBar.setGeometry(QtCore.QRect(40, 380, 711, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton.clicked.connect(self.openVideoFile)

        self.retranslateUi(change)
        self.buttonBox.accepted.connect(change.accept)
        self.buttonBox.rejected.connect(change.reject)
        QtCore.QMetaObject.connectSlotsByName(change)

    def retranslateUi(self, change):
        _translate = QtCore.QCoreApplication.translate
        change.setWindowTitle(_translate("change", "Dialog"))
        self.pushButton.setText(_translate("change", "Add"))
        self.textBrowser.setHtml(_translate("change", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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

