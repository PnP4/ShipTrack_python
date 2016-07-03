import random
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 4000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

while(True):
    sock.sendall("pathchecker&mapper^test")
    try:
        while(True):
            data = sock.recv(1024)
            print >> sys.stderr, 'received "%s"' % data

            body = data.split("^")[1]
            bodyls = body.split("|")

            message = 'pathchecker&mapper^'
            if((float(bodyls[0])>7.0) or (float(bodyls[0])>80.2)):
                print >>sys.stderr, 'sending "%s"' % message
                message=message+"|"+bodyls[0]+"|"+bodyls[1]+"||"
                sock.sendall(message)

            '''# Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                print >>sys.stderr, 'received "%s"' % data'''
    except Exception,e:
        print e
    finally:
        print >>sys.stderr, 'closing socket'
        #sock.close()