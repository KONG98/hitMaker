from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5 import QtCore
from playUI import Ui_MainWindow
filedic={}

class myMainWindow(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video_2)  # 视频播放输出的widget，就是上面定义的
        self.pushButton.clicked.connect(self.openVideoFile)   # 打开视频文件按钮
        self.pushButton_7.clicked.connect(self.playVideo)       # play
        self.pushButton_8.clicked.connect(self.pauseVideo)       # pause
        self.player.positionChanged.connect(self.changeSlide)      # change Slide
        self.listWidget.itemClicked.connect(self.clickPlayVideo)
    def openVideoFile(self):
        filepath = QFileDialog.getOpenFileName()[0]
        filename = filepath.split('/')[-1:][0]
        url = QtCore.QUrl(filepath)
        self.listWidget.addItem(filename)
        global filedic
        filedic[filename]=url
        print(filedic)
    def playVideo(self):
        self.player.play()
    def clickPlayVideo(self,item):
        self.player.setMedia(QMediaContent(filedic[item.text()]))
        self.player.play()

    def pauseVideo(self):
        self.player.pause()
    def changeSlide(self,position):
       self.vidoeLength = self.player.duration()+0.1
       self.sld_video.setValue(round((position/self.vidoeLength)*100))
       self.lab_video.setText(str(round((position/self.vidoeLength)*100,2))+'%')
