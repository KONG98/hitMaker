# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\HP\Desktop\code\hitMaker-new\hitMaker\vlogMake.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_vlogmake(object):
    def setupUi(self, vlogmake):
        vlogmake.setObjectName("vlogmake")
        vlogmake.resize(800, 727)
        self.horizontalLayout = QtWidgets.QHBoxLayout(vlogmake)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_left = QtWidgets.QWidget(vlogmake)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_left.sizePolicy().hasHeightForWidth())
        self.widget_left.setSizePolicy(sizePolicy)
        self.widget_left.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_left.setMaximumSize(QtCore.QSize(150, 16777215))
        self.widget_left.setObjectName("widget_left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_left)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.widget_left)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.add = QtWidgets.QPushButton(self.widget_left)
        self.add.setObjectName("add")
        self.verticalLayout.addWidget(self.add)
        self.add2 = QtWidgets.QPushButton(self.widget_left)
        self.add2.setObjectName("add2")
        self.verticalLayout.addWidget(self.add2)
        self.horizontalLayout.addWidget(self.widget_left)
        self.widget = QtWidgets.QWidget(vlogmake)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 9, 9, 9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.wgt_video_2 = myVideoWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wgt_video_2.sizePolicy().hasHeightForWidth())
        self.wgt_video_2.setSizePolicy(sizePolicy)
        self.wgt_video_2.setMinimumSize(QtCore.QSize(500, 500))
        self.wgt_video_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.wgt_video_2.setObjectName("wgt_video_2")
        self.verticalLayout_3.addWidget(self.wgt_video_2)
        self.widgetcentral_cen = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetcentral_cen.sizePolicy().hasHeightForWidth())
        self.widgetcentral_cen.setSizePolicy(sizePolicy)
        self.widgetcentral_cen.setMinimumSize(QtCore.QSize(0, 0))
        self.widgetcentral_cen.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widgetcentral_cen.setObjectName("widgetcentral_cen")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetcentral_cen)
        self.horizontalLayout_2.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.play = QtWidgets.QToolButton(self.widgetcentral_cen)
        self.play.setMinimumSize(QtCore.QSize(30, 30))
        self.play.setMaximumSize(QtCore.QSize(30, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon)
        self.play.setIconSize(QtCore.QSize(130, 70))
        self.play.setObjectName("play")
        self.horizontalLayout_2.addWidget(self.play)
        self.sld_video = QtWidgets.QSlider(self.widgetcentral_cen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sld_video.sizePolicy().hasHeightForWidth())
        self.sld_video.setSizePolicy(sizePolicy)
        self.sld_video.setMaximum(100)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.horizontalLayout_2.addWidget(self.sld_video)
        self.lab_video = QtWidgets.QLabel(self.widgetcentral_cen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_video.sizePolicy().hasHeightForWidth())
        self.lab_video.setSizePolicy(sizePolicy)
        self.lab_video.setObjectName("lab_video")
        self.horizontalLayout_2.addWidget(self.lab_video)
        self.model = QtWidgets.QLabel(self.widgetcentral_cen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model.sizePolicy().hasHeightForWidth())
        self.model.setSizePolicy(sizePolicy)
        self.model.setObjectName("model")
        self.horizontalLayout_2.addWidget(self.model)
        self.comboBox = QtWidgets.QComboBox(self.widgetcentral_cen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.start = QtWidgets.QPushButton(self.widgetcentral_cen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy)
        self.start.setObjectName("start")
        self.horizontalLayout_2.addWidget(self.start)
        self.verticalLayout_3.addWidget(self.widgetcentral_cen)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(500, 80))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(vlogmake)
        QtCore.QMetaObject.connectSlotsByName(vlogmake)

    def retranslateUi(self, vlogmake):
        _translate = QtCore.QCoreApplication.translate
        vlogmake.setWindowTitle(_translate("vlogmake", "Dialog"))
        self.add.setText(_translate("vlogmake", "添加文件"))
        self.add2.setText(_translate("vlogmake", "指定工作文件夹"))
        self.play.setText(_translate("vlogmake", "..."))
        self.lab_video.setText(_translate("vlogmake", "0%"))
        self.model.setText(_translate("vlogmake", "model"))
        self.start.setText(_translate("vlogmake", "生成"))
        self.textBrowser.setHtml(_translate("vlogmake", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Log:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


from myVideoWidget import myVideoWidget
