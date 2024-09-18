from calendar import month

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from widget import DialogCreateAccount_ui as ui
import setting


class CreateAccountDialog(QDialog, ui.Ui_CreateAccount):
    def __init__(self):
        super(CreateAccountDialog,self).__init__()
        self.setupUi(self)
        self.stt = setting.setting()
        self.data = self.stt.get_data()

        #connect
        self.saveAcc_btn.clicked.connect(self.accept)
        self.close_btn.clicked.connect(self.reject)

    def accept(self):
        if self.isLogin():
            user = self.updataData()
            self.createUserData(user)
            super(CreateAccountDialog, self).accept()

    def isLogin(self):
        allLogins = map(lambda u :self.data[u]['name'], self.data)
        if self.login_le.text() not in allLogins and self.pass_le.text():
            print('free login')
            return True
        else:
            self.infoLogin_lb.setText('This login already exist')

    # Write user in LoginsAndPass.json
    def updataData(self):
        user = f"user{len((self.data)) + 1}"
        data = {user: {
            "name": self.login_le.text(),
            "pass": self.pass_le.text(),
            'email':self.email_le.text()
        }}
        self.data.update(data)
        self.stt.saveData(self.data)
        return user

    def createUserData(self,user):
        name = self.name_le.text()
        lstName = self.lastName_le.text()
        mail = self.email_le.text()
        phone = self.mobNumber_le.text()
        birt = f'{self.day_sb.text()} {self.month_cbb.currentText()} {self.yers_sb.text()}'
        data = dict(name=name,
                    LastName=lstName,
                    email=mail,
                    phone=phone,
                    Birthday=birt)
        self.stt.saveUserData(user, data)