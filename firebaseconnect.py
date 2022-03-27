import pyrebase
from PyQt5.QtWidgets import QMainWindow

from  Ui_ChooseExecutors import Ui_MainWindow as ChooseExecutors
from secondScreen import SecondScreen
from Ui_AuthWindow import Ui_MainWindow
firebaseconfig = {'apiKey': "AIzaSyDQeQ_YV0ZVeLW--dzDt6XntEwcCEGwTrg",
                  'authDomain': "energotemp-9b8c9.firebaseapp.com",
                  'databaseURL': "https://energotemp-9b8c9-default-rtdb.europe-west1.firebasedatabase.app",
                  'projectId': "energotemp-9b8c9",
                  'storageBucket': "energotemp-9b8c9.appspot.com",
                  'messagingSenderId': "622369709896",
                  'appId': "1:622369709896:web:5b1121856ffdff3a4e9d7d"}

fireBaseApp= pyrebase.initialize_app(firebaseconfig)
database = fireBaseApp.database()

class AuthWindow (Ui_MainWindow):
    # Own methods
    def authorize(self, login):
        allUsers = database.child("users").shallow().get()
        userNames = allUsers.val()
        # if login in userNames:
        self.label_3.setText("Авторизация прошла успешно!")
        self.chooseExecutors = QMainWindow()
        self.chooseExecutorsUi= SecondScreen()
        self.chooseExecutorsUi.setupUi(self.chooseExecutors)
        self.chooseExecutorsUi.initEventListeners()
        self.chooseExecutors.show()
        # else:
        #     self.label_3.setText("Неверный логин, попробуйте снова")

    def initEventListeners(self):
        self.pushButton.clicked.connect(
            lambda: self.authorize(self.lineEdit.text()))
        self.lineEdit.textChanged.connect(self.clearAuthStatusLabel)

    def clearAuthStatusLabel(self):
        self.label_3.clear()

