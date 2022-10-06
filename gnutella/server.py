# import socket
# import threading

# class Server:
#     connections = []
#     peers = []
#     def __init__(self):
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         sock.bind(('0.0.0.0',10000))
#         sock.listen(1)
#         print("Server running...")
#         while True:
#             c, a = sock.accept()
#             cThread = threading.Thread(target=self.handler, args = (c,a))
#             cThread.daemon = True
#             cThread.start()
#             self.connections.append(c)
#             self.peers.append(a[0])
#             print(str(a[0]) + ":" + str(a[1]), "connected")
#             self.sendPeers()
    
#     def handler(self, c, a):
#         while True:
#             data = c.recv(1024)
#             for connection in self.connections:
#                 connection.send(data)
#             if not data:
#                 print(str(a[0]) + ":" + str(a[1]), "disconnected")
#                 self.connections.remove(c)
#                 self.peers.remove(a[0])
#                 self.sendPeers()
#                 break

#     def sendPeers(self):
#         p = ""
#         for peer in self.peers:
#             p = p + peer + ","
        
#         for connection in self.connections:
#             connection.send(b'\x11' + bytes(p, 'utf-8'))