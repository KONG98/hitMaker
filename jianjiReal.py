from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5 import QtCore,QtGui
from jianjiUID import Ui_jianjiD

global play
play=1
filedic={}
class Ui_jianjiDReal(Ui_jianjiD,QDialog):
    def __init__(self):
        super(Ui_jianjiD,self).__init__()
        self.setupUi(self)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video_2)  # 视频播放输出的widget，就是上面定义的
        self.add_3.clicked.connect(self.openVideoFile)  # 打开视频文件按钮
        self.listWidget_3.itemClicked.connect(self.clickPlayVideo) #点击某个素材
        self.play_3.clicked.connect(self.playVideo)  # play
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("picture/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_3.setIcon(icon)
        qssStyle = '''

               QWidget{
                       border:none;
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
                               '''
        self.widget_left.setStyleSheet(qssStyle)
        self.widget_bottom.setStyleSheet(qssStyle)
        self.widgetcentral_cen.setStyleSheet(qssStyle)
        self.wgt_video_2.setStyleSheet(qssStyle)

    def openVideoFile(self):
        filepath = QFileDialog.getOpenFileName()[0]
        filename = filepath.split('/')[-1:][0]
        url = QtCore.QUrl(filepath)
        self.listWidget_3.addItem(filename)
        self.textBrowser_3.append("添加成功")


        global filedic
        filedic[filename] = url

    def clickPlayVideo(self, item):
        self.player.setMedia(QMediaContent(filedic[item.text()]))
        self.player.play()
        self.player.pause()

    def playVideo(self):  # 1开始播放，2停止播放
        global play
        if play == 1:
            self.player.play()
            play = 2
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("picture/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.play_3.setIcon(icon)
        elif play == 2:
            self.player.pause()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("picture/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.play_3.setIcon(icon)
            play = 1

