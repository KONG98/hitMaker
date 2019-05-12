# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jianjiUID.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5 import QtCore
filedic={}

class Ui_jianjiD(object):
    def setupUi(self, jianjiD):
        jianjiD.setObjectName("jianjiD")
        jianjiD.resize(1600, 1400)
        self.sld_video_2 = QtWidgets.QSlider(jianjiD)
        self.sld_video_2.setGeometry(QtCore.QRect(750, 1020, 481, 31))
        self.sld_video_2.setMaximum(100)
        self.sld_video_2.setSliderPosition(100)
        self.sld_video_2.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video_2.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.sld_video_2.setObjectName("sld_video_2")
        self.sld_video = QtWidgets.QSlider(jianjiD)
        self.sld_video.setGeometry(QtCore.QRect(750, 930, 471, 31))
        self.sld_video.setMaximum(100)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.label_2 = QtWidgets.QLabel(jianjiD)
        self.label_2.setGeometry(QtCore.QRect(580, 1010, 121, 41))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(jianjiD)
        self.textBrowser.setGeometry(QtCore.QRect(580, 1090, 861, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.wgt_video_2 = myVideoWidget(jianjiD)
        self.wgt_video_2.setGeometry(QtCore.QRect(580, 130, 861, 771))
        self.wgt_video_2.setObjectName("wgt_video_2")
        self.listWidget = QtWidgets.QListWidget(jianjiD)
        self.listWidget.setGeometry(QtCore.QRect(85, 131, 371, 1071))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(jianjiD)
        self.pushButton.setGeometry(QtCore.QRect(320, 1250, 130, 40))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(jianjiD)
        self.label.setGeometry(QtCore.QRect(580, 920, 131, 41))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(jianjiD)
        self.pushButton_2.setGeometry(QtCore.QRect(1310, 1020, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(jianjiD)
        QtCore.QMetaObject.connectSlotsByName(jianjiD)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video_2)  # 视频播放输出的widget，就是上面定义的
        self.pushButton.clicked.connect(self.openVideoFile)  # 打开视频文件按钮
        self.listWidget.itemClicked.connect(self.clickPlayVideo) #点击某个素材

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

    def retranslateUi(self, jianjiD):
        _translate = QtCore.QCoreApplication.translate
        jianjiD.setWindowTitle(_translate("jianjiD", "Dialog"))
        self.label_2.setText(_translate("jianjiD", "to"))
        self.textBrowser.setHtml(_translate("jianjiD", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Log:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("jianjiD", "添加文件"))
        self.label.setText(_translate("jianjiD", "from"))
        self.pushButton_2.setText(_translate("jianjiD", "确认"))

from myVideoWidget import myVideoWidget
