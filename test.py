import sys
import socket
import selectors
import types
import json

def start_connections(peers):
    for i in range(0, len(peers)):
        connid = i + 1
        print(f"Starting connection {connid} to {peers[i]}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(peers[i])
        while True:
            try:
                sock.send(bytes('Test', 'utf-8'))
                data = sock.recv(1024)
                if not data:
                    break
                else:
                    print(data)
            except:
                pass

def getPeers() -> list:
        peersTuple = []
        file = open('peers.json')
        data = json.load(file)
        for entry in data:
            peersTuple.append((str(entry['address']),int(entry['port'])))
        return peersTuple

peers = getPeers()
start_connections(peers)