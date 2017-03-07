# encoding=utf-8
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time

from remark import RemarkDialog


class ReturnDialog(QDialog):

    returnNumLabel = None
    returnMoneyLabel = None
    memberNameLabel = None

    def __init__(self,*args):

        QDialog.__init__(self,*args)
        self.setWindowTitle(u'商品退货')
        self.setModal(True)
        self.setFixedSize(800, 400)
        self.initUI()

    def initUI(self):

        self.mainLayout = QGridLayout()
        self.orderNo = 'R'+ time.strftime('%Y%m%d%H%M%S', time.gmtime())
        self.returnNoLabel = QLabel(u'退货单号:%s'% self.orderNo)
        self.orderNoLabel = QLabel(u'退货小票:')
        self.orderNoLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.orderNoInput = QLineEdit()
        self.orderNoInput.setFocus()
        self.orderNoInput.setFixedWidth(140)

        self.goodsNoLabel = QLabel(u'编号/条形码:')
        self.goodsNoLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.goodsNoInput = QLineEdit()
        self.goodsNoInput.setFixedWidth(140)

        self.operatorLabel = QLabel(u'导购员:')
        self.operatorLabel.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.operatorInput = QComboBox()
        self.operatorInput.setFixedWidth(80)

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            [u'',u'编号/条形码',u'品名', u'货号', u'规格', u'单位', u'单价'])
        self.table.setSortingEnabled(True)

        self.setReturnNumLabel(10)
        self.setReturnMoneyLabel(10.00)

        self.returnType1 = QCheckBox(u'退储值')
        self.returnType2 = QCheckBox(u'退现金')

        self.returnBtn = QPushButton(u'退货')
        self.returnBtn.setFocus(False)
        self.returnBtn.setAutoDefault(False)
        self.cancelBtn = QPushButton(u'退出')
        self.cancelBtn.setAutoDefault(False)

        self.memberNoLabel = QLabel(u'会员卡号:')
        self.memberNoLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.memberNoInput = QLineEdit()
        self.setMemberName('--')

        self.remarkBtn = QPushButton(u'备注')
        self.remarkBtn.setAutoDefault(False)
        self.memberScoreLabel = QLabel(u'本次积分:')
        self.memberScoreLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # self.memberScoreLabel.setFixedWidth(60)
        self.memberScoreInput = QLineEdit()
        # self.memberScoreInput.setFixedWidth(100)

        self.mainLayout.addWidget(self.returnNoLabel, 0, 0, 1, 4)
        self.mainLayout.addWidget(self.orderNoLabel,0,4,1,1)
        self.mainLayout.addWidget(self.orderNoInput,0,6,1,2)
        self.mainLayout.addWidget(self.goodsNoLabel,0,9,1,1)
        self.mainLayout.addWidget(self.goodsNoInput,0,10,1,2)
        self.mainLayout.addWidget(self.operatorLabel,0,13,1,1)
        self.mainLayout.addWidget(self.operatorInput,0,14,1,1)
        self.mainLayout.addWidget(self.table,1,0,11,15)
        self.mainLayout.addWidget(self.returnNumLabel,12,0,1,2)
        self.mainLayout.addWidget(self.returnMoneyLabel,12,3,1,2)
        self.mainLayout.addWidget(self.returnType1,12,6,1,1)
        self.mainLayout.addWidget(self.returnType2,12,7,1,1)
        self.mainLayout.addWidget(self.returnBtn,12,13,1,1)
        self.mainLayout.addWidget(self.cancelBtn,12,14,1,1)

        self.mainLayout.addWidget(self.memberNoLabel,13,0,1,1)
        self.mainLayout.addWidget(self.memberNoInput,13,1,1,5)
        self.mainLayout.addWidget(self.memberScoreLabel,13,6,1,1)
        self.mainLayout.addWidget(self.memberScoreInput,13,7,1,2)
        self.mainLayout.addWidget(self.remarkBtn,13,14,1,1)

        self.mainLayout.addWidget(self.memberNameLabel,14,0,1,3)


        # self.exitBtn.clicked.connect(self.close)
        # self.addMemeberBtn.clicked.connect(self.showAddMemberDialog)

        self.remarkBtn.clicked.connect(self.showRemarkDialog)

        self.setLayout(self.mainLayout)

    def setReturnNumLabel(self,num):

        if self.returnNumLabel is not None:
            self.returnNumLabel.setText(u'退货数量:%d'%num)
        else:
            self.returnNumLabel = QLabel(u'退货数量:%d' % num)

    def setReturnMoneyLabel(self,money):

        if self.returnMoneyLabel is not None:
            self.returnMoneyLabel.setText(u'退货金额:%f'%money)
        else:
            self.returnMoneyLabel = QLabel(u'退货金额:%.2f' % money)

    def setMemberName(self,name):

        if self.memberNameLabel is not None:
            self.memberNameLabel.setText(u'姓名:%s'% name)
        else:
            self.memberNameLabel = QLabel(u'姓名:%s' % name)

    def showRemarkDialog(self):

        self.remarkDialog = RemarkDialog(self)
        self.remarkDialog.show()


