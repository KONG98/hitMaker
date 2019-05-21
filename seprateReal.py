from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from seprateUI import Ui_seg

filedic = {}


class Ui_seg(Ui_seg, QDialog):
    def __init__(self):
        super(Ui_seg, self).__init__()
        self.setupUi(self)
        self.add.clicked.connect(self.openVideoFile)
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

QPushButton{
		border-radius: 4px;
		border: none;
		width: 75px;
		height: 25px;
		background: rgb(173, 202, 232)
}


    QTextBrowser{
    background:rgb(255,255,255);
    border-radius: 4px;
		border: none;
		
    }
      QListWidget{
      border-radius: 4px;
		border: none;
		
    background:rgb(255,255,255);
    }
                '''
        self.widget_2.setStyleSheet(qssStyle)

    def openVideoFile(self):
        filepath = QFileDialog.getOpenFileName()[0]
        filename = filepath.split('/')[-1:][0]
        url = QtCore.QUrl(filepath)
        self.listWidget.addItem(filename)
        global filedic
        filedic[filename] = url
