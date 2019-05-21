# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zimu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5 import QtCore
from zimu import Ui_zimu
from recognizer import getSRT_PRE, getSRT_AFTER
from PyQt5.QtCore import *

global play
play = 1
filedic = {}
videoNameDic = {}
global currentVideoName
global flag
flag = 0


class Ui_zimuReal(Ui_zimu, QDialog):
    def __init__(self):
        super(Ui_zimu, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('hitMaker')

        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video_2)  # 视频播放输出的widget，就是上面定义的
        self.add.clicked.connect(self.openVideoFile)  # 打开视频文件按钮
        self.start.clicked.connect(self.zimucreat)  # zimu
        self.play.clicked.connect(self.playVideo)  # play
        self.player.positionChanged.connect(self.changeSlide)  # change Slide
        self.listWidget.itemClicked.connect(self.clickPlayVideo)
        self.save.clicked.connect(self.saveSRT)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("picture/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon)
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
        self.widget.setStyleSheet(qssStyle)
        self.widget_2.setStyleSheet(qssStyle)
        self.widget_3.setStyleSheet(qssStyle)
        self.widget_4.setStyleSheet(qssStyle)

        self.widgetcentral_cen.setStyleSheet(qssStyle)
        self.wgt_video_2.setStyleSheet(qssStyle)

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Space):
            self.playVideo()


    def openVideoFile(self):
        filepath = QFileDialog.getOpenFileName()[0]
        filename = filepath.split('/')[-1:][0]
        url = QtCore.QUrl(filepath)
        self.listWidget.addItem(filename)
        global filedic
        global videoNameDic
        filedic[filename] = url
        videoNameDic[filename] = filepath

    def clickPlayVideo(self, item):
        global currentVideoName
        currentVideoName = item.text()
        # 改！
        self.player.setMedia(QMediaContent(filedic[currentVideoName]))
        self.player.play()
        self.player.pause()
        self.setFocus()

    def zimucreat(self):

        try:
            if currentVideoName:
                videoName = videoNameDic[currentVideoName]
                SRT_pipeline = getSRT_PRE(videoName)

                Index = list(range(len(SRT_pipeline.TimeStampList)))
                count = 0
                for i in Index:
                    print(i, '开始')
                    if ((i + 1) % 3 == 0):
                        self.textEdit.append(str(SRT_pipeline.Lesson_content[count]))
                        count += 1
                    self.textEdit.append(SRT_pipeline.TimeStampList[i])

                from fileHelper import removeAllFile
                removeAllFile('chunks')
                removeAllFile('tmp')

        except NameError as e:
            print(e, 'NameError')
            return 0

    def saveSRT(self):
        content = self.textEdit.toPlainText()
        with open("subtitle.srt", "w", encoding='utf-8') as handle:
            handle.write(content)

        print('生成字幕subtitle.srt成功')

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

    def changeSlide(self, position):
        self.vidoeLength = self.player.duration() + 0.1
        self.sld_video.setValue(round((position / self.vidoeLength) * 100))
        time= QTime(0, position / 60000, qRound((position % 60000) / 1000.0))
        self.lab_video.setText(time.toString())

