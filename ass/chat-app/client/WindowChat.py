from threading import Thread

from gui.ClientGUI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QStackedWidget, QListWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PyQt5.QtCore import QModelIndex, Qt

from p2p.PeerServer import PeerServer
from p2p.PeerClient import PeerClient
from model import emoji

class WindowChat(QMainWindow):

    def __init__(self, username):
        super(WindowChat, self).__init__()
        self.username = username
        self.isRunning = False
        self.peer_server = None
        self.peer_client = None
        self.isServer = False
        self.curr_peer_chat = None
        self.peerList = []
        self.peer_chatting = {}
        self.ui = Ui_MainWindow()
        # self.modelFriend = QStandardItemModel()
        self.stackMessages = QStackedWidget()
        self.initUI()

    def initUI(self):
        self.ui.setupUi(self)
        # self.ui.lvFriend.setModel(self.modelFriend)
        # self.ui.lvFriend.curr
        self.ui.btnSend.setDisabled(True)
        # Setup event
        self.ui.txtUsername.setText(self.username)
        self.ui.btnSend.clicked.connect(self.sendMessage)
        self.ui.etxtMessage.returnPressed.connect(self.sendMessage)
        self.ui.lvFriend.itemSelectionChanged.connect(self.setupChat)

    def createSocketServer(self, host, port):
        self.peer_server = PeerServer(host, port)
        self.peer_server.message_received.connect(self.updateMessage)

    def createListViewShowMessage(self):
        listViewMessage = QListWidget()
        listViewMessage.insertItems(["hello", "haha", "hihi"])

    def setupChat(self):
        self.isServer = False
        self.ui.btnSend.setEnabled(True)
        peer_name = self.ui.lvFriend.selectedItems()[0].text()
        for peer in self.peerList:
            if peer[0] == peer_name:
                if peer_name in self.peer_server.peer_connections.keys():
                    self.isServer = True
                    self.curr_peer_chat = peer_name
                else:
                    if peer_name not in self.peer_chatting.keys():
                        self.peer_client = PeerClient(self.username, peer[1], int(peer[2]))
                        self.peer_chatting[peer[0]] = self.peer_client.socket_client
                        self.peer_client.message_received.connect(self.updateMessage)
                    self.curr_peer_chat = peer_name

    def createClientSocket(self, username, host, port):
        self.peer_client = PeerClient(username, host, int(port))
        self.peer_client.message_received.connect(self.updateMessage)

    def sendMessage(self):
        msg = emoji.replace(self.ui.etxtMessage.text())
        self.ui.etxtMessage.clear()
        self.updateMessage('\t\t\t\tMe: ' + msg)
        if self.isServer:
            self.peer_server.send_to_client(self.curr_peer_chat, msg)
        else:
            socket_client = self.peer_chatting[self.curr_peer_chat]
            socket_client.send(bytes(msg, "utf8"))


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
            # self.modelFriend.clear()
            self.ui.lvFriend.clear()
            self.peerList = friendsList
            for friend in friendsList:
                if friend[0] != self.getUsername():
                    # self.modelFriend.appendRow(QStandardItem(friend[0]))
                    self.ui.lvFriend.addItem(friend[0])
                elif not self.isRunning:
                    self.isRunning = True
                    self.createSocketServer(friend[1], int(friend[2]))

    def updateMessage(self, msg):
        self.ui.lvBodyMessage.addItem(msg)

