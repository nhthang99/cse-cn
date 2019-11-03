from ClientGUI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QStackedWidget, QListWidget, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from PeerServer import PeerServer
from PeerClient import PeerClient
<<<<<<< HEAD
import Emoji, Encode
=======
import emoji
>>>>>>> 38dba6a2c9ffefea88b22ef3f96d3ba93e80a695

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
        self.stackMessages = QStackedWidget()
        self.initUI()

    def initUI(self):
        self.ui.setupUi(self)
        self.setFixedSize(780, 560)
        # Setup event
        self.ui.txtUsername.setText(self.username)
        self.ui.btnSend.clicked.connect(self.sendMessage)
        self.ui.etxtMessage.returnPressed.connect(self.sendMessage)
        self.ui.lvFriend.itemSelectionChanged.connect(self.setupChat)

    def createSocketServer(self, host, port):
        self.peer_server = PeerServer(host, port)
        self.peer_server.message_received.connect(self.updateMessage)

    def setupChat(self):
        self.isServer = False
<<<<<<< HEAD
        try:
            peer_name = self.ui.lvFriend.selectedItems()[0].text()
        except:
            return
=======
        peer_name = self.ui.lvFriend.selectedItems()[0].text()
>>>>>>> 38dba6a2c9ffefea88b22ef3f96d3ba93e80a695
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

    def sendMessage(self):
        peer_name = self.ui.lvFriend.selectedItems()
        # must select friend before chat
        if peer_name:
<<<<<<< HEAD
            msg = Emoji.replace(self.ui.etxtMessage.text())
=======
            msg = emoji.replace(self.ui.etxtMessage.text())
>>>>>>> 38dba6a2c9ffefea88b22ef3f96d3ba93e80a695
            my_name = self.getUsername()
            self.ui.etxtMessage.clear()
            self.updateMessage('\t\t\t\t' + my_name +': ' + msg)
            if self.isServer:
<<<<<<< HEAD
                self.peer_server.send_to_client(my_name, self.curr_peer_chat, msg)
            else:
                socket_client = self.peer_chatting[self.curr_peer_chat]
                msg_encode = Encode.encode_message(my_name, msg)
                socket_client.send(bytes(msg_encode, "utf8"))
=======
                self.peer_server.send_to_client(self.curr_peer_chat, my_name + ': ' + msg)
            else:
                socket_client = self.peer_chatting[self.curr_peer_chat]
                socket_client.send(bytes(my_name + ': ' + msg, "utf8"))
>>>>>>> 38dba6a2c9ffefea88b22ef3f96d3ba93e80a695
        else:
            self.ui.etxtMessage.clear()
            QMessageBox.about(self, "Warning", "You are talking to yourself. Choose someone to be less alone.")


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
            self.ui.lvFriend.clear()
            self.peerList = friendsList
            for friend in friendsList:
                if friend[0] != self.getUsername():
                    self.ui.lvFriend.addItem(friend[0])
                elif not self.isRunning:
                    self.isRunning = True
                    self.createSocketServer(friend[1], int(friend[2]))
            self.ui.lvFriend.setCurrentRow(0)

    def updateMessage(self, msg):
        self.ui.lvBodyMessage.addItem(msg)

