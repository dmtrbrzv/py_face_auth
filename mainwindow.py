import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
import resource

from out_window import Ui_OutputDialog
from listOfWorkers import Load_dialog
from listOfStatus import OpenList


class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        loadUi("ui/mainwindow.ui", self)

        self.runButton.clicked.connect(self.runSlot)
        self.workerButton.clicked.connect(self.showWorkers)
        self.documentButton.clicked.connect(self.showStatus)

        self._new_window = None
        self.Videocapture_ = None

    def refreshAll(self):
        """
        Set the text of lineEdit once it's valid
        """
        self.Videocapture_ = "0"

    @pyqtSlot()
    def runSlot(self):
        """
        Called when the user presses the Run button
        """
        # print("Clicked Run")
        self.refreshAll()
        # print(self.Videocapture_)

        
        self.hide()  # hide the main window
        self.outputWindow_()  # Create and open new output window

    def showWorkers(self):
        self.ui = Load_dialog()
        self.ui.show()

    def showStatus(self):
        self.listStatus = OpenList()
        self.listStatus.show()    

    def outputWindow_(self):
        self._new_window = Ui_OutputDialog()
        self._new_window.show()
        self._new_window.startVideo(self.Videocapture_)
        # print("Video Played")
