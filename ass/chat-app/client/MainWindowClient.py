import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QLineEdit
from PyQt5.QtGui import QPixmap, QStandardItem, QStandardItemModel

from gui.ClientGUI import Ui_MainWindow as WindowChat
from gui.LoginGUI import Ui_MainWindow as WindowLogin
from client.Client import Client
from model import emoji


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
        self.ui.etxtMessage.returnPressed.connect(self.setMessage)

    def setMessage(self):
        msg = self.ui.etxtMessage.text()
        self.ui.btnSend.setText(emoji.replace(msg))

    def changeAvatar(self, avatar):
        avatar = QPixmap(avatar)
        self.ui.ivAvatar.setPixmap(avatar)

    def getUsername(self):
        return self.ui.txtUsername.text()

    def setupFriendsList(self, friendsList):
        model = QStandardItemModel()
        self.ui.lvFriend.setModel(model)
        if self.getUsername() in friendsList:
            friendsList.remove(self.getUsername())
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

            # Username is empty or somethings
            isConnectionFail = self.client.connectToServer()
            if isConnectionFail:
                self.dialogChangeUsername()
            else:
                self.windowChat.setupFriendsList(self.client.usernameList)
            # Track changeing Friend List
            # self.client.usernameList.remove(self.getUsername())
            self.client.change_friend_list.connect(self.windowChat.setupFriendsList)
            self.client.start()
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
            self.windowChat.setupFriendsList(self.client.usernameList)
            port = self.client.generateRandomPort()
            self.client.send_peer_info_to_server(new_name, port)
        else:
            self.showMessageBox("Invalid", "Username in use")
            self.dialogChangeUsername()
        return new_name


    def showMessageBox(self, title, msg):
        return QMessageBox.about(self, title, msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windowLogin = MainWindowLogin()
    windowLogin.show()
    sys.exit(app.exec_())
