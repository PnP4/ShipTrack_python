import random
import socket
import sys
import json
import csv
import time

csvfile=open(str(time.time())+'- Viwer.csv', 'w')
fieldnames = ['id', 'msgtime', 'systime']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()



# Create a TCP/IP socket
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
#server_address = ('localhost', 4000)
#print >>sys.stderr, 'connecting to %s port %s' % server_address
#sock.connect(server_address)

def view(data):
    writer.writerow({'id': data["id"], 'msgtime': data["msgtime"], 'systime': time.time()})
    csvfile.flush()
    data["msgtime"] = time.time()
    print json.dump(data)
