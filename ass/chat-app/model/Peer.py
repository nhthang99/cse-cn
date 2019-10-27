class Peer:
    
    def __init__(self, username, host, port):
        self.username = username
        self.host = host
        self.port = port

    @property
    def username(self):
        return self.username

    @username.setter
    def username(username):
        self.username = username

    @property
    def host(self):
        return self.host
    
    @host.setter
    def host(host):
        self.host = host
    
    @property
    def port(self):
        return self.port

    @port.setter
    def port(port):
        self.port = port