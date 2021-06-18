# -*- coding: utf-8 -*-

                                                     
from xlsxwriter.workbook import Workbook
import xlrd                                                      
from PyQt5 import QtCore, QtGui, QtWidgets
import csv

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(649, 553)

        self.model = QtGui.QStandardItemModel(Form)

        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setModel(self.model)
        self.tableView.setGeometry(QtCore.QRect(20, 160, 401, 341))
        self.tableView.setObjectName("tableView")

        self.model.setHorizontalHeaderLabels(["Имя", "Время действия", "Статус сотрудника", "Часы", "Минуты"])
        self.tableView.setModel(self.model)



        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(440, 450, 181, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_pushButtonLoad_clicked)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 390, 181, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.fileSave)


        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 140, 401, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(450, 180, 161, 191))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 20, 650, 115))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("icons/background_logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.fileName = ("Attendance.csv")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Security Control System"))
        self.pushButton.setText("Обновить")
        self.pushButton_2.setText("Экспорт в файл")
        self.label.setText("Журнал посещаемости предприятия сотрудниками")
        self.label_2.setText("В данной таблице можно наблюдать всю основную информацию по посещению сотрудниками территории организации. Отображаются основные поля, регистриуремые в течение работы системы, администратором приложения.")

   
    def loadCsv(self, fileName):
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)
        self.tableView.setColumnWidth(0, 100)
        self.tableView.setColumnWidth(1, 150)
        self.tableView.setColumnWidth(2, 150)        

    def on_pushButtonLoad_clicked(self):
        self.loadCsv(self.fileName)

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
        model = self.tableView.model()
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

class OpenList(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)

#     ui = OpenList()
#     ui.show()

#     sys.exit(app.exec_())
