# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zimu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5 import QtCore

filedic={}
class Ui_zimu(object):
    def setupUi(self, zimu):
        zimu.setObjectName("zimu")
        zimu.resize(1600, 1400)
        self.textBrowser = QtWidgets.QTextBrowser(zimu)
        self.textBrowser.setGeometry(QtCore.QRect(600, 1190, 871, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_8 = QtWidgets.QPushButton(zimu)
        self.pushButton_8.setGeometry(QtCore.QRect(1330, 920, 131, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.wgt_video_2 = myVideoWidget(zimu)
        self.wgt_video_2.setGeometry(QtCore.QRect(600, 130, 861, 771))
        self.wgt_video_2.setObjectName("wgt_video_2")
        self.sld_video = QtWidgets.QSlider(zimu)
        self.sld_video.setGeometry(QtCore.QRect(780, 930, 421, 31))
        self.sld_video.setMaximum(100)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.listWidget = QtWidgets.QListWidget(zimu)
        self.listWidget.setGeometry(QtCore.QRect(115, 131, 371, 1071))
        self.listWidget.setObjectName("listWidget")
        self.lab_video = QtWidgets.QLabel(zimu)
        self.lab_video.setGeometry(QtCore.QRect(1240, 930, 91, 31))
        self.lab_video.setObjectName("lab_video")
        self.textEdit = QtWidgets.QTextEdit(zimu)
        self.textEdit.setGeometry(QtCore.QRect(600, 1010, 721, 141))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(zimu)
        self.pushButton.setGeometry(QtCore.QRect(350, 1250, 130, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_7 = QtWidgets.QPushButton(zimu)
        self.pushButton_7.setGeometry(QtCore.QRect(600, 930, 131, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_2 = QtWidgets.QPushButton(zimu)
        self.pushButton_2.setGeometry(QtCore.QRect(1330, 1110, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi(zimu)
        QtCore.QMetaObject.connectSlotsByName(zimu)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video_2)  # 视频播放输出的widget，就是上面定义的
        self.pushButton.clicked.connect(self.openVideoFile)  # 打开视频文件按钮
        self.pushButton_7.clicked.connect(self.playVideo)  # play
        self.pushButton_8.clicked.connect(self.pauseVideo)  # pause
        self.player.positionChanged.connect(self.changeSlide)  # change Slide
        self.listWidget.itemClicked.connect(self.clickPlayVideo)

    def openVideoFile(self):
        filepath = QFileDialog.getOpenFileName()[0]
        filename = filepath.split('/')[-1:][0]
        url = QtCore.QUrl(filepath)
        self.listWidget.addItem(filename)
        global filedic
        filedic[filename] = url
        print(filedic)

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

    def retranslateUi(self, zimu):
        _translate = QtCore.QCoreApplication.translate
        zimu.setWindowTitle(_translate("zimu", "Dialog"))
        self.textBrowser.setHtml(_translate("zimu", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Log:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_8.setText(_translate("zimu", "暂停"))
        self.lab_video.setText(_translate("zimu", "0%"))
        self.pushButton.setText(_translate("zimu", "添加文件"))
        self.pushButton_7.setText(_translate("zimu", "播放"))
        self.pushButton_2.setText(_translate("zimu", "确认"))

from myVideoWidget import myVideoWidget
