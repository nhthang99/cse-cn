import sys
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot

from server.Server import Server
from gui.ServerGUI import Ui_Server
from model.MessageModel import MessageModel


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.server = None
        self.initUI()
        self.modelMessage = MessageModel()
        self.modelFriend = MessageModel()
        self.ui.listMessage.setModel(self.modelMessage)
        self.ui.listFriend.setModel(self.modelFriend)
        self.setupEvent()

    def initUI(self):
        self.ui = Ui_Server()
        self.ui.setupUi(self)

    def setupEvent(self):
        self.ui.btnStartServer.clicked.connect(self.startServer)
        self.ui.btnStopServer.clicked.connect(self.stopServer)

    def startServer(self):
        self.ui.btnStartServer.setDisabled(True)
        self.ui.btnStopServer.setEnabled(True)
        host = self.getHost()
        port = self.getPort()
        self.server = Server(host, port)
        msg = self.server.start()
        self.updateMessage(msg)
        self.server.accept_incoming_connection()

    def stopServer(self):
        if self.server:
            host = self.getHost()
            port = self.getPort()
            self.server.stop()
            self.updateMessage("SERVER DISCONNECTED: {} {}".format(host, port))
            self.ui.btnStartServer.setEnabled(True)
            self.ui.btnStopServer.setDisabled(True)
            self.ui.edtHost.setReadOnly(False)
            self.ui.edtPort.setReadOnly(False)

    @pyqtSlot()
    def updateMessage(self, message):
        if message:
            self.modelMessage.messages.append((False, message))
            self.modelMessage.layoutChanged.emit()

    @pyqtSlot()
    def updateFriend(self, friend):
        if friend:
            self.modelFriend.messages.append((False, friend))
            self.modelFriend.layoutChanged.emit()

    def getHost(self):
        host = self.ui.edtHost.text()
        self.ui.edtHost.setReadOnly(True)
        return host

    def getPort(self):
        port = self.ui.edtPort.text()
        self.ui.edtPort.setReadOnly(True)
        return int(port)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
