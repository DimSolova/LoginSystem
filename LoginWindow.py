from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from widget import DialogLoginWindow_ui as ui
import setting

class LoginWindowClass(QDialog, ui.Ui_DialogLoginWindow):
    def __init__(self):
        super(LoginWindowClass,self).__init__()
        self.setupUi(self)
        self.setting = setting.setting()
        self.data = self.setting.get_data()

        #connect
        self.logIn_btn.clicked.connect(self.accept)

    def accept(self):
        for i in self.data:
            name = self.data[i]['name']
            pas = self.data[i]['pass']
            if self.login_le_3.text() == name and self.pass_le_3.text() == pas:
                return super(LoginWindowClass, self).accept()
        self.info_lb.setText('\t\tWrong Credentials\n\t          Invalid Username or Password')
        self.info_lb.setStyleSheet("background-color: red;")

if __name__ == '__main__':
    app = QApplication([])
    w = LoginWindowClass()
    w.show()
    res = app.exec()
