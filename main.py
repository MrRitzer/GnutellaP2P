from random import randint
import sys
import time
from random import randint

from gnutella.client import Client, p2p
from gnutella.server import Server

while True:
    try:
        print("Trying to connect...")
        time.sleep(randint(1,5))
        for peer in p2p.peers:
            try:
                client = Client(peer)
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                pass

            try:
                server = Server()
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                print("Couldn't start the server...")
            
    except KeyboardInterrupt:
        sys.exit(0)