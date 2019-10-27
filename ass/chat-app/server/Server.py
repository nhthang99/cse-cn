import socket
import threading


class Server(threading.Thread):
    QUEUE_SIZE = 5
    RECV_BUFFER = 1024

    def __init__(self, host='127.0.0.1', port=8888):
        super().__init__()
        self.host = host
        self.port = port
        self.addresses = {}
        self.connections = {}
        self.server_socket = None
        self.isRunning = True

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state,
        # without waiting for its natural timeout to expire
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server_socket.bind((self.host, self.port))
        # lỗi chõ này nè
        self.server_socket.listen(self.QUEUE_SIZE)
     # thread chỗn àny
        # why?
        message = "SERVER CONNECTED: {}:{}".format(self.host, self.port)
        return message

    def stop(self):
        if self.server_socket:
            self.isRunning = False
            self.server_socket.close()

    def accept_incoming_connection(self):
        """ Setting up handling for incoming connections from client sides """
        # while True:
        client_socket, client_address = self.server_socket.accept()
        msg = client_address[0] + ':' + client_address[1] +" CONNECTED"
        print(msg)
        client_socket.send(bytes("CONNECTION HAS ESTABLISHED", "utf8"))
        self.addresses[client_socket] = client_address
        threading.Thread(target=self.handle_client_thread, args=(client_socket,)).start()

    def handle_client_thread(self, client_socket):
        """ Handle a single client connection """
        username = client_socket.recv(self.RECV_BUFFER).decode("utf8")
        self.broadcast(bytes("Welcome " + username, "utf8"))
        self.connections[client_socket] = username
        # while True:
        #     msg = client_socket.recv(self.RECV_BUFFER)
        #     if msg:
        #         self.broadcast(msg)

    def broadcast(self, msg, prefix=""):
        for sock in self.connections:
            sock.send(bytes(prefix, "utf8") + msg)
