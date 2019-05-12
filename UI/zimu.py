# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zimu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5 import QtCore

global play
play=1
filedic={}

class Ui_zimu(object):
    def setupUi(self, zimu):
        zimu.setObjectName("zimu")
        zimu.resize(1600, 1346)
        self.textBrowser = QtWidgets.QTextBrowser(zimu)
        self.textBrowser.setGeometry(QtCore.QRect(300, 1140, 1301, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.wgt_video_2 = myVideoWidget(zimu)
        self.wgt_video_2.setGeometry(QtCore.QRect(300, 0, 991, 1041))
        self.wgt_video_2.setObjectName("wgt_video_2")
        self.sld_video = QtWidgets.QSlider(zimu)
        self.sld_video.setGeometry(QtCore.QRect(700, 1060, 461, 61))
        self.sld_video.setMaximum(100)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.listWidget = QtWidgets.QListWidget(zimu)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 300, 1400))
        self.listWidget.setObjectName("listWidget")
        self.lab_video = QtWidgets.QLabel(zimu)
        self.lab_video.setGeometry(QtCore.QRect(1220, 1070, 141, 41))
        self.lab_video.setObjectName("lab_video")
        self.textEdit = QtWidgets.QTextEdit(zimu)
        self.textEdit.setGeometry(QtCore.QRect(1290, 0, 311, 1141))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(zimu)
        self.pushButton.setGeometry(QtCore.QRect(0, 1259, 301, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(zimu)
        self.pushButton_2.setGeometry(QtCore.QRect(1290, 1040, 311, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        self.toolButton = QtWidgets.QToolButton(zimu)
        self.toolButton.setGeometry(QtCore.QRect(530, 1040, 171, 101))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(130, 70))
        self.toolButton.setObjectName("toolButton")
        self.pushButton_3 = QtWidgets.QPushButton(zimu)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 1040, 231, 101))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(zimu)
        QtCore.QMetaObject.connectSlotsByName(zimu)

        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video_2)  # 视频播放输出的widget，就是上面定义的
        self.pushButton.clicked.connect(self.openVideoFile)  # 打开视频文件按钮
        self.pushButton_3.clicked.connect(self.zimucreat)  # zimu
        self.toolButton.clicked.connect(self.playVideo)  # play
        self.player.positionChanged.connect(self.changeSlide)  # change Slide
        self.listWidget.itemClicked.connect(self.clickPlayVideo)

    def retranslateUi(self, zimu):
        _translate = QtCore.QCoreApplication.translate
        zimu.setWindowTitle(_translate("zimu", "Dialog"))
        self.textBrowser.setHtml(_translate("zimu", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Log:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lab_video.setText(_translate("zimu", "0%"))
        self.pushButton.setText(_translate("zimu", "添加文件"))
        self.pushButton_2.setText(_translate("zimu", "保存"))
        self.toolButton.setText(_translate("zimu", "..."))
        self.pushButton_3.setText(_translate("zimu", "开始生成"))

    def openVideoFile(self):
        filepath = QFileDialog.getOpenFileName()[0]
        filename = filepath.split('/')[-1:][0]
        url = QtCore.QUrl(filepath)
        self.listWidget.addItem(filename)
        global filedic
        filedic[filename] = url




    def clickPlayVideo(self, item):
        self.player.setMedia(QMediaContent(filedic[item.text()]))
        self.player.play()
        self.player.pause()

    def zimucreat(self, item):
        self.player.setMedia(QMediaContent(filedic[item.text()]))
        self.player.play()

    def playVideo(self):#1开始播放，2停止播放
        global play
        if play==1:
            self.player.play()
            play=2
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../../Desktop/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton.setIcon(icon)
        elif play==2:
            self.player.pause()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../../Desktop/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton.setIcon(icon)
            play = 1

    def changeSlide(self, position):
        self.vidoeLength = self.player.duration() + 0.1
        self.sld_video.setValue(round((position / self.vidoeLength) * 100))
        self.lab_video.setText(str(round((position / self.vidoeLength) * 100, 2)) + '%')



from myVideoWidget import myVideoWidget



