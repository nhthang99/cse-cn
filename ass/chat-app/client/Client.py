import socket
from random import randint
from threading import Thread


class Client:

    RECV_SIZE = 1024

    def __init__(self, username='Unknown', host='127.0.0.1', port=8888):
        self.host = host
        self.port = port
        self.username = username
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connectToServer(self):
        self.client_socket.connect((self.host, self.port))
        self.client_socket.send(bytes('<p>' + self.username + ':' + str(self.generateRandomPort()) + '</p>', "utf8"))
        Thread(target=self.receive())

    def receive(self):
        while True:
            data = self.client_socket.recv(self.RECV_SIZE).decode("utf8")
            print(data)

    def generateRandomPort(self):
        port = randint(10000, 12000)
        while self.isExistPort(port):
            port = randint(10000, 12000)
        return port


    def isExistPort(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((self.host, port))
            sock.shutdown(2)
            return True
        except:
            return False
