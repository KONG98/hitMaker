import sys

from PyQt5.QtWidgets import *
from MainWindowReal import *

def run():
#if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
