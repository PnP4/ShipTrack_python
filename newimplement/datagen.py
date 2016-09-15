import random
import socket
import sys

# Create a TCP/IP socket
import time
import json
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
#server_address = ('localhost', 4000)
#print >>sys.stderr, 'connecting to %s port %s' % server_address
#sock.connect(server_address)

while(True):
    try:
      while(True):
          lat=random.uniform(6.9218386,7.2418386)
          lon=random.uniform(79.8562055, 80.5062055)
          sname="Ship"+str(random.random())
          # Send data
          #message = 'gen&dfilter^'
#          print >>sys.stderr, 'sending "%s"' % message
          alert={}
          alert["lat"]=lat
          alert["lon"] = lon
          alert["sname"] = sname
          alert["time"] = time.time()
          alert["shiptype"] = "Navy"
          message=json.dumps(alert)
          print message
          #sock.sendall(message)
          time.sleep(1)

    finally:
        print >>sys.stderr, 'closing socket'
        #sock.close()