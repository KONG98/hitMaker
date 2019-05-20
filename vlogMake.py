# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vlogMake.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_vlogmake(object):
    def setupUi(self, vlogmake):
        vlogmake.setObjectName("vlogmake")
        vlogmake.resize(1600, 1400)
        self.wgt_video_2 = myVideoWidget(vlogmake)
        self.wgt_video_2.setGeometry(QtCore.QRect(300, -1, 1301, 1051))
        self.wgt_video_2.setObjectName("wgt_video_2")
        self.widget_left = QtWidgets.QWidget(vlogmake)
        self.widget_left.setGeometry(QtCore.QRect(0, 0, 300, 1400))
        self.widget_left.setObjectName("widget_left")
        self.listWidget = QtWidgets.QListWidget(self.widget_left)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 300, 1401))
        self.listWidget.setObjectName("listWidget")
        self.add = QtWidgets.QPushButton(self.widget_left)
        self.add.setGeometry(QtCore.QRect(60, 1290, 171, 61))
        self.add.setObjectName("add")
        self.widget_bottom = QtWidgets.QWidget(vlogmake)
        self.widget_bottom.setGeometry(QtCore.QRect(300, 1150, 1300, 251))
        self.widget_bottom.setObjectName("widget_bottom")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_bottom)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 1300, 261))
        self.textBrowser.setObjectName("textBrowser")
        self.widgetcentral_cen = QtWidgets.QWidget(vlogmake)
        self.widgetcentral_cen.setGeometry(QtCore.QRect(300, 1050, 1301, 101))
        self.widgetcentral_cen.setObjectName("widgetcentral_cen")
        self.play = QtWidgets.QToolButton(self.widgetcentral_cen)
        self.play.setGeometry(QtCore.QRect(0, 0, 170, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon)
        self.play.setIconSize(QtCore.QSize(130, 70))
        self.play.setObjectName("play")
        self.start = QtWidgets.QPushButton(self.widgetcentral_cen)
        self.start.setGeometry(QtCore.QRect(1099, 19, 171, 61))
        self.start.setObjectName("start")
        self.sld_video = QtWidgets.QSlider(self.widgetcentral_cen)
        self.sld_video.setGeometry(QtCore.QRect(170, 20, 531, 61))
        self.sld_video.setMaximum(100)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.lab_video = QtWidgets.QLabel(self.widgetcentral_cen)
        self.lab_video.setGeometry(QtCore.QRect(720, 30, 51, 41))
        self.lab_video.setObjectName("lab_video")
        self.comboBox = QtWidgets.QComboBox(self.widgetcentral_cen)
        self.comboBox.setGeometry(QtCore.QRect(900, 20, 171, 61))
        self.comboBox.setObjectName("comboBox")
        self.model = QtWidgets.QLabel(self.widgetcentral_cen)
        self.model.setGeometry(QtCore.QRect(800, 30, 91, 41))
        self.model.setObjectName("model")

        self.retranslateUi(vlogmake)
        QtCore.QMetaObject.connectSlotsByName(vlogmake)

    def retranslateUi(self, vlogmake):
        _translate = QtCore.QCoreApplication.translate
        vlogmake.setWindowTitle(_translate("vlogmake", "Dialog"))
        self.add.setText(_translate("vlogmake", "添加文件"))
        self.textBrowser.setHtml(_translate("vlogmake",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Log:</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.play.setText(_translate("vlogmake", "..."))
        self.start.setText(_translate("vlogmake", "确认"))
        self.lab_video.setText(_translate("vlogmake", "0%"))
        self.model.setText(_translate("vlogmake", "model"))


from myVideoWidget import myVideoWidget
