# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\HP\Desktop\code\hitMaker-new\hitMaker\zimu.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_zimu(object):
    def setupUi(self, zimu):
        zimu.setObjectName("zimu")
        zimu.resize(920, 743)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(zimu)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_left = QtWidgets.QWidget(zimu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_left.sizePolicy().hasHeightForWidth())
        self.widget_left.setSizePolicy(sizePolicy)
        self.widget_left.setMinimumSize(QtCore.QSize(165, 650))
        self.widget_left.setObjectName("widget_left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_left)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.widget_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.add = QtWidgets.QPushButton(self.widget_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy)
        self.add.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(7)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.verticalLayout.addWidget(self.add)
        self.horizontalLayout_2.addWidget(self.widget_left)
        self.widget_4 = QtWidgets.QWidget(zimu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setContentsMargins(0, 9, 9, 9)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(650, 450))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 200))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 16666666))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wgt_video_2 = myVideoWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wgt_video_2.sizePolicy().hasHeightForWidth())
        self.wgt_video_2.setSizePolicy(sizePolicy)
        self.wgt_video_2.setMinimumSize(QtCore.QSize(450, 300))
        self.wgt_video_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.wgt_video_2.setObjectName("wgt_video_2")
        self.verticalLayout_2.addWidget(self.wgt_video_2)
        self.widgetcentral_cen = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetcentral_cen.sizePolicy().hasHeightForWidth())
        self.widgetcentral_cen.setSizePolicy(sizePolicy)
        self.widgetcentral_cen.setMinimumSize(QtCore.QSize(400, 16))
        self.widgetcentral_cen.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widgetcentral_cen.setObjectName("widgetcentral_cen")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widgetcentral_cen)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.start = QtWidgets.QPushButton(self.widgetcentral_cen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy)
        self.start.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(7)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.horizontalLayout_3.addWidget(self.start)
        self.play = QtWidgets.QToolButton(self.widgetcentral_cen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play.sizePolicy().hasHeightForWidth())
        self.play.setSizePolicy(sizePolicy)
        self.play.setMinimumSize(QtCore.QSize(30, 30))
        self.play.setMaximumSize(QtCore.QSize(60, 16777215))
        self.play.setBaseSize(QtCore.QSize(0, 0))
        self.play.setIconSize(QtCore.QSize(126, 42))
        self.play.setObjectName("play")
        self.horizontalLayout_3.addWidget(self.play)
        self.sld_video = QtWidgets.QSlider(self.widgetcentral_cen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sld_video.sizePolicy().hasHeightForWidth())
        self.sld_video.setSizePolicy(sizePolicy)
        self.sld_video.setMinimumSize(QtCore.QSize(0, 30))
        self.sld_video.setMaximum(100)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.horizontalLayout_3.addWidget(self.sld_video)
        self.lab_video = QtWidgets.QLabel(self.widgetcentral_cen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_video.sizePolicy().hasHeightForWidth())
        self.lab_video.setSizePolicy(sizePolicy)
        self.lab_video.setMinimumSize(QtCore.QSize(0, 30))
        self.lab_video.setObjectName("lab_video")
        self.horizontalLayout_3.addWidget(self.lab_video)
        self.verticalLayout_2.addWidget(self.widgetcentral_cen)
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(250, 300))
        self.textEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.embed = QtWidgets.QPushButton(self.widget_3)
        self.embed.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.embed.setFont(font)
        self.embed.setObjectName("embed")
        self.verticalLayout_3.addWidget(self.embed)
        self.save = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy)
        self.save.setMinimumSize(QtCore.QSize(0, 30))
        self.save.setMaximumSize(QtCore.QSize(1666, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(7)
        self.save.setFont(font)
        self.save.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.save.setObjectName("save")
        self.verticalLayout_3.addWidget(self.save)
        self.horizontalLayout.addWidget(self.widget_3)
        self.verticalLayout_4.addWidget(self.widget)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(600, 80))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.horizontalLayout_2.addWidget(self.widget_4)

        self.retranslateUi(zimu)
        QtCore.QMetaObject.connectSlotsByName(zimu)

    def retranslateUi(self, zimu):
        _translate = QtCore.QCoreApplication.translate
        zimu.setWindowTitle(_translate("zimu", "Dialog"))
        self.add.setText(_translate("zimu", "添加文件"))
        self.start.setText(_translate("zimu", "开始生成"))
        self.play.setText(_translate("zimu", "..."))
        self.lab_video.setText(_translate("zimu", "0%"))
        self.embed.setText(_translate("zimu", "融合"))
        self.save.setText(_translate("zimu", "保存"))
        self.textBrowser.setHtml(_translate("zimu", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Log:</span>                                        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                    </p></body></html>"))


from myVideoWidget import myVideoWidget
