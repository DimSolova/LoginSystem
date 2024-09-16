from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from widget import OpenWindow_ui as ui


class LoginSystemClass(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(LoginSystemClass,self).__init__()
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication([])
    w = LoginSystemClass()
    w.show()
    app.exec()
