from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from widget import OpenWindow_ui as ui
import setting


class LoginSystemClass(QMainWindow, ui.Ui_MainWindow):
    def __init__(self,user):
        super(LoginSystemClass,self).__init__()
        self.setupUi(self)
        self.stt = setting.setting()
        data = self.stt.getUserData(user)
        self.name_lb.setText(data['name'])
        text = (f"name: {data['name']}\n"
                f"last name: {data['LastName']}\n"
                f"email: {data['email']}\n"
                f"phone: {data['phone']}\n"
                f"birthday: {data['Birthday']}")
        self.name_lb.setText(text)
        self.name_lb.adjustSize()









if __name__ == '__main__':
    app = QApplication([])
    w = LoginSystemClass()
    w.show()
    app.exec()
