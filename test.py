import sys
import socket
import selectors
import types
import json

sel = selectors.DefaultSelector()
messages = [b"Message 1 from client.", b"Message 2 from client."]

def start_connections(peers):
    for i in range(0, len(peers)):
        connid = i + 1
        print(f"Starting connection {connid} to {peers[i]}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(peers[i])
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(
            connid=connid,
            msg_total=sum(len(m) for m in messages),
            recv_total=0,
            messages=messages.copy(),
            outb=b"",
        )
        sel.register(sock, events, data=data)

def getPeers() -> list:
        peersTuple = []
        file = open('peers.json')
        data = json.load(file)
        for entry in data:
            peersTuple.append((str(entry['address']),int(entry['port'])))
        return peersTuple

peers = getPeers()
start_connections(peers)