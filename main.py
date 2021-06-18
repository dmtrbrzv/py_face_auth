from sqlite3.dbapi2 import Date
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QMessageBox
from PyQt5.uic import loadUi
from check_db import *
from mainwindow import Ui_Dialog
import datetime



class Interface(QDialog):
    def __init__(self):
        super(Interface, self).__init__()
        loadUi("ui/login_menu.ui", self)

        self.passwordLabel.setEchoMode(QLineEdit.Password)

        # self.loginButton.clicked.connect(self.auth)
        self.base_line_edit = [self.loginLabel, self.passwordLabel]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

        now = QtCore.QDate.currentDate()
        current_date = now.toString('dd')
        current_time = datetime.datetime.now().strftime("%I")
        

        int_date = int(current_date)
        int_time = int(current_time)
        result = self.checkDate(int_date,int_time)

        self.date_label.setText(result)
       

    def checkDate(self, current_date, current_time):
        if (current_date % 3 == 0) & (current_time == 12):
            self.loginButton.clicked.connect(self.checkAuth)
            result = "*Сегодня необходимо сменить пароль"
            print("*Пора менять пароль")
        elif (current_date % 3 == 1 ):
            self.loginButton.clicked.connect(self.auth)
            result = "*Осталось 2 дня до смены пароля" 
            print("Осталось два дня")
        elif (current_date % 3 == 2):
            self.loginButton.clicked.connect(self.auth)
            result = "*Остался 1 день до смены пароля"
            print("Остался 1 день") 
        elif (current_date % 3 == 0) & (current_time != 12):
            self.loginButton.clicked.connect(self.auth)
            result = "*Сегодня необходимо сменить пароль"
        return result

    def checkAuth(self):
        QMessageBox.about(self, "Предупреждение", "Вам необходимо сменить пароль!")

    def check_input(funct):
        def wrapper(self):
            for loginLabel in self.base_line_edit:
                if len(loginLabel.text()) == 0:
                    return
            funct(self)
        return wrapper

    # Обработчик сигналов
    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    @check_input
    def auth(self):
        name = self.loginLabel.text()
        passw = self.passwordLabel.text()
        elem = self.check_db.thr_login(name, passw)
        if elem == 1:
            self.output()
            self.close()

    def output(self):
        self.newwindow = Ui_Dialog()
        self.newwindow.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())        