# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jianjiUID.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_jianjiD(object):
    def setupUi(self, jianjiD):
        jianjiD.setObjectName("jianjiD")
        jianjiD.resize(1600, 1400)
        self.widget_left = QtWidgets.QWidget(jianjiD)
        self.widget_left.setGeometry(QtCore.QRect(0, 0, 300, 1400))
        self.widget_left.setObjectName("widget_left")
        self.listWidget_3 = QtWidgets.QListWidget(self.widget_left)
        self.listWidget_3.setGeometry(QtCore.QRect(0, 0, 300, 1401))
        self.listWidget_3.setObjectName("listWidget_3")
        self.add_3 = QtWidgets.QPushButton(self.widget_left)
        self.add_3.setGeometry(QtCore.QRect(60, 1290, 170, 60))
        self.add_3.setObjectName("add_3")
        self.wgt_video_2 = myVideoWidget(jianjiD)
        self.wgt_video_2.setGeometry(QtCore.QRect(300, 0, 1301, 991))
        self.wgt_video_2.setObjectName("wgt_video_2")
        self.widget_bottom = QtWidgets.QWidget(jianjiD)
        self.widget_bottom.setGeometry(QtCore.QRect(300, 1150, 1300, 251))
        self.widget_bottom.setObjectName("widget_bottom")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.widget_bottom)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 0, 1300, 261))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.widgetcentral_cen = QtWidgets.QWidget(jianjiD)
        self.widgetcentral_cen.setGeometry(QtCore.QRect(300, 990, 1301, 161))
        self.widgetcentral_cen.setObjectName("widgetcentral_cen")
        self.play_3 = QtWidgets.QToolButton(self.widgetcentral_cen)
        self.play_3.setGeometry(QtCore.QRect(160, 20, 170, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_3.setIcon(icon)
        self.play_3.setIconSize(QtCore.QSize(130, 70))
        self.play_3.setObjectName("play_3")
        self.sld_video_2 = QtWidgets.QSlider(self.widgetcentral_cen)
        self.sld_video_2.setGeometry(QtCore.QRect(420, 100, 831, 31))
        self.sld_video_2.setMaximum(100)
        self.sld_video_2.setSliderPosition(100)
        self.sld_video_2.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video_2.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.sld_video_2.setObjectName("sld_video_2")
        self.label_3 = QtWidgets.QLabel(self.widgetcentral_cen)
        self.label_3.setGeometry(QtCore.QRect(380, 90, 121, 41))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.widgetcentral_cen)
        self.label.setGeometry(QtCore.QRect(380, 10, 131, 31))
        self.label.setObjectName("label")
        self.sld_video_6 = QtWidgets.QSlider(self.widgetcentral_cen)
        self.sld_video_6.setGeometry(QtCore.QRect(440, 10, 801, 31))
        self.sld_video_6.setMaximum(100)
        self.sld_video_6.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video_6.setObjectName("sld_video_6")
        self.ok = QtWidgets.QPushButton(self.widgetcentral_cen)
        self.ok.setGeometry(QtCore.QRect(20, 40, 170, 60))
        self.ok.setObjectName("ok")

        self.retranslateUi(jianjiD)
        QtCore.QMetaObject.connectSlotsByName(jianjiD)

    def retranslateUi(self, jianjiD):
        _translate = QtCore.QCoreApplication.translate
        jianjiD.setWindowTitle(_translate("jianjiD", "Dialog"))
        self.add_3.setText(_translate("jianjiD", "添加文件"))
        self.textBrowser_3.setHtml(_translate("jianjiD", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Log:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.play_3.setText(_translate("jianjiD", "..."))
        self.label_3.setText(_translate("jianjiD", "to"))
        self.label.setText(_translate("jianjiD", "from"))
        self.ok.setText(_translate("jianjiD", "确认"))

from myVideoWidget import myVideoWidget
