import random
import socket
import sys

# Create a TCP/IP socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 4000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

while(True):
    try:
      while(True):
          lat=str(random.uniform(6.9218386,7.2418386))
          lon=str(random.uniform(79.8562055, 80.5062055))
          sname="Ship"+str(random.random())
          # Send data
          message = 'gen&dfilter^'
          print >>sys.stderr, 'sending "%s"' % message
          sock.sendall(message+lat+"|"+lon+"|"+sname+"||")
          time.sleep(1)
          '''# Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                print >>sys.stderr, 'received "%s"' % data'''

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()