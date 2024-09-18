from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from widget import DialogForgot_ui as ui

class DialogForgotClass(QDialog, ui.Ui_Dialog):
    def __init__(self,data):
        super(DialogForgotClass,self).__init__()
        self.setupUi(self)
        self.data = data
        #connect
        self.search_btn.clicked.connect(self.searchEmail)
        self.close_btn.clicked.connect(self.reject)

    def searchEmail(self):
        searc = self.email_le.text()
        for e in self.data:
            print(self.data[e].get('email'))
            if self.data[e].get('email') == searc:
                pas = self.data[e]['pass']
                pas = pas[0] + '*****' + pas[6:]
                self.answer_lb.setText(pas)





