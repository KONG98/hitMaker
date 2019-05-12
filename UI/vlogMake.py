# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vlogMake.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5 import QtCore

filedic={}
class Ui_vlogmakee(object):
    def setupUi(self, vlogmakee):
        vlogmakee.setObjectName("vlogmakee")
        vlogmakee.resize(1600, 1400)
        self.wgt_video_2 = myVideoWidget(vlogmakee)
        self.wgt_video_2.setGeometry(QtCore.QRect(620, 130, 861, 771))
        self.wgt_video_2.setObjectName("wgt_video_2")
        self.pushButton = QtWidgets.QPushButton(vlogmakee)
        self.pushButton.setGeometry(QtCore.QRect(360, 1250, 130, 40))
        self.pushButton.setObjectName("pushButton")
        self.lab_video = QtWidgets.QLabel(vlogmakee)
        self.lab_video.setGeometry(QtCore.QRect(1260, 940, 91, 31))
        self.lab_video.setObjectName("lab_video")
        self.comboBox = QtWidgets.QComboBox(vlogmakee)
        self.comboBox.setGeometry(QtCore.QRect(810, 1010, 161, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["model1","model2"])
        self.listWidget = QtWidgets.QListWidget(vlogmakee)
        self.listWidget.setGeometry(QtCore.QRect(125, 131, 371, 1071))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_7 = QtWidgets.QPushButton(vlogmakee)
        self.pushButton_7.setGeometry(QtCore.QRect(620, 930, 131, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.textBrowser = QtWidgets.QTextBrowser(vlogmakee)
        self.textBrowser.setGeometry(QtCore.QRect(620, 1090, 861, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(vlogmakee)
        self.pushButton_2.setGeometry(QtCore.QRect(1350, 1010, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(vlogmakee)
        self.label_2.setGeometry(QtCore.QRect(620, 1010, 121, 41))
        self.label_2.setObjectName("label_2")
        self.pushButton_8 = QtWidgets.QPushButton(vlogmakee)
        self.pushButton_8.setGeometry(QtCore.QRect(1350, 940, 131, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.sld_video_2 = QtWidgets.QSlider(vlogmakee)
        self.sld_video_2.setGeometry(QtCore.QRect(800, 940, 421, 31))
        self.sld_video_2.setMaximum(100)
        self.sld_video_2.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video_2.setObjectName("sld_video_2")

        self.retranslateUi(vlogmakee)
        QtCore.QMetaObject.connectSlotsByName(vlogmakee)

        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video_2)  # 视频播放输出的widget，就是上面定义的
        self.pushButton.clicked.connect(self.openVideoFile)  # 打开视频文件按钮
        self.pushButton_7.clicked.connect(self.playVideo)  # play
        self.pushButton_8.clicked.connect(self.pauseVideo)  # pause
        self.player.positionChanged.connect(self.changeSlide)  # change Slide
        self.listWidget.itemClicked.connect(self.clickPlayVideo)

    def openVideoFile(self):
        filepath = QFileDialog.getOpenFileNames()[0]
        for onefilepath in filepath:
          filename = onefilepath.split('/')[-1:][0]
          url = QtCore.QUrl(onefilepath)
          self.listWidget.addItem(filename)
          global filedic
          filedic[filename] = url

    def playVideo(self):
        self.player.play()

    def clickPlayVideo(self, item):
        self.player.setMedia(QMediaContent(filedic[item.text()]))
        self.player.play()

    def pauseVideo(self):
        self.player.pause()

    def changeSlide(self, position):
        self.vidoeLength = self.player.duration() + 0.1
        self.sld_video.setValue(round((position / self.vidoeLength) * 100))
        self.lab_video.setText(str(round((position / self.vidoeLength) * 100, 2)) + '%')

    def retranslateUi(self, vlogmakee):
        _translate = QtCore.QCoreApplication.translate
        vlogmakee.setWindowTitle(_translate("vlogmakee", "Dialog"))
        self.pushButton.setText(_translate("vlogmakee", "添加文件"))
        self.lab_video.setText(_translate("vlogmakee", "0%"))
        self.pushButton_7.setText(_translate("vlogmakee", "播放"))
        self.textBrowser.setHtml(_translate("vlogmakee", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Log:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("vlogmakee", "确认"))
        self.label_2.setText(_translate("vlogmakee", "model"))
        self.pushButton_8.setText(_translate("vlogmakee", "暂停"))

from myVideoWidget import myVideoWidget
