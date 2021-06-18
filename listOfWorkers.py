# -*- coding: utf-8 -*-

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from xlsxwriter.workbook import Workbook
import xlrd 

class Worker_Dialog(object):

    def loadFromBase(self):
        connection = sqlite3.connect('datebase/SystemSecurity.db')
        query = "SELECT name, position FROM worker"
        result = connection.execute(query)
        self.tableOfWorkers.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableOfWorkers.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableOfWorkers.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(655, 553)
        

        self.tableOfWorkers = QtWidgets.QTableWidget(Dialog)
        self.tableOfWorkers.setGeometry(QtCore.QRect(20, 230, 417, 270))
        self.tableOfWorkers.setRowCount(6)
        self.tableOfWorkers.setColumnCount(2)
        self.tableOfWorkers.setObjectName("tableOfWorkers")
        self.tableOfWorkers.setColumnWidth(1,200)
        self.tableOfWorkers.setColumnWidth(0,200)
        self.tableOfWorkers.setHorizontalHeaderLabels(["Имя", "Должность"])

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 30, 661, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/background_logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(460, 440, 181, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fileSave)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(468, 240, 171, 175))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        
        self.loadFromBase()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Security Control System"))
        self.pushButton.setText(_translate("Dialog", "Экспорт данных"))
        self.label_2.setText(_translate("Dialog", "Зарегистрировано в базе 36 сотрудников. Фотоматериалы хранятся в отдельной БД, доступа к которой нет ни у кого из сотрудников. В данной таблице отображается лишь основная ифнормация, необходимая для осуществления контроля на территории организации."))

    def fileSave(self):
        fileName, ok = QtWidgets.QFileDialog.getSaveFileName(
            None,
            "Сохранить файл",
            ".",
            "All Files(*.xlsx)"
        )
        if not fileName:
            return 

        _list = []
        model = self.tableOfWorkers.model()
        for row in range(model.rowCount()):
            _r = []
            for column in range(model.columnCount()):
                _r.append("{}".format(model.index(row, column).data() or ""))
            _list.append(_r)
        print(fileName)
        
        workbook = Workbook(fileName)
        worksheet = workbook.add_worksheet() 

        for r, row in enumerate(_list):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)        
        workbook.close()  
        msg = QtWidgets.QMessageBox.information(
            None, 
            "Success!", 
            f"Данные сохранены в файле: \n{fileName}"
        )     

class Load_dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Worker_Dialog()
        self.ui.setupUi(self)

