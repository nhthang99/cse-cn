import socket
from threading import Thread
from model import Encode, Decode
from PyQt5.QtCore import QObject, pyqtSignal

class PeerClient(QObject):

    message_received = pyqtSignal(str)
    BUFF_SIZE = 4096

    def __init__(self, peer_name_src, host, port):
        super().__init__()
        self.peer_name_src = peer_name_src
        self.host = host
        self.port = port
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.handle_connect_chat()

    def receive_data(self):
        while True:
            data = self.socket_client.recv(self.BUFF_SIZE).decode("utf8")
            msg_decode = Decode.decode_message(data)
            if msg_decode:
                username = msg_decode[0]
                content = msg_decode[1]
                self.message_received.emit(username + ': ' + content)
            file_name = Decode.decode_file_name(data)
            if file_name:
                # with open(file_name, 'wb') as f:
                #     while True:
                #         data = self.socket_client.recv(self.BUFF_SIZE * 5)
                #         # end_file = Decode.decode_file_name(data)
                #         if not data:
                #             break
                #         f.write(data)
                file_size = self.socket_client.recv(32).decode("utf8")
                file_size = int(file_size)
                file_to_write = open(file_name, 'wb')
                chunksize = 10240
                while file_size > 0:
                    if file_size < chunksize:
                        chunksize = file_size
                    data = self.socket_client.recv(chunksize)
                    file_to_write.write(data)
                    file_size -= len(data)
                file_to_write.close()
                        

    def handle_connect_chat(self):
        try:
            self.socket_client.connect((self.host, self.port))
            info = Encode.encode_start_session(self.peer_name_src)
            self.socket_client.send(bytes(info, "utf8"))
            Thread(target=self.receive_data).start()
        except socket.error:
            print(str(socket.error))
