import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ClientGUI import Ui_MainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def changeAvatar(self, avatar):
        avatar = QPixmap(avatar)
        self.ui.ivAvatar.setPixmap(avatar)

    def setupSendMessage(self):
        message = self.ui.etxtMessage.text()
        pass

    def setupFriendsList(self, friendsList):
        model = QStandardItemModel()
        self.ui.lvFriend.setModel(model)
        for friend in friendsList:
            model.appendRow(QStandardItem(friend))

    def main(self):
        self.ui.btnSend.clicked.connect(self.setupSendMessage)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    friendsList = ['thang', 'khoi', 'nam']*10
    window.setupFriendsList(friendsList)

    window.show()
    sys.exit(app.exec_())