import sys

from PyQt5.QtWidgets import *
from MainWindowReal import *


def run():
    app = QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
