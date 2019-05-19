
from vedioReal import Ui_vedio
from changeUIreal import Ui_changeReal
from zimuReal import Ui_zimuReal
from jianjiReal import Ui_jianjiDReal
from seprateReal import Ui_seg
from vlogMakeReal import Ui_vlogmake
from MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow

class Ui_MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

        # 暂时修改...我做一些逻辑
        # self.toolButton_7.clicked.connect(self.changeUI)  # 格式转换
        self.toolButton_7.clicked.connect(self.zimuUI)
        self.toolButton_4.clicked.connect(self.vedioUI)
        self.toolButton_6.clicked.connect(self.zimuUI)
        self.toolButton_3.clicked.connect(self.jianjiUI)
        self.toolButton.clicked.connect(self.vlogmakeUI)
        self.toolButton_2.clicked.connect(self.seprateUI)  # s视频分割

        qssStyle = '''
        MainWindow{background-color: rgb(232, 241, 252)}
        QWidget{
        border:none;
        background: rgb(232, 241, 252);
        }

        QFrame{
        border: 1px solid rgb(111, 156, 207);
        background: rgb(232, 241, 252);
        }

        QToolButton{
		 border-radius: 4px;
		 border: none;
		 width: 75px;
		 height: 25px;
		 background: rgb(173, 202, 232)
		 }
        
        QLabel {
        color: black;
        border: none;
        }
                '''
        self.centralwidget.setStyleSheet(qssStyle)
        self.setStyleSheet(qssStyle)


    def changeUI(self):
        self.mainWindow.hide()
        myDialog = Ui_changeReal()  # 创建对话框
        myDialog.show()
        myDialog.exec_()
        self.mainWindow.show()

    def seprateUI(self):
        self.mainWindow.hide()
        myDialog = Ui_seg()  # 创建对话框
        myDialog.show()
        myDialog.exec_()
        self.mainWindow.show()

    def zimuUI(self):
        self.mainWindow.hide()
        myDialog = Ui_zimuReal()  # 创建对话框
        myDialog.show()
        myDialog.exec_()
        self.mainWindow.show()

    def jianjiUI(self ):
        self.mainWindow.hide()
        myDialog = Ui_jianjiDReal()  # 创建对话框
        myDialog.show()
        myDialog.exec_()
        self.mainWindow.show()

    def vedioUI(self):
        self.mainWindow.hide()
        myDialog = Ui_vedio()  # 创建对话框
        myDialog.show()
        myDialog.exec_()
        self.mainWindow.show()

    def vlogmakeUI(self):
        self.mainWindow.hide()
        myDialog = Ui_vlogmake()  # 创建对话框
        myDialog.show()
        myDialog.exec_()
        self.mainWindow.show()

