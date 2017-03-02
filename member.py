# encoding=utf-8
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MemberListDialog(QDialog):

    def __init__(self, *args):

        QDialog.__init__(self, *args)
        self.setWindowTitle(u'会员管理')
        self.setFixedSize(750,400)
        self.setModal(True)
        self.initUI()

    def initUI(self):

        self.mainLayout = QGridLayout()

        self.memberNoLabel = QLabel(u'卡号/姓名/电话:')
        self.memberNoInput = QLineEdit()
        self.memberNoInput.setFixedWidth(150)
        self.memberNoInput.setFocus()

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            [u'',u'卡号',u'姓名', u'类型', u'积分', u'会员折扣', u'开卡日期'])
        self.table.setSortingEnabled(True)

        self.addMemeberBtn = QPushButton(u'新增')
        self.rechargeBtn = QPushButton(u'充值')
        self.exitBtn = QPushButton(u'退出')

        self.mainLayout.addWidget(self.memberNoLabel,0,0,1,1)
        self.mainLayout.addWidget(self.memberNoInput,0,1,1,3)
        self.mainLayout.addWidget(self.table,1,0,4,8)
        self.mainLayout.addWidget(self.addMemeberBtn,5,0,1,1)
        self.mainLayout.addWidget(self.rechargeBtn,5,1,1,1)
        self.mainLayout.addWidget(self.exitBtn,5,7,1,1)

        self.exitBtn.clicked.connect(self.close)
        self.addMemeberBtn.clicked.connect(self.showAddMemberDialog)

        self.setLayout(self.mainLayout)

    def showAddMemberDialog(self):

        self.addMemeberDialog = AddMemberDialog(self)
        self.addMemeberDialog.show()

class AddMemberDialog(QDialog):

    def __init__(self,*args):
        QDialog.__init__(self,*args)

        self.setFixedWidth(400)
        self.setWindowTitle(u'新增会员')
        self.setModal(True)
        self.initUI()

    def initUI(self):

        self.mainLayout = QFormLayout()

        self.memberTypeInput = QComboBox()
        self.memberOpenDateInput = QDateEdit(QDate.currentDate())
        self.memberOpenDateInput.setDisplayFormat('yyyy-MM-dd')
        self.memberOpenDateInput.setCalendarPopup(True)
        self.memberNameInput = QLineEdit()
        self.memberNoInput = QLineEdit()
        self.memberPhoneInput = QLineEdit()
        self.memberBirthdayInput = QDateEdit(QDate.currentDate())
        self.memberBirthdayInput.setDisplayFormat('yyyy-MM-dd')
        self.memberBirthdayInput.setCalendarPopup(True)
        self.memberEmailInput = QLineEdit()
        self.memberRemarkInput = QTextEdit()

        self.statusHBox = QHBoxLayout()
        self.memberStatus1Input = QCheckBox(u'启用')
        self.memberStatus2Input = QCheckBox(u'禁用')
        self.statusHBox.addWidget(self.memberStatus1Input)
        self.statusHBox.addWidget(self.memberStatus2Input)

        self.mainLayout.addRow(u'会员类型',self.memberTypeInput)
        self.mainLayout.addRow(u'开卡日期',self.memberOpenDateInput)
        self.mainLayout.addRow(u'卡号',self.memberNoInput)
        self.mainLayout.addRow(u'姓名',self.memberNameInput)
        self.mainLayout.addRow(u'电话',self.memberPhoneInput)
        self.mainLayout.addRow(u'生日',self.memberBirthdayInput)
        self.mainLayout.addRow(u'邮箱',self.memberEmailInput)
        self.mainLayout.addRow(u'备注',self.memberRemarkInput)
        self.mainLayout.addRow(u'状态',self.statusHBox)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.button(QDialogButtonBox.Ok).setText(u'保存')
        buttonBox.button(QDialogButtonBox.Cancel).setText(u'取消')
        self.mainLayout.addWidget(buttonBox)

        self.setLayout(self.mainLayout)

        buttonBox.accepted.connect(self.saveMember)
        buttonBox.rejected.connect(self.close)

    def saveMember(self):

        self.memberOpenDateInput.text()
        self.close()