import sys, re
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap, QStandardItem, QStandardItemModel

from gui.ClientGUI import Ui_MainWindow as WindowChat
from gui.LoginGUI import Ui_MainWindow as WindowLogin
from client.Client import Client

class MainWindowChat(QMainWindow):

    def __init__(self, username):
        super(MainWindowChat, self).__init__()
        self.username = username
        self.initUI()

    def initUI(self):
        self.ui = WindowChat()
        self.ui.setupUi(self)
        self.ui.txtUsername.setText(self.username)
        self.ui.btnSend.clicked.connect(self.setupSendMessage)

    def changeAvatar(self, avatar):
        avatar = QPixmap(avatar)
        self.ui.ivAvatar.setPixmap(avatar)
    
    def getUsername(self):
        return self.ui.txtUsername.text()

    def setupFriendsList(self, friendsList):
        model = QStandardItemModel()
        self.ui.lvFriend.setModel(model)
        for friend in friendsList:
            model.appendRow(QStandardItem(friend))

    def setupSendMessage(self):
        pass

class MainWindowLogin(QMainWindow):

    def __init__(self):
        super(MainWindowLogin, self).__init__()
        self.initUI()


    def initUI(self):
        self.ui = WindowLogin()
        self.ui.setupUi(self)
        self.ui.btnLogin.clicked.connect(self.startLogin)

    def startLogin(self):
        username = self.getUsername()
        host = self.getHost()
        port = self.getPort()
        try:
            client = Client(username, host, port)
            client.connectToServer()
            self.windowChat = MainWindowChat(username)
            self.windowChat.show()
            MainWindowLogin.close(self)
        except:
            self.showMessageBox("Error", "Can't connect to server %s:%d" %(host, port))

    def getUsername(self):
        username = self.ui.edtUsername.text()
        if username:
            return username
        else:
            self.showMessageBox("Error", "Please enter your username ...\n Try to again")

    def getHost(self):
        host = self.ui.edtHost.text()
        if host:
            return host
        else:
            self.showMessageBox("Error", "Please enter server's host ...\n Try to again")


    def getPort(self):
        port = self.ui.edtPort.text()
        if port:
            return int(port)
        else:
            self.showMessageBox("Error", "Please enter server's port ...\n Try to again")

    def showMessageBox(self, title, msg):
        return QMessageBox.about(self, title, msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    windowLogin = MainWindowLogin()
    windowLogin.show()
    sys.exit(app.exec_())