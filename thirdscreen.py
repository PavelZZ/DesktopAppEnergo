import pyrebase
from Ui_ControlMethods import Ui_MainWindow
from jsonadd import addToJson
# Const
QTY_OF_CHECKBOXES = 6

executors = [{'executor': 'ООО «НИИПГАЗА»',
              'postal': '450059, Россия, Республика Башкортостан, г. Уфа, проспект Октября, дом 43/5, офис Б',
              'cert': '№ ЛНК-053А0002 от 02.03.2021 г'},
             {'executor': 'ООО «Энергоэксперт»',
              'postal': '197342, г. Санкт-Петербург, наб. Черной речки, д.41, к.2, лит. Б, пом.7',
              'cert': '№ 89А112162 от 14.02.2020 г.'}]
clients = [{'client': 'ООО «Газпром трансгаз Казань»',
            'postal': '450059, Россия, Республика Башкортостан, г. Уфа, проспект Октября, дом 43/5, офис Б'},
           {'client': 'ООО «Газпром трансгаз Югорск»', 'postal': '628260, РФ, г. Югорск, ул. Мира, 15'}]

devices= ["Фильтр высокого давления, инв. № 136033","Пылеуловитель, инв. № 135783"]

firebaseconfig = {'apiKey': "AIzaSyDQeQ_YV0ZVeLW--dzDt6XntEwcCEGwTrg",
                  'authDomain': "energotemp-9b8c9.firebaseapp.com",
                  'databaseURL': "https://energotemp-9b8c9-default-rtdb.europe-west1.firebasedatabase.app",
                  'projectId': "energotemp-9b8c9",
                  'storageBucket': "energotemp-9b8c9.appspot.com",
                  'messagingSenderId': "622369709896",
                  'appId': "1:622369709896:web:5b1121856ffdff3a4e9d7d"}

fireBaseApp = pyrebase.initialize_app(firebaseconfig)
database = fireBaseApp.database()
file = open("JSONstring.txt","w")

class ThirdScreen(Ui_MainWindow):
    # Own methods
    val = []
    def initEventListeners(self):
        self.comboBox.addItems(devices)
        self.dateEdit.date()
    def getState(self):
        for i in range(QTY_OF_CHECKBOXES):
            chked = False
            exec(f"chked = self.checkBox_{i + 1}.isChecked()")
            if (chked):
                self.val.append(i)
        # Чекбоксы в json
        jsonString = addToJson({"methods": self.val})
        self.comboBoxValue = self.comboBox.currentIndex()
        jsonString += addToJson({"device: " + self.comboBoxValue})


