# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zimu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import  QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5 import QtCore
from zimu import Ui_zimu
global play
play=1
filedic={}

class Ui_zimuReal(Ui_zimu,QDialog):
    def __init__(self):
        super(Ui_zimu,self).__init__()
        self.setupUi(self)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video_2)  # 视频播放输出的widget，就是上面定义的
        self.add.clicked.connect(self.openVideoFile)  # 打开视频文件按钮
        self.start.clicked.connect(self.zimucreat)  # zimu
        self.play.clicked.connect(self.playVideo)  # play
        self.player.positionChanged.connect(self.changeSlide)  # change Slide
        self.listWidget.itemClicked.connect(self.clickPlayVideo)
        qssStyle = '''

                QWidget{
                        border: 1px solid rgb(111, 156, 207);
                        background: rgb(232, 241, 252);
                }
                QProgressBar{
                        border: none;
                        text-align: center;
                        color: white;
                        background: rgb(173, 202, 232);
                }
                QLabel{
                        border: none;
                        color: black; 
                }
                QSlider{
                    border: none;
                }

                QPushButton{
                		border-radius: 4px;
                		border: none;
                		width: 75px;
                		height: 25px;
                		background: rgb(173, 202, 232)
                }
                QToolButton{
                border:none}
                
                QTextEdit {
        border: 1px solid rgb(111, 156, 207);
        color: rgb(70, 71, 73);
        background: rgb(255, 255, 255);
}


                 QTextBrowser{
                    background:rgb(255,255,255);
                    border-radius: 4px;
                	 border: 1px solid rgb(111, 156, 207);

                    }
                      QListWidget{
                      border-radius: 4px;
                	    border: 1px solid rgb(111, 156, 207);

                    background:rgb(255,255,255);
                    }
                                '''
        self.widget_left.setStyleSheet(qssStyle)
        self.widget_bottom.setStyleSheet(qssStyle)
        self.widgetcentral_cen.setStyleSheet(qssStyle)
        self.wgt_video_2.setStyleSheet(qssStyle)
        self.widget_right.setStyleSheet(qssStyle)


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
            self.play.setIcon(icon)
        elif play==2:
            self.player.pause()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../../Desktop/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.play.setIcon(icon)
            play = 1

    def changeSlide(self, position):
        self.vidoeLength = self.player.duration() + 0.1
        self.sld_video.setValue(round((position / self.vidoeLength) * 100))
        self.lab_video.setText(str(round((position / self.vidoeLength) * 100, 2)) + '%')



