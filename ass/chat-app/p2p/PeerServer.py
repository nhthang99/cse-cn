import socket
from threading import Thread
<<<<<<< HEAD

=======
import Decode
>>>>>>> 38dba6a2c9ffefea88b22ef3f96d3ba93e80a695
from PyQt5.QtCore import pyqtSignal, QObject

import Decode, Encode


class PeerServer(QObject):
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
        except socket.error as e:
            print(e)

    def listen_peer_incoming(self):
        while self.isRunning:
            (client_socket, (client_addr, client_port)) = self.socket_server.accept()
            info_peer =  client_socket.recv(self.BUFF_SIZE).decode("utf8")
            peer_name_client = Decode.decode_start_session(info_peer)
            print("%s:%s connected"%(client_addr, client_port))
            self.peer_connections[peer_name_client] = client_socket
            # self.receive_data(client_socket)
            Thread(target=self.receive_data, args=(client_socket, )).start()

    def receive_data(self, client_socket):
        while self.isRunning:
            data = client_socket.recv(self.BUFF_SIZE).decode("utf8")
            msg_decode = Decode.decode_message(data)
            if msg_decode:
                username = msg_decode[0]
                content = msg_decode[1]
                self.message_received.emit(username + ': ' + content)

    def send_to_client(self, peer_src, peer_dest, msg):
        if peer_dest in self.peer_connections.keys():
            msg_encode = Encode.encode_message(peer_src, msg)
            self.peer_connections[peer_dest].send(bytes(msg_encode, "utf8"))

    def close(self):
        self.isRunning = False
        for peer in self.peer_connections:
            peer.close()
        self.socket_server.close()

