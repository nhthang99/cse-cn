from gui.ClientGUI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PyQt5.QtCore import QModelIndex, Qt

from p2p.PeerServer import PeerServer
from model import emoji

class WindowChat(QMainWindow):

    def __init__(self, username, client):
        super(WindowChat, self).__init__()
        self.username = username
        self.client = client
        self.ui = Ui_MainWindow()
        self.model = QStandardItemModel()
        self.initUI()

    def initUI(self):
        self.ui.setupUi(self)
        self.ui.lvFriend.setModel(self.model)
        self.createSocketServer()
        # Setup event
        self.ui.txtUsername.setText(self.username)
        self.ui.btnSend.clicked.connect(self.sendMessage)
        self.ui.etxtMessage.returnPressed.connect(self.sendMessage)
        self.ui.lvFriend.doubleClicked[QModelIndex].connect(self.setupChat)

    def createSocketServer(self):
        for peer in self.client.peerList:
            peer_name = peer[0]
            peer_host = peer[1]
            peer_port = int(peer[2])
            print(peer_name, self.username)
            if peer_name == self.username:
                print(peer_host, peer_port)
                self.peer_server = PeerServer(peer_host, peer_port)

    def setupChat(self, index):
        item = self.model.itemFromIndex(index)
        peer_name = item.text()
        for peer in self.client.peerList:
            if peer[0] == peer_name:
                pass

    def sendMessage(self):
        msg = self.ui.etxtMessage.text()
        self.ui.btnSend.setText(emoji.replace(msg))

    def changeProfileImage(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)")  # Ask for file
        if fileName:  # If the user gives a file
            pixmap = QPixmap(fileName)  # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.ui.ivAvatar.width(), self.ui.ivAvatar.height(), Qt.KeepAspectRatio)  # Scale pixmap
            self.ui.ivAvatar.setPixmap(pixmap) # Set the pixmap onto the label
            self.ui.ivAvatar.setAlignment(Qt.AlignCenter)  # Align the label to center

    def getUsername(self):
        return self.ui.txtUsername.text()

    def setupFriendsList(self, friendsList):
        self.model.clear()
        for friend in friendsList:
            if friend != self.getUsername():
                self.model.appendRow(QStandardItem(friend))