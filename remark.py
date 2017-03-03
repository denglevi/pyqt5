# encoding=utf-8
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class RemarkDialog(QDialog):

    def __init__(self,*args):

        QDialog.__init__(self,*args)

        self.setFixedSize(300,200)
        self.setWindowTitle(u'单据备注')
        self.setModal(True)

        self.fromLayout = QFormLayout()
        self.orderNo = QLineEdit(u'%s'%self.parentWidget().orderNo)
        self.orderNo.setReadOnly(True)
        self.fromLayout.addRow(u'流水号',self.orderNo)
        self.remark = QTextEdit()
        self.fromLayout.addRow(u'备注',self.remark)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.button(QDialogButtonBox.Ok).setText(u'保存')
        buttonBox.button(QDialogButtonBox.Cancel).setText(u'取消')
        self.fromLayout.addWidget(buttonBox)

        self.setLayout(self.fromLayout)

        buttonBox.accepted.connect(self.saveRemark)
        buttonBox.rejected.connect(self.close)

    def saveRemark(self):

        remark = self.remark.toPlainText()
        print(remark)