import socket

from gui.ClientGUI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PyQt5.QtCore import QModelIndex, Qt

from p2p.PeerServer import PeerServer
from model import emoji

class WindowChat(QMainWindow):

    def __init__(self, username):
        super(WindowChat, self).__init__()
        self.username = username
        self.isRunning = False
        self.peer_socket = None
        self.peerList = []
        self.ui = Ui_MainWindow()
        self.model = QStandardItemModel()
        self.initUI()

    def initUI(self):
        self.ui.setupUi(self)
        self.ui.lvFriend.setModel(self.model)
        # Setup event
        self.ui.txtUsername.setText(self.username)
        self.ui.btnSend.clicked.connect(self.createSocketServer)
        self.ui.etxtMessage.returnPressed.connect(self.sendMessage)
        self.ui.lvFriend.doubleClicked[QModelIndex].connect(self.setupChat)

    def createSocketServer(self, host, port):
        self.peer_socket = PeerServer(host, port)

    def setupChat(self, index):
        item = self.model.itemFromIndex(index)
        peer_name = item.text()
        for peer in self.peerList:
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
        if friendsList:
            self.model.clear()
            self.peerList = friendsList
            print(friendsList)
            for friend in friendsList:
                if friend[0] != self.getUsername():
                    self.model.appendRow(QStandardItem(friend[0]))
                elif not self.isRunning:
                    self.isRunning = True
                    self.createSocketServer(friend[1], friend[2])
