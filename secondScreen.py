import pyrebase
from PyQt5.QtWidgets import QMainWindow
import sqlite3
from thirdscreen import *
executors = [{'executor' : 'ООО «НИИПГАЗА»', 'postal' : '450059, Россия, Республика Башкортостан, г. Уфа, проспект Октября, дом 43/5, офис Б',
                          'cert' : '№ ЛНК-053А0002 от 02.03.2021 г'},
        {'executor' : 'ООО «Энергоэксперт»', 'postal' : '197342, г. Санкт-Петербург, наб. Черной речки, д.41, к.2, лит. Б, пом.7',
                          'cert' : '№ 89А112162 от 14.02.2020 г.'}]
clients = [{'client' : 'ООО «Газпром трансгаз Казань»', 'postal' : '450059, Россия, Республика Башкортостан, г. Уфа, проспект Октября, дом 43/5, офис Б'},
        {'client' : 'ООО «Газпром трансгаз Югорск»', 'postal' : '628260, РФ, г. Югорск, ул. Мира, 15'}]
from Ui_ChooseExecutors import Ui_MainWindow
firebaseconfig = {'apiKey': "AIzaSyDQeQ_YV0ZVeLW--dzDt6XntEwcCEGwTrg",
                  'authDomain': "energotemp-9b8c9.firebaseapp.com",
                  'databaseURL': "https://energotemp-9b8c9-default-rtdb.europe-west1.firebasedatabase.app",
                  'projectId': "energotemp-9b8c9",
                  'storageBucket': "energotemp-9b8c9.appspot.com",
                  'messagingSenderId': "622369709896",
                  'appId': "1:622369709896:web:5b1121856ffdff3a4e9d7d"}

fireBaseApp= pyrebase.initialize_app(firebaseconfig)
database = fireBaseApp.database()
jsonstring = dict()
class SecondScreen (Ui_MainWindow):
    # Own methods
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("SELECT user FROM USERSTABLE")
    rows = cur.fetchall()
    executorList = [i["executor"] for i in executors]
    clientList =[i["client"] for i in clients]
    surNames = [row[0] for row in rows]
    def initEventListeners(self):
        self.comboBox.addItems(self.executorList)
        self.comboBox_2.addItems(self.clientList)
        self.comboBox_3.addItems(self.surNames)
        self.pushButton_continue.clicked.connect(self.nextScreen)
    def nextScreen(self):
        global jsonstring
        jsonstring = {"executor": self.comboBox.currentIndex(),"client": self.comboBox_2.currentIndex(),"FIO": self.comboBox_3.currentIndex()}
        self.chooseMethods = QMainWindow()
        self.chooseMethodsUi = ThirdScreen()
        self.chooseMethodsUi.setupUi(self.chooseMethods)
        self.chooseMethodsUi.initEventListeners()
        self.chooseMethods.show()
