from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import LoginWindow
import OpenWindow
import sys


# class LoginWindowClass(LoginWindow.LoginWindowClass):
#     def __init__(self):
#         super(LoginWindowClass,self).__init__()


# class OpenWindowClass(OpenWindow.LoginSystemClass):
#     def __init__(self):
#         super(OpenWindowClass,self).__init__()


if __name__ == '__main__':
    app = QApplication([])
    w = LoginWindow.LoginWindowClass()
    if w.exec():
        main = OpenWindow.LoginSystemClass()
        main.show()
        app.exec()
    else:
        sys.exit()
