# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vlogMake.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5 import QtCore, QtGui
from vlogMake import Ui_vlogmake
from PyQt5.QtGui import  QIcon
global play
global workStationPath
workStationPath = './'
play = 1
filedic = {}
from tikTokMaker import static_ImgSeq, static_tkHit_Speed


class Ui_vlogmake(Ui_vlogmake, QDialog):
    def __init__(self):
        super(Ui_vlogmake, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('hitMaker')
        self.setWindowIcon(QIcon("picture/camera.png"))
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video_2)  # 视频播放输出的widget，就是上面定义的
        self.add.clicked.connect(self.openVideoFile)  # 打开视频文件按钮
        self.add2.clicked.connect(self.openWorkStation)
        self.play.clicked.connect(self.playVideo)  # play
        self.start.clicked.connect(self.makeVlog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("picture/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon)

        self.player.positionChanged.connect(self.changeSlide)  # change Slide
        self.listWidget.itemClicked.connect(self.clickPlayVideo)
        self.comboBox.addItems(["model1", "model2"])
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

    def openWorkStation(self):
        global workStationPath
        workStationPath = QFileDialog.getExistingDirectory()

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Space):
            self.playVideo()

    def makeVlog(self):
        model = self.comboBox.currentText()
        from cmdCaller import subprocessCaller
        from fileHelper import removeOneFile
        #
        if model == 'model1':
            static_ImgSeq.run(workStation=workStationPath,outputVideoName='out.mp4')

            outputFinalName = 'out.avi'
            # #转码
            subprocessCaller('ffmpeg -i %s %s'%( str(workStationPath)+'/out.mp4' , str(workStationPath)+'/'+outputFinalName))
            removeOneFile(str(workStationPath)+'/out.mp4')
            self.listWidget.addItem(outputFinalName)
            url = QtCore.QUrl(str(workStationPath)+'/'+outputFinalName)
            global filedic
            filedic[outputFinalName]=url

  

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
        time = QTime(0, position / 60000, qRound((position % 60000) / 1000.0))
        self.lab_video.setText(time.toString())


    def playVideo(self):  # 1开始播放，2停止播放
        global play
        if play == 1:
            self.player.play()
            play = 2
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("picture/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.play.setIcon(icon)
        elif play == 2:
            self.player.pause()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("picture/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.play.setIcon(icon)
            play = 1


    def clickPlayVideo(self, item):
        self.player.setMedia(QMediaContent(filedic[item.text()]))
        self.player.play()
        self.player.pause()
        self.setFocus()
