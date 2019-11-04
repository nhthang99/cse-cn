import socket, os
from threading import Thread
from PyQt5.QtCore import pyqtSignal, QObject

from model import Decode, Encode


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
            data = client_socket.recv(self.BUFF_SIZE).decode("utf8", "ignore")
            print(data)
            msg_decode = Decode.decode_message(data)
            if msg_decode:
                username = msg_decode[0]
                content = msg_decode[1]
                self.message_received.emit(username + ': ' + content)
            file_name = Decode.decode_file_name(data)
            if file_name:
                file_size = client_socket.recv(32)
                file_size = int.from_bytes(file_size, byteorder='big')
                file_to_write = open(file_name, 'wb')
                chunksize = 10240
                while file_size > 0:
                    if file_size < chunksize:
                        chunksize = file_size
                    data = client_socket.recv(chunksize)
                    file_to_write.write(data)
                    file_size -= len(data)
                file_to_write.close()

    def send_message(self, peer_src, peer_dest, msg):
        if peer_dest in self.peer_connections.keys():
            msg_encode = Encode.encode_message(peer_src, msg)
            self.peer_connections[peer_dest].send(bytes(msg_encode, "utf8"))

    def send_file(self, peer_src, peer_dest, file_name, file_path):
        if peer_dest in self.peer_connections.keys():
            file_name_encode = Encode.encode_file_name(file_name)
            peer_socket = self.peer_connections[peer_dest]
            peer_socket.send(bytes(file_name_encode, "utf8"))
            file_size = os.path.getsize(file_path)
            file_size = file_size.to_bytes(32, byteorder='big')
            peer_socket.send(file_size)
            with open(file_path, "rb") as f:
                # data = f.read(2048 * 5)
                # while data:
                #     peer_socket.send(data)
                #     data = f.read(2048 * 5)
                peer_socket.sendfile(f)

    def close(self):
        self.isRunning = False
        for peer in self.peer_connections:
            peer.close()
        self.socket_server.close()

