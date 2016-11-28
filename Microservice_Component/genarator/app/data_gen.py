import random
import socket
import sys
import time
import json
import requests
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
#server_address = ('localhost', 4000)
#print >>sys.stderr, 'connecting to %s port %s' % server_address
#sock.connect(server_address)

def genarat():
    url = "http://localhost:5003"
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
    requests.post(url, json=alert)