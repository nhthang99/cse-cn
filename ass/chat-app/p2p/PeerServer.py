from threading import Thread
from model import Decode
from PyQt5.QtCore import pyqtSignal
import socket


class PeerServer:
    message_received = pyqtSignal(str)
    BUFF_SIZE = 4096
    NUM_PEER_LISTEN = 5

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = int(port)
        self.socket_server = None
        self.peer_connections = {}
        self.isRunning = True
        self.startSocket()

    def startSocket(self):
        if self.socket_server:
            self.socket_server.close()
            self.socket_server = None
            self.isRunning = False

        try:
            self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket_server.bind((self.host, self.port))
            self.socket_server.listen(self.NUM_PEER_LISTEN)
            self.isRunning = True
            Thread(target=self.listen_peer_incoming).start()
            # self.listen_peer_incoming()
        except socket.error as e:
            print(e)

    def listen_peer_incoming(self):
        while self.isRunning:
            (client_socket, (client_addr, client_port)) = self.socket_server.accept()
            info_peer =  client_socket.recv(self.BUFF_SIZE).decode("utf8")
            peer_name_client = Decode.decode_start_session(info_peer)
            print("%s:%s connected"%(client_addr, client_port))
            self.peer_connections[peer_name_client] = client_socket
            print(self.peer_connections)
            self.receive_data(client_socket)
            # Thread(target=self.receive_data, args=(client_socket,)).start()

    def receive_data(self, client_socket):
        while True:
            data = client_socket.recv(self.BUFF_SIZE).decode("utf8")
            print(data)
            # self.message_received.emit(data)


    def close(self):
        self.isRunning = False
        for peer in self.peer_connections:
            peer.close()
        self.socket_server.close()

