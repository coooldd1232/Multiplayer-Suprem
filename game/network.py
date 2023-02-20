import socket
import random
import threading
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.clientInfo = ("localhost", random.randint(8000, 9000))
        self.client.bind(self.clientInfo)

        self.tSend = threading.Thread(target=self.send)
        self.tReceive = threading.Thread(target=self.receive)

        self.server = ("localhost", 9999)

        self.latestPlayerClass = []
        self.latestPlayerDictionary = {}

        self.tSend.start()
        self.tReceive.start()

    def send(self):
        while True:
            self.client.sendto(pickle.dumps(self.latestPlayerClass), self.server)

    def receive(self):
        while True:
            serverData, _ = self.client.recvfrom(1024)
            playerDictionary = pickle.loads(serverData)
            self.latestPlayerDictionary = playerDictionary

