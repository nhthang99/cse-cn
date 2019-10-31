import socket, sys
from random import randint
from model import Encode, Decode, Tags
from PyQt5.QtCore import QThread, pyqtSignal


class Client(QThread):
    RECV_SIZE = 4096
    change_friend_list = pyqtSignal(list)

    def __init__(self, username='', host='127.0.0.1', port=8888, parent=None):
        super(Client, self).__init__(parent)
        self.host = host
        self.port = port
        self.username = username
        self.isRunning = True
        self.peerList = []
        self.usernameList = []
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connectToServer(self):
        self.client_socket.connect((self.host, self.port))
        data = self.client_socket.recv(self.RECV_SIZE).decode("utf8")
        peerList = Decode.decode_peer_info_list(data)

        # First peer join in app
        if peerList == [[None, None, None]]:
            self.send_peer_info_to_server(self.username, self.generateRandomPort())
        # App contained multiple people
        else:
            # Check username whether exist or not
            self.usernameList = [peer[0] for peer in peerList]
            if self.username in self.usernameList:
                # Username in user
                return True
            else:
                # Username is valid
                # self.change_friend_list.emit(self.usernameList)
                self.send_peer_info_to_server(self.username, self.generateRandomPort())
                return False

    def run(self):
        # while self.isRunning:
        self.receive()

    def receive(self):
        while self.isRunning:
            try:
                data = self.client_socket.recv(self.RECV_SIZE).decode("utf8")

                self.peerList = Decode.decode_peer_info_list(data)
                self.usernameList = [peer[0] for peer in self.peerList]
                # Track changing List Friend
                self.change_friend_list.emit(self.peerList)
            except socket.error as e:
                print(e)
                self.stop()
                sys.exit()

    def stop(self):
        self.isRunning = False
        self.client_socket.close()

    def send_peer_info_to_server(self, username, port):
        info = Encode.encode_peer_info(username, port)
        self.send_to_server(info)


    def send_to_server(self, msg):
        self.client_socket.send(bytes(msg, "utf8"))

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
