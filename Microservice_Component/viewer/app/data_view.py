import random
import socket
import sys
import json

# Create a TCP/IP socket
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
#server_address = ('localhost', 4000)
#print >>sys.stderr, 'connecting to %s port %s' % server_address
#sock.connect(server_address)

def view(data):
    print json.dump(data)
