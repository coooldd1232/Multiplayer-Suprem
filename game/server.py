import socket
import threading
import pickle
import time

# list holding connections
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 9999))

players = {}

def receive():
    while True:
        try:
            data, addr = server.recvfrom(1024)
            
            # if its a new person sending to server
            if addr not in clients:
                clients.append(addr)
                print(f"client {addr} joined")
                players[addr] = None

            playerClass = pickle.loads(data)

            # checking if client sent their player class to server
            if playerClass is not None:
                players[addr] = playerClass
        except:
            pass

def send():
    while True:
        #try:
        for client in clients:
            server.sendto(pickle.dumps(players), client)
        #except:
            #clients.remove(client)


tReceive = threading.Thread(target=receive)
tReceive.start()

tSend = threading.Thread(target=send)
tSend.start()