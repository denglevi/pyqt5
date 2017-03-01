# encoding=utf-8
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):

    def __init__(self, *args):

        QWidget.__init__(self, *args)

        self.initUI()

        self.setWindowTitle(u'收银系统')

    def initUI(self):
        self.createHeader()
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.horizontalGroupBox,0,Qt.AlignTop)

        self.setLayout(self.mainLayout)

    def createHeader(self):
        self.horizontalGroupBox = QGroupBox()


        self.headLayout = QHBoxLayout()
        self.goodsNoLabel = QLabel(u'商品编号/条形码')
        self.goodsNoLabel.setFixedWidth(100)

        self.goodsNoInput = QLineEdit()
        # self.goodsNoInput.setAlignment(Qt.AlignLeft)
        self.goodsNoInput.setFixedWidth(150)
        self.goodsNoInput.setMaxLength(15)
        font = self.goodsNoInput.font()
        font.setPointSize(font.pointSize() + 5)
        self.goodsNoInput.setFont(font)

        self.operatorLabel = QLabel(u'导购员')
        self.operatorLabel.setFixedWidth(50)
        self.operatorInput = QLineEdit()
        # self.operatorInput.setAlignment(Qt.AlignLeft)
        self.operatorInput.setFixedWidth(150)
        self.operatorInput.setMaxLength(15)
        font = self.operatorInput.font()
        font.setPointSize(font.pointSize() + 5)
        self.operatorInput.setFont(font)

        self.orderNoLabel = QLabel(u'小票流水号:33333333333333333')


        self.headLayout.addWidget(self.goodsNoLabel)
        self.headLayout.addWidget(self.goodsNoInput)
        self.headLayout.addWidget(QSpacerItem())
        self.headLayout.addWidget(self.operatorLabel)
        self.headLayout.addWidget(self.operatorInput)
        self.headLayout.addWidget(self.orderNoLabel)

        self.horizontalGroupBox.setFixedHeight(50)
        self.horizontalGroupBox.setAlignment(Qt.AlignTop)
        self.horizontalGroupBox.setLayout(self.headLayout)
        return
