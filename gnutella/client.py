import socket
import threading

class Client:
    def __init__(self,address):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((address,10000))

        iThread = threading.Thread(target=self.sendMsg, args=(sock,))
        iThread.daemon = True
        iThread.start()

        while True:
            data = sock.recv(1024)
            if not data:
                break
            if data[0:1] == b'\x11':
                print(str(data[1:], 'utf-8'))
                self.updatePeers(data[1:])
            else:
                print(str(data, 'utf-8'))

    def sendMsg(self,sock):
        while True:
            sock.send(bytes(input(""), 'utf-8'))

    def updatePeers(self, peerData):
        p2p.peers = str(peerData, 'utf-8').split(',')[:-1]

class p2p:
    peers = ['127.0.0.1']
