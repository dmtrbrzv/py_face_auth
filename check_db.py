from PyQt5 import QtCore, QtGui, QtWidgets
from handler.db_handler import *


class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def thr_login(self, name, passw):
        elem = login(name, passw, self.mysignal)
        return elem

    def thr_register(self, name, passw):
        register(name, passw, self.mysignal)