#!/usr/bin/env python3
"""Server for multi-threaded (asynchronous) chat application."""
import socket, sys
from threading import Thread
from model import Decode, Encode


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = server.accept()
        if client:
            socketPeerList.append(client)
            info_peers = Encode.encode_peer_info_list(peerList)
            broadcast(info_peers)
        Thread(target=handle_client, args=(client, client_address)).start()


def handle_client(client,client_address):
    """Handles a single client connection."""

    while True:
        data = client.recv(BUFSIZ).decode("utf8")
        if data:
            username, port = Decode.decode_peer_name(data)
            if not username and not port:
                break
            else:
                host = client_address[0]
                print("%s:%s:%s has connected." % (username, client_address[0], client_address[1]))
                peerList.append([username, host, int(port)])
            print(peerList)



def close(server, socketPeerList):
    server.close()
    for socketPeer in socketPeerList:
        socketPeer.close()


def broadcast(data):
    for peer in socketPeerList:
        peer.send(bytes(data, "utf8"))

        
peerList = []
socketPeerList = []
HOST = '127.0.0.1'
PORT = 8888
BUFSIZ = 4096
ADDR = (HOST, PORT)
isRunning = True


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind(ADDR)
        server.listen(5)
        print("Waiting for connection ...")
        accept_thread = Thread(target=accept_incoming_connections)
        accept_thread.start()
        accept_thread.join()
    except socket.error as e:
        print("Can't start server ...\n")
        print("Caused by: " + str(e))

    sys.exit(close(server, socketPeerList))
