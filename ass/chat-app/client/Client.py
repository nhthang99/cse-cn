import socket, sys, time
from random import randint
from model import Encode, Decode
from PyQt5.QtCore import QThread, pyqtSignal


class Client(QThread):
    RECV_SIZE = 4096
    change_friend_list = pyqtSignal(list)

    def __init__(self, username='', host='127.0.0.1', port=8888, window_chat=None, parent=None):
        super(Client, self).__init__(parent)
        self.host = host
        self.port = port
        self.username = username
        self.window_chat = window_chat
        self.isRunning = True
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connectToServer(self):
        self.client_socket.connect((self.host, self.port))
        info = Encode.encode_peer_name(self.username, self.generateRandomPort())
        self.client_socket.send(bytes(info, "utf8"))

    def run(self):
        while self.isRunning:
            self.receive()

    def receive(self):
        while self.isRunning:
            try:
                data = self.client_socket.recv(self.RECV_SIZE).decode("utf8")
                peerList = Decode.decode_peer_info_list(data)
                if isinstance(peerList, list):
                    usernameListFriend = [peer[0] for peer in peerList]
                    usernameListFriend.remove(self.username)
                    self.change_friend_list.emit(usernameListFriend)
                    time.sleep(1)

                    # self.window_chat.setupFriendsList(usernameListFriend)
            except socket.error as e:
                print(e)
                self.stop()
                sys.exit()

    def stop(self):
        self.isRunning = False
        self.client_socket.close()

    def generateRandomPort(self):
        port = randint(10000, 12000)
        while self.isExistPort(port):
            port = randint(10000, 12000)
        return port

    def isExistPort(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect((self.host, port))
            sock.shutdown(1)
            return True
        except socket.error:
            return False
        finally:
            return False
