from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import *


class myVideoWidget(QVideoWidget):
    doubleClickedItem = pyqtSignal(str)  # 创建双击信号

    def __init__(self, parent=None):
        super(QVideoWidget, self).__init__(parent)
