import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QPixmap, QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt, QModelIndex

from gui.ClientGUI import Ui_MainWindow as WindowChat
from gui.LoginGUI import Ui_MainWindow as WindowLogin
from client.Client import Client
from model import emoji


class MainWindowChat(QMainWindow):

    def __init__(self, username, client):
        super(MainWindowChat, self).__init__()
        self.username = username
        self.client = client
        self.initUI()

    def initUI(self):
        self.ui = WindowChat()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        self.ui.lvFriend.setModel(self.model)
        self.ui.txtUsername.setText(self.username)
        self.ui.btnSend.clicked.connect(self.sendMessage)
        self.ui.etxtMessage.returnPressed.connect(self.sendMessage)
        self.ui.lvFriend.doubleClicked[QModelIndex].connect(self.setupChat)

    def setupChat(self, index):
        item = self.model.itemFromIndex(index)
        peer_name = item.text()
        for peer in self.client.peerList:
            if peer[0] == peer_name:
                self.startChatWithPeer()

    def startChatWithPeer(self):
        pass

    def sendMessage(self):
        msg = self.ui.etxtMessage.text()
        self.ui.btnSend.setText(emoji.replace(msg))

    def changeProfileImage(self):
        fileName = QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)")  # Ask for file
        if fileName:  # If the user gives a file
            pixmap = QPixmap(fileName)  # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), Qt.KeepAspectRatio)  # Scale pixmap
            self.ui.ivAvatar.setPixmap(pixmap) # Set the pixmap onto the label
            self.ui.ivAvatar.setAlignment(Qt.AlignCenter)  # Align the label to center

    def getUsername(self):
        return self.ui.txtUsername.text()

    def setupFriendsList(self, friendsList):
        self.model.clear()
        for friend in friendsList:
            if friend != self.getUsername():
                self.model.appendRow(QStandardItem(friend))


class MainWindowLogin(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.client = None
        self.windowChat = None
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
            self.client = Client(username, host, port)
            self.windowChat = MainWindowChat(username, self.client)

            # Username is empty or somethings
            isConnectionFail = self.client.connectToServer()
            if isConnectionFail:
                self.dialogChangeUsername()
            else:
                self.windowChat.setupFriendsList(self.client.usernameList)
        except:
            self.showMessageBox("Error", "Can't connect to server %s:%d" % (host, port))

        # Track changeing Friend List
        self.client.change_friend_list.connect(self.windowChat.setupFriendsList)
        self.client.start()
        self.windowChat.show()
        MainWindowLogin.close(self)

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
