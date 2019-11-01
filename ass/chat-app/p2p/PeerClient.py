import socket
from threading import Thread
from model import Encode

class PeerClient:

    BUFF_SIZE = 4096

    def __init__(self, peer_name, host, port):
        super().__init__()
        self.peer_name = peer_name
        self.host = host
        self.port = port
        self.isRunning = False
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # def connect(self):
    #     self.socket_client.connect((self.host, self.port))
    #     self.isRunning = True
    #     print("connect: ", self.isRunning)
    #
    # def run(self):
    #     self.receive()
    #
    # def receive(self):
    #     while self.isRunning:
    #         data = self.socket_client.recv(self.BUFF_SIZE).decode("utf8")
    #         print(data)
    #
    # def send(self, user, msg):
    #     print("send", self.socket_client)
    #     self.socket_client.send(bytes(user + ':'+ msg, "utf8"))

    def handle_connect_chat(self):
        try:
            self.socket_client.connect((self.host, self.port))
            info = Encode.encode_start_session(self.peer_name)
            self.send_to_peer(info)
            print(info)
            # Thread(target=self.receive_data, args=(client_socket,)).start()
        except socket.error:
            print(str(socket.error))

    def send_to_peer(self, msg):
        self.socket_client.send(bytes(msg, "utf8"))

