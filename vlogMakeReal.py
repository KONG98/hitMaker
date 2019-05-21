# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vlogMake.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5 import QtCore,QtGui
from vlogMake import Ui_vlogmake
global play
play=1
filedic={}
class Ui_vlogmake(Ui_vlogmake,QDialog):
    def __init__(self):
        super(Ui_vlogmake, self).__init__()
        self.setupUi(self)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video_2)  # 视频播放输出的widget，就是上面定义的
        self.add.clicked.connect(self.openVideoFile)  # 打开视频文件按钮
        self.play.clicked.connect(self.playVideo)  # play
        self.player.positionChanged.connect(self.changeSlide)  # change Slide
        self.listWidget.itemClicked.connect(self.clickPlayVideo)
        self.comboBox.addItems(["model1","model2"])
        qssStyle = '''
      
        QWidget{
                border: none;
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
            QComboBox{
             
            background:rgb(255,255,255);
            }
                        '''


        self.widget_left.setStyleSheet(qssStyle)
        self.widget.setStyleSheet(qssStyle)
       # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框




        self.widgetcentral_cen.setStyleSheet(qssStyle)
        self.wgt_video_2.setStyleSheet(qssStyle)



    def openVideoFile(self):
        filepath = QFileDialog.getOpenFileNames()[0]
        for onefilepath in filepath:
          filename = onefilepath.split('/')[-1:][0]
          url = QtCore.QUrl(onefilepath)
          print(url)
          self.listWidget.addItem(filename)
          global filedic
          filedic[filename] = url

    def changeSlide(self, position):
        self.vidoeLength = self.player.duration() + 0.1
        self.sld_video.setValue(round((position / self.vidoeLength) * 100))
        self.lab_video.setText(str(round((position / self.vidoeLength) * 100, 2)) + '%')

    def playVideo(self):  # 1开始播放，2停止播放
        global play
        if play == 1:
            self.player.play()
            play = 2
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../../Desktop/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.play.setIcon(icon)
        elif play == 2:
            self.player.pause()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../../Desktop/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.play.setIcon(icon)
            play = 1

    def clickPlayVideo(self, item):
        self.player.setMedia(QMediaContent(filedic[item.text()]))
        self.player.play()
        self.player.pause()