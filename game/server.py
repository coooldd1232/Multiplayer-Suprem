import socket
import threading
import pickle

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 9999))

players = {}

def receive():
    while True:
        try:
            data, addr = server.recvfrom(1024)

            if addr not in clients:
                clients.append(addr)
                players[addr] = None
                print("HAPPENING ONCE")

            decodedData = pickle.loads(data)
            if decodedData:
                clientPlayer = decodedData
                players[addr] = clientPlayer
        except():
            pass

def send():
    while True:
        for client in clients:
            server.sendto(pickle.dumps(players), client)


tReceive = threading.Thread(target=receive)
tReceive.start()

tSend = threading.Thread(target=send)
tSend.start()