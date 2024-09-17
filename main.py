from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import LoginWindow
import OpenWindow
import sys


if __name__ == '__main__':
    app = QApplication([])
    w = LoginWindow.LoginWindowClass()
    if w.exec():
        main = OpenWindow.LoginSystemClass(w.user)
        main.show()
        app.exec()
    else:
        sys.exit()
