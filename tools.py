# encoding=utf-8
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Tools:
    @staticmethod
    def showMsgDialog(msg, parent,title=u'系统提示'):
        msgBox = QMessageBox(QMessageBox.Warning,title , msg, QMessageBox.NoButton, parent)
        msgBox.exec_()
