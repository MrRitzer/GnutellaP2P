from gnutella.gnutella import Peer
import sys

try:
    Peer(int(sys.argv[1]))
except KeyboardInterrupt:
    sys.exit(0)

# import sys

# from gnutella.client import Client, p2p
# from gnutella.server import Server

# while True:
#     try:
#         print("Trying to connect...")
#         for peer in p2p.peers:
#             try:
#                 client = Client(peer)
#             except KeyboardInterrupt:
#                 sys.exit(0)
#             except:
#                 pass
#             try:
#                 server = Server()
#             except KeyboardInterrupt:
#                 sys.exit(0)
#             except:
#                 print("Couldn't start the server...")
            
#     except KeyboardInterrupt:
#         sys.exit(0)