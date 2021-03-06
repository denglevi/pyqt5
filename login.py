# encoding=utf-8
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from main import MainWindow
from http_api import HttpAPI
from tools import Tools


class LoginWindow(QDialog):
    def __init__(self, *args):
        QDialog.__init__(self, *args)
        self.setWindowTitle(u'系统登录')
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setFixedSize(300, 150)
        self.initUI()

        self.setStyleSheet('QDialog{background:#E3EFFF;}')

    def initUI(self):

        self.layout = QGridLayout()

        self.logoLabel = QLabel()
        self.logoLabel.setPixmap(QPixmap('images/icon.png'))

        self.usernameInput = QLineEdit()
        self.passwordInput = QLineEdit()

        self.usernameLabel = QLabel(u'用户名')
        self.passwordLabel = QLabel(u'密  码')

        self.usernameInput.setAlignment(Qt.AlignLeft)
        self.usernameInput.setMaxLength(15)
        font = self.usernameInput.font()
        font.setPointSize(font.pointSize() + 5)
        self.usernameInput.setFont(font)

        self.passwordInput.setAlignment(Qt.AlignLeft)
        self.passwordInput.setMaxLength(15)
        self.passwordInput.setEchoMode(QLineEdit.Password)
        font = self.passwordInput.font()
        font.setPointSize(font.pointSize() + 5)
        self.passwordInput.setFont(font)

        self.loginButton = QPushButton(u'登录')
        self.loginButton.setIcon(QIcon('images/icon.png'))

        self.progressBar = QProgressBar()
        self.progressBar.setValue(100)
        self.progressBar.setTextVisible(False)
        self.progressBar.setVisible(False)

        self.layout.addWidget(self.logoLabel, 0, 0, 2, 3)
        self.layout.addWidget(self.usernameLabel, 0, 4, 1, 1)
        self.layout.addWidget(self.usernameInput, 0, 5, 1, 5)
        self.layout.addWidget(self.passwordLabel, 1, 4, 1, 1)
        self.layout.addWidget(self.passwordInput, 1, 5, 1, 5)

        self.layout.addWidget(self.loginButton, 2, 0, 1, 10)
        self.layout.addWidget(self.progressBar, 2, 0, 1, 10)

        self.loginButton.clicked.connect(self.login)

        self.setLayout(self.layout)

    def login(self, args):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        if username == '' or password == '':
            Tools.showMsgDialog(u'用户名或密码不能为空', self)
            return
        self.loginButton.setVisible(False)
        self.progressBar.setVisible(True)
        httpAPI = HttpAPI()
        apiRes = httpAPI.login(username, password)
        if not apiRes[0]:
            Tools.showMsgDialog(apiRes[1], self)
            self.loginButton.setVisible(True)
            self.progressBar.setVisible(False)
            return
        self.close()

        self.mainWindow = MainWindow(apiRes[1])
        self.mainWindow.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = LoginWindow()
    win.show()

    sys.exit(app.exec())
