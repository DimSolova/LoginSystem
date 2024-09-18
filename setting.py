import os, json
set_fold = os.path.join(os.path.expanduser('~'),'settingLoginProject')
file_logins = 'LoginsAndPass.json'

class setting():
    def __init__(self):
        super(setting,self).__init__()
        self.loginData = os.path.join(set_fold,file_logins)
        self.make_dir()

    def make_dir(self):
        if not os.path.exists(set_fold):
            os.mkdir(set_fold)
        if not os.path.exists(self.loginData):
            data = dict(user1={
                'name':'admin',
                'pass':'admin'})
            with open(self.loginData, 'w') as f:
                json.dump(data, f, indent=4)

    def get_data(self):
        return json.load(open(self.loginData))

    def saveData(self, data):
        with open(self.loginData, 'w') as f:
            json.dump(data, f, indent=4)

    def saveUserData(self,user, data):
        fileName = f"userData{user}.json"
        path = os.path.join(set_fold,fileName)
        with open(path, 'w') as f:
            json.dump(data, f, indent= 4)

    def getUserData(self,fileName):
        fileName = f"userData{fileName}.json"
        path = os.path.join(set_fold,fileName)
        return json.load(open(path))



