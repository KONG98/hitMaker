from PyQt5.QtWidgets import *
from vedio import Ui_vedio


class Ui_vedio(Ui_vedio, QDialog):
    def __init__(self):
        super(Ui_vedio, self).__init__()
        self.setupUi(self)
        qssStyle = '''
        QWidget{
              border: 1px solid rgb(111, 156, 207);
              background: rgb(232, 241, 252);
        }
        QPushButton{
		border-radius: 4px;
		border: none;
		width: 75px;
		height: 25px;
		background: rgb(173, 202, 232)
}

                '''
        self.widget.setStyleSheet(qssStyle)
