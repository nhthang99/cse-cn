import socket
import threading
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ServerGUI import Ui_Server
from Message import MessageModel

class MainWindow(QMainWindow):

    server = None
    messageList = []

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.setupEvent()
        self.model = MessageModel()
        self.ui.listMessage.setModel(self.model)

    def initUI(self):
        self.ui = Ui_Server()
        self.ui.setupUi(self)

    def setupEvent(self):
        self.ui.btnStartServer.clicked.connect(self.startServer)
        self.ui.btnStopServer.clicked.connect(self.cancelServer)
    
    def startServer(self):
        host = self.getHost()
        port = self.getPort()
        server = Server(host, port)
        self.updateMessage(server.messageList[-1])
        self.ui.btnStartServer.setDisabled(True)
        self.ui.btnStopServer.setEnabled(True)

    def getHost(self):
        host = self.ui.edtHost.text()
        self.ui.edtHost.setReadOnly(True)
        return host
    
    def getPort(self):
        port = self.ui.edtPort.text()
        self.ui.edtPort.setReadOnly(True)
        return int(port)

    def cancelServer(self):
        host = self.getHost()
        port = self.getPort()
        Server.s.close()
        self.updateMessage("SERVER DISCONNECTED: {} {}".format(host, port))
        self.ui.btnStartServer.setEnabled(True)
        self.ui.btnStopServer.setDisabled(True)
        self.ui.edtHost.setReadOnly(False)
        self.ui.edtPort.setReadOnly(False)

    
    def updateMessage(self, message):
        if message:
            self.model.messages.append((False, message))
            self.model.layoutChanged.emit()

class Server:

    s = socket.socket()
    QUEUE_SIZE = 10
    BUFFER_SIZE = 2048
    messageList = []

    def __init__(self, host, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((host, port))
            self.messageList.append(str("BINDING SUCCESS: {} {}".format(host, port)))
        except:
            self.messageList.append(str("BINDING FAILED: {} {}".format(host, port)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec_())