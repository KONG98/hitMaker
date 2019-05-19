# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zimu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_zimu(object):
    def setupUi(self, zimu):
        zimu.setObjectName("zimu")
        zimu.resize(800, 700)
        self.widget_left = QtWidgets.QWidget(zimu)
        self.widget_left.setGeometry(QtCore.QRect(0, 0, 151, 701))
        self.widget_left.setObjectName("widget_left")
        self.add = QtWidgets.QPushButton(self.widget_left)
        self.add.setGeometry(QtCore.QRect(20, 650, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(5)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.listWidget = QtWidgets.QListWidget(self.widget_left)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 151, 651))
        self.listWidget.setObjectName("listWidget")
        self.widget_bottom = QtWidgets.QWidget(zimu)
        self.widget_bottom.setGeometry(QtCore.QRect(150, 550, 651, 150))
        self.widget_bottom.setObjectName("widget_bottom")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_bottom)
        self.textBrowser.setGeometry(QtCore.QRect(-1, 0, 651, 150))
        self.textBrowser.setObjectName("textBrowser")
        self.widget_right = QtWidgets.QWidget(zimu)
        self.widget_right.setGeometry(QtCore.QRect(650, 0, 150, 551))
        self.widget_right.setObjectName("widget_right")
        self.textEdit = QtWidgets.QTextEdit(self.widget_right)
        self.textEdit.setGeometry(QtCore.QRect(-1, 0, 151, 551))
        self.textEdit.setObjectName("textEdit")
        self.save = QtWidgets.QPushButton(self.widget_right)
        self.save.setGeometry(QtCore.QRect(20, 490, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(5)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.widgetcentral_cen = QtWidgets.QWidget(zimu)
        self.widgetcentral_cen.setGeometry(QtCore.QRect(150, 460, 501, 91))
        self.widgetcentral_cen.setObjectName("widgetcentral_cen")
        self.play = QtWidgets.QToolButton(self.widgetcentral_cen)
        self.play.setGeometry(QtCore.QRect(90, 20, 91, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon)
        self.play.setIconSize(QtCore.QSize(126, 42))
        self.play.setObjectName("play")
        self.start = QtWidgets.QPushButton(self.widgetcentral_cen)
        self.start.setGeometry(QtCore.QRect(10, 30, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(5)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.sld_video = QtWidgets.QSlider(self.widgetcentral_cen)
        self.sld_video.setGeometry(QtCore.QRect(180, 30, 261, 51))
        self.sld_video.setMaximum(100)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.lab_video = QtWidgets.QLabel(self.widgetcentral_cen)
        self.lab_video.setGeometry(QtCore.QRect(460, 30, 31, 41))
        self.lab_video.setObjectName("lab_video")
        self.wgt_video_2 = myVideoWidget(zimu)
        self.wgt_video_2.setGeometry(QtCore.QRect(150, 0, 501, 461))
        self.wgt_video_2.setObjectName("wgt_video_2")

        self.retranslateUi(zimu)
        QtCore.QMetaObject.connectSlotsByName(zimu)

    def retranslateUi(self, zimu):
        _translate = QtCore.QCoreApplication.translate
        zimu.setWindowTitle(_translate("zimu", "Dialog"))
        self.add.setText(_translate("zimu", "添加文件"))
        self.textBrowser.setHtml(_translate("zimu", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Log:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.save.setText(_translate("zimu", "保存"))
        self.play.setText(_translate("zimu", "..."))
        self.start.setText(_translate("zimu", "开始生成"))
        self.lab_video.setText(_translate("zimu", "0%"))

from myVideoWidget import myVideoWidget
