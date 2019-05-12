from PyQt5.QtWidgets import *
from playWindowUI import myMainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vieo_gui = myMainWindow()
    vieo_gui.show()
    sys.exit(app.exec_())