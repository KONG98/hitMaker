# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'play.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 1230, 130, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 1230, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(800, 1230, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(980, 1230, 131, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1170, 1230, 131, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1350, 1230, 131, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(620, 1140, 131, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(1350, 1130, 131, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.wgt_video_2 = myVideoWidget(self.centralwidget)
        self.wgt_video_2.setGeometry(QtCore.QRect(620, 110, 861, 971))
        self.wgt_video_2.setObjectName("wgt_video_2")
        self.sld_video = QtWidgets.QSlider(self.centralwidget)
        self.sld_video.setGeometry(QtCore.QRect(800, 1140, 421, 31))
        self.sld_video.setMaximum(100)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.lab_video = QtWidgets.QLabel(self.centralwidget)
        self.lab_video.setGeometry(QtCore.QRect(1260, 1140, 91, 31))
        self.lab_video.setObjectName("lab_video")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(115, 111, 371, 1071))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "添加文件"))
        self.pushButton_2.setText(_translate("MainWindow", "生成字幕"))
        self.pushButton_3.setText(_translate("MainWindow", "视频剪辑"))
        self.pushButton_4.setText(_translate("MainWindow", "格式转换"))
        self.pushButton_5.setText(_translate("MainWindow", "一键VLOG"))
        self.pushButton_6.setText(_translate("MainWindow", "视频剪切"))
        self.pushButton_7.setText(_translate("MainWindow", "播放"))
        self.pushButton_8.setText(_translate("MainWindow", "暂停"))
        self.lab_video.setText(_translate("MainWindow", "0%"))

from myVideoWidget import myVideoWidget
