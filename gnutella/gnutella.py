import json
import socket
import socketserver
import threading
import time
from gnutella.host import Host

class Peer:
    def __init__(self,port):
        self.knownPeers = self.__getPeers(Host('127.0.0.1',str(port)))
        self.connections = []
        self.keywords = []

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client.bind(('0.0.0.0',port))

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('0.0.0.0'))
        
        pingThread = threading.Thread(target=self.Ping)
        pingThread.daemon = True
        pingThread.start()
        self.Pong()
    
    def Ping(self):
        print("Started pinging")
        for peer in self.knownPeers:
            cThread = threading.Thread(target=self.__handshake, args = (peer,))
            cThread.daemon = True
            cThread.start()
        print("Completed pinging")

    def Pong(self):
        self.client.listen(1)
        while True:
            c, a = self.client.accept()
            cThread = threading.Thread(target=self.__PongHandler, args = (c,))
            cThread.daemon = True
            cThread.start()

    def __PongHandler(self,c):
        print("Started Handler")
        while True:
            data = c.recv(1024)
            self.__handleMessage(data)
            if not data:
                break
        print("Stopped Handler")

    def Query(self):
        pass
    
    def QueryHit(self):
        pass

    def __handshake(self,peer):
        try:
            # self.client.connect_ex(peer)
            self.client.sendto(bytes(self.__getKey() + '&00&2','utf-8'),peer)
            while True:
                data = self.client.recv(1024)
                self.__handleMessage(data)
        except:
            pass

    def __handleMessage(self,msg):
        print(str(msg,'utf-8'))

    def __getPeers(self, host: Host) -> list:
        peers = []
        peersTuple = []
        file = open('peers.json')
        data = json.load(file)
        for entry in data:
            peers.append(Host(entry['address'],entry['port']))
        for p in peers:
            if p == host:
                pass
            else:
                peersTuple.append(p.gettuple())
        return peersTuple 

    def __getKey(self) -> str:
        file = open('messagekey.json')
        data = json.load(file)
        return data['key']

    def __updatePeers(self,peer):
        self.connections.append(peer)


# class Client:
#     def __init__(self,address):
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         sock.connect((address,10000))

#         iThread = threading.Thread(target=self.sendMsg, args=(sock,))
#         iThread.daemon = True
#         iThread.start()

#         while True:
#             data = sock.recv(1024)
#             if not data:
#                 break
#             if data[0:1] == b'\x11':
#                 self.updatePeers(data[1:])
#             else:
#                 print(str(data, 'utf-8'))

#     def sendMsg(self,sock):
#         while True:
#             sock.send(bytes(input(""), 'utf-8'))

#     def updatePeers(self, peerData):
#         print(peerData)
#         p2p.peers = str(peerData, 'utf-8').split(',')[:-1]

# class p2p:
#     peers = ['127.0.0.1']
