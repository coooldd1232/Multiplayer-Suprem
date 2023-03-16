import socket
import random
import threading
import pickle
import time

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.clientConnection = ("127.0.0.1", random.randint(8000, 9000))
        self.client.bind(self.clientConnection)

        self.server = ("localhost", 9999)

        self.latestPlayerClass = None
        self.latestPlayersDictionary = {}

        self.tSend = threading.Thread(target=self.send)
        self.tReceive = threading.Thread(target=self.receive)

        self.tSend.start()
        self.tReceive.start()

    def send(self):
        while True:
            self.client.sendto(pickle.dumps(self.latestPlayerClass), self.server)

    def receive(self):
        while True:
            serverData, _ = self.client.recvfrom(2048)
            playerDictionary = pickle.loads(serverData)
            self.latestPlayersDictionary = playerDictionary

