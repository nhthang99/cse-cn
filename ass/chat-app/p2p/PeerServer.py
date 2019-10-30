from threading import Thread
import socket, sys

class PeerServer(Thread):

    BUFF_SIZE = 4096
    NUM_PEER_LISTEN = 5

    def __init__(self, src_name, dest_name, host, port):
        super().__init__()
        self.src_name = src_name
        self.dest_name = dest_name
        self.host = host
        self.port = port
        self.peer_connections = []
        self.isRunning = True
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def startSocket(self, host, port):
        try:
            self.socket_server.bind((host, port))
            self.socket_server.listen(self.NUM_PEER_LISTEN)
        except socket.error as e:
            print(e)
            self.socket_server.close()
            sys.exit()

    def run(self):
        self.receive_data()

    def accept_incoming_peer(self):
        while self.isRunning:
            (socket_peer, (addr_peer, port_peer)) = self.socket_server.accept()
            self.peer_connections.append([self.dest_name, socket_peer, addr_peer, port_peer])
            Thread(target=self.receive_data, args=(socket_peer,))

    def receive_data(self, socket_peer):
        while self.isRunning:
            data = socket_peer.recv(self.BUFF_SIZE).decode("utf8")
            print(data)

