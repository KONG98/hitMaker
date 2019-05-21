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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(seg)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(seg)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.widget_2)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.progressBar = QtWidgets.QProgressBar(self.widget_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.widget = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(50, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add = QtWidgets.QPushButton(self.widget)
        self.add.setObjectName("add")
        self.horizontalLayout.addWidget(self.add)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.OK = QtWidgets.QPushButton(self.widget)
        self.OK.setObjectName("OK")
        self.horizontalLayout.addWidget(self.OK)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_2.addWidget(self.widget_2)

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
