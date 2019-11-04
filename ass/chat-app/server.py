#!/usr/bin/env python3
"""Server for multi-threaded (asynchronous) chat application."""
import socket, sys, time
from threading import Thread

sys.path.append('.')

from model import Decode, Encode


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = server.accept()
        if client:
            socketPeerList.append([client])
            info_peers = Encode.encode_peer_info_list(peerList)
            broadcast(info_peers)
        Thread(target=handle_client, args=(client, client_address)).start()


def check_for_connection():
    while True:
        broadcast(Encode.encode_check_alive())
        time.sleep(5)


def handle_client(client,client_address):
    """Handles a single client connection."""

    while True:
        data = client.recv(BUFSIZ).decode("utf8")
        if data:
            username, port = Decode.decode_peer_info(data)
            if not username and not port:
                break
            else:
                host = client_address[0]
                print("%s has connected." % username)
                peerList.append([username, host, int(port)])
                socketPeerList[-1].append(username)
            info_peers = Encode.encode_peer_info_list(peerList)
            broadcast(info_peers)


def close(server, socketPeerList):
    server.close()
    for socketPeer in socketPeerList:
        socketPeer[0].close()


def broadcast(data):
    isAnyPeerDisconnected = False
    for client in socketPeerList:
        try:
            client[0].send(bytes(data, "utf8"))
        except socket.error:
            print(client[1], "is offline")
            for peer in peerList:
                if peer[0] == client[1]:
                    peerList.remove(peer)
                    socketPeerList.remove(client)
            isAnyPeerDisconnected = True
    if isAnyPeerDisconnected:
        info_peers = Encode.encode_peer_info_list(peerList)
        broadcast(info_peers)



def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
        
peerList = []
socketPeerList = []
HOST = get_ip()
PORT = 8888
BUFSIZ = 2048
ADDR = (HOST, PORT)
isRunning = True


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind(ADDR)
        server.listen(5)
        print("Server start with %s:%d" %(HOST, PORT))
        print("Waiting for connection ...")
        accept_thread = Thread(target=accept_incoming_connections)
        # accept_thread.setDaemon(True)
        check_connect_thread = Thread(target=check_for_connection)
        # check_connect_thread.setDaemon(True)
        accept_thread.start()
        check_connect_thread.start()
        accept_thread.join()
        check_connect_thread.join()
    except socket.error as e:
        print("Can't start server ...\n")
        print("Caused by: " + str(e))

    sys.exit(close(server, socketPeerList))
