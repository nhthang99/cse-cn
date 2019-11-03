import socket
from threading import Thread
<<<<<<< HEAD
import Encode, Decode
=======
import Encode
>>>>>>> 38dba6a2c9ffefea88b22ef3f96d3ba93e80a695
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

    def handle_connect_chat(self):
        try:
            self.socket_client.connect((self.host, self.port))
            info = Encode.encode_start_session(self.peer_name_src)
            self.socket_client.send(bytes(info, "utf8"))
            Thread(target=self.receive_data).start()
        except socket.error:
            print(str(socket.error))
