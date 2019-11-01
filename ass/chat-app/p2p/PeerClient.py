import socket
from threading import Thread

class PeerClient(Thread):

    BUFF_SIZE = 4096

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.isRunning = False
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket_client.connect((self.host, self.port))
        self.isRunning = True
        print("connect: ", self.isRunning)

    def run(self):
        self.receive()

    def receive(self):
        while self.isRunning:
            data = self.socket_client.recv(self.BUFF_SIZE).decode("utf8")
            print(data)

    def send(self, user, msg):
        print("send", self.socket_client)
        self.socket_client.send(bytes(user + ':'+ msg, "utf8"))

