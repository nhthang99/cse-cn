#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import re


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client, client_address[0])).start()

def isExistUsername(username):
    if username in clients.keys():
        return True
    else:
        return False

def handle_client(client,client_host):  # Takes client socket as argument.
    """Handles a single client connection."""

    data = client.recv(BUFSIZ).decode("utf8")
    print(data)
    name_format = re.match(r'<p>(.*)</p>', data, re.M | re.I)
    if name_format:
        info = name_format.group()[3:-4].split(':')
        username = info[0]
        port = int(info[1])
        if isExistUsername(username):
            client.send(bytes('<ExistUsername>', "utf8"))
        else:
            welcome = 'Welcome %s:%d! If you ever want to quit, type {quit} to exit.' %(username, port)
            client.send(bytes(welcome, "utf8"))
            clients[username] = (client_host, port)
            print('clients: ', clients)

    else:
        pass

        
clients = {}
addresses = {}

HOST = '127.0.0.1'
PORT = 8888
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
