from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from changeUI import Ui_change
filedic={}
class Ui_changeReal(Ui_change,QDialog):
    def __init__(self):
        super(Ui_change, self).__init__()
        self.setupUi(self)
        self.comboBox_2.addItems([".mp4", ".mp3", ".avi", ".mov"])
        self.add.clicked.connect(self.openVideoFile)
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
            
            QComboBox {
        height: 25px;
        border-radius: 4px;
        border: 1px solid rgb(111, 156, 207);
        background: rgba(255, 255, 255, 30);
}
QComboBox:enabled {
        color: rgb(84, 84, 84);
}

QComboBox:enabled:hover, QComboBox:enabled:focus {
        color: rgb(51, 51, 51);
}
                        '''
        self.widget.setStyleSheet(qssStyle)
    def openVideoFile(self):
        filepath = QFileDialog.getOpenFileName()[0]
        filename = filepath.split('/')[-1:][0]
        url = QtCore.QUrl(filepath)
        self.listWidget.addItem(filename)
        global filedic
        filedic[filename] = url

