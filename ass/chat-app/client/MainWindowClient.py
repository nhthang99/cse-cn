import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QLineEdit
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

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = WindowLogin()
        self.initUI()

    def initUI(self):
        self.ui.setupUi(self)
        self.ui.btnLogin.clicked.connect(self.startLogin)

    def startLogin(self):
        username = self.getUsername()
        host = self.getHost()
        port = self.getPort()
        try:
            self.windowChat = MainWindowChat(username)
            self.client = Client(username, host, port, self.windowChat)
            isExistUsername = self.client.connectToServer()
            if isExistUsername:
                self.dialogChangeUsername()

            self.client.start()
            self.client.change_friend_list.connect(self.windowChat.setupFriendsList)
            self.windowChat.show()
            MainWindowLogin.close(self)
        except:
            self.showMessageBox("Error", "Can't connect to server %s:%d" % (host, port))

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

    def dialogChangeUsername(self):
        new_name, okPressed = QInputDialog.getText(self, "Username in user", "Your username", QLineEdit.Normal, "")
        if okPressed and new_name not in self.client.usernameList:
            self.windowChat.username = new_name
            self.windowChat.ui.txtUsername.setText(new_name)
            port = self.client.generateRandomPort()
            self.client.send_peer_info_to_server(new_name, port)
        else:
            self.showMessageBox("Invalid", "Username in use")
            self.dialogChangeUsername()


    def showMessageBox(self, title, msg):
        return QMessageBox.about(self, title, msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windowLogin = MainWindowLogin()
    windowLogin.show()
    sys.exit(app.exec_())
