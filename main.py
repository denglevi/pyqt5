# encoding=utf-8
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time

from member import MemberListDialog
from remark import RemarkDialog

class MainWindow(QWidget):

    def __init__(self, *args):

        QWidget.__init__(self, *args)

        self.initUI()

        self.setWindowTitle(u'收银系统')

    def initUI(self):
        self.createHeader()
        self.createTable()
        self.createFooter()
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.horizontalGroupBox,0,Qt.AlignTop)
        self.mainLayout.addWidget(self.table)
        self.mainLayout.addWidget(self.footer)

        self.setCustomStyle()
        self.setLayout(self.mainLayout)

    def createHeader(self):
        self.horizontalGroupBox = QGroupBox()
        self.headLayout = QHBoxLayout()
        self.goodsNoLabel = QLabel(u'商品编号/条形码')
        self.goodsNoLabel.setFixedWidth(100)
        self.goodsNoLabel.setAlignment(Qt.AlignVCenter|Qt.AlignRight)

        self.goodsNoInput = QLineEdit()
        self.goodsNoInput.setFixedWidth(200)
        self.goodsNoInput.setMaxLength(15)
        font = self.goodsNoInput.font()
        font.setPointSize(font.pointSize() + 5)
        self.goodsNoInput.setFont(font)
        self.goodsNoInput.setFocus()

        self.operatorLabel = QLabel(u'导购员:2222222222')
        self.orderNo = time.strftime('%Y%m%d%H%M%S',time.gmtime())
        self.orderNoLabel = QLabel(u'小票流水号:%s'%self.orderNo)


        self.headLayout.addWidget(self.goodsNoLabel)
        self.headLayout.addWidget(self.goodsNoInput)
        self.headLayout.addStretch()
        self.headLayout.addWidget(self.operatorLabel)
        self.headLayout.addSpacing(10)
        self.headLayout.addWidget(self.orderNoLabel)

        self.horizontalGroupBox.setFixedHeight(50)
        self.horizontalGroupBox.setAlignment(Qt.AlignTop)
        self.horizontalGroupBox.setLayout(self.headLayout)

    def createTable(self):

        self.table = QTableWidget()
        self.table.setColumnCount(17)
        self.table.setHorizontalHeaderLabels(
            [u'',u'编号/条形码',u'品名', u'规格', u'货号', u'单位', u'单价', u'折扣率％', u'折扣价', u'数量', u'金额',u'生产日期',u'保质期',u'到期日期',u'生产批号',u'供应商',u'备注'])
        self.table.setSortingEnabled(True)

    def createFooter(self):

        self.footer = QFrame()
        self.footer.setMinimumHeight(200)
        self.footLayout = QGridLayout()

        self.footerTotal = QFrame()
        self.footerTotalLayout = QGridLayout()
        self.priceNumLabel = QLabel(u'共:1000.00')
        self.goodsNumLabel = QLabel(u'商品数量:10')
        self.goodsDiscountLabel = QLabel(u'折扣:10')

        self.footerTotalLayout.addWidget(self.priceNumLabel,0,0,2,6)
        self.footerTotalLayout.addWidget(self.goodsNumLabel,2,0,1,2)
        self.footerTotalLayout.addWidget(self.goodsDiscountLabel,2,5,-2,2)
        self.footerTotal.setLayout(self.footerTotalLayout)


        self.ysLabel = QLabel(u'应收:')
        self.ysLabel.setFixedWidth(40)
        self.ysLabel.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.skLabel = QLabel(u'收款:')
        self.skLabel.setFixedWidth(40)
        self.skLabel.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.zlLabel = QLabel(u'找零:')
        self.zlLabel.setFixedWidth(40)
        self.zlLabel.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

        self.ysInput = QLineEdit(u'0.00')
        self.ysInput.setFixedWidth(100)
        self.ysInput.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.skInput = QLineEdit(u'0.00')
        self.skInput.setFixedWidth(100)
        self.skInput.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.zlInput = QLineEdit(u'0.00')
        self.zlInput.setFixedWidth(100)
        self.zlInput.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

        self.blankInput = QComboBox()
        self.blankInput.setFixedWidth(100)

        self.discountBtn = QPushButton(u'打折')
        self.finishBtn = QPushButton(u'结算打印')
        self.returnBtn = QPushButton(u'退货')
        self.gdBtn = QPushButton(u'挂单')
        self.qdBtn = QPushButton(u'取单')
        self.sdBtn = QPushButton(u'删单')
        self.remarkBtn = QPushButton(u'备注')
        self.fullScreenBtn = QPushButton(u'全屏')
        self.memberBtn = QPushButton(u'会员管理')
        self.orderBtn = QPushButton(u'订单管理')
        self.orderBtn.setFixedWidth(80)
        self.memberBtn.setFixedWidth(80)

        self.memberNoLabel = QLabel(u'会员卡号:')
        self.memberNoLabel.setFixedWidth(60)
        self.memberNoInput = QLineEdit()
        self.memberNoInput.setFixedWidth(200)
        self.memberName = QLabel(u'姓名:--')

        self.memberScoreLabel = QLabel(u'本次积分:')
        self.memberScoreLabel.setFixedWidth(60)
        self.memberScoreInput = QLineEdit()
        self.memberScoreInput.setFixedWidth(100)
        self.chargeBtn = QPushButton(u'兑换')
        self.chargeBtn.setFixedWidth(80)

        self.footLayout.addWidget(self.footerTotal,0,0,4,8)
        self.footLayout.addWidget(self.ysLabel,0,8,1,1)
        self.footLayout.addWidget(self.skLabel,1,8,1,1)
        self.footLayout.addWidget(self.zlLabel,2,8,1,1)
        self.footLayout.addWidget(self.ysInput,0,9,1,1)
        self.footLayout.addWidget(self.skInput,1,9,1,1)
        self.footLayout.addWidget(self.zlInput,2,9,1,1)
        self.footLayout.addWidget(self.blankInput,0,10,1,1)
        self.footLayout.addWidget(self.discountBtn,1,10,1,1)
        self.footLayout.addWidget(self.finishBtn,3,9,1,1)
        self.footLayout.addWidget(self.returnBtn,3,10,1,1)
        self.footLayout.addWidget(self.gdBtn,4,8,1,1)
        self.footLayout.addWidget(self.qdBtn,4,9,1,1)
        self.footLayout.addWidget(self.sdBtn,4,10,1,1)
        self.footLayout.addWidget(self.remarkBtn,5,10,1,1)
        self.footLayout.addWidget(self.fullScreenBtn,5,9,1,1)
        self.footLayout.addWidget(self.memberBtn,5,7,1,1)
        self.footLayout.addWidget(self.orderBtn,5,8,1,1)
        self.footLayout.addWidget(self.memberNoLabel,4,0,1,1)
        self.footLayout.addWidget(self.memberNoInput,4,1,1,1)
        self.footLayout.addWidget(self.memberScoreLabel,4,2,1,1)
        self.footLayout.addWidget(self.memberScoreInput,4,3,1,1)
        self.footLayout.addWidget(self.chargeBtn,4,4,1,1)
        self.footLayout.addWidget(self.memberName,5,0,1,2)

        self.fullScreenBtn.clicked.connect(self.fullScreen)
        self.memberBtn.clicked.connect(self.showMemberDialog)
        self.remarkBtn.clicked.connect(self.showRemarkDialog)

        self.footer.setLayout(self.footLayout)

    def setCustomStyle(self):
        self.setStyleSheet("QGroupBox {  border: none;}")
        self.table.setStyleSheet('QTableWidget{border:none;}')
        self.footer.setStyleSheet("QFrame{background:#E3EFFF;}")

        self.operatorLabel.setStyleSheet('QLabel{font-size:15px;}')
        self.orderNoLabel.setStyleSheet('QLabel{font-size:15px;}')

        self.footerTotal.setStyleSheet('QFrame{background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0#FC7759, stop: 1 #FFFFFF);}')
        self.priceNumLabel.setStyleSheet('QLabel{background:none;font-size:40px;font-weight:700;}')
        self.goodsNumLabel.setStyleSheet('QLabel{background:none;font-size:20px;}')
        self.goodsDiscountLabel.setStyleSheet('QLabel{background:none;font-size:20px;}')

    def fullScreen(self):

        if self.isFullScreen():
            self.showMaximized()
            self.fullScreenBtn.setText(u'全屏')
        else:
            self.showFullScreen()
            self.fullScreenBtn.setText(u'退出全屏')

    def showMemberDialog(self):

        self.memberListDialog = MemberListDialog(self)

        self.memberListDialog.show()

    def showRemarkDialog(self):

        self.remarkDialog = RemarkDialog(self)
        self.remarkDialog.show()
