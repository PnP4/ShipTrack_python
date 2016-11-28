import random
import socket
import sys
import json
import requests

# Create a TCP/IP socket
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
#server_address = ('localhost', 4000)
#print >>sys.stderr, 'connecting to %s port %s' % server_address
#sock.connect(server_address)

#data=json.loads('{"lat": 7.217592304415584, "sname": "Ship0.284266547671", "lon": 80.08063450635785, "shiptype": "Navy", "time": 1474300567.82514}')

def filter(data):
    url = "http://localhost:5004"
    alert={}
    alert["lat"]=data["lat"]
    alert["lon"]=data["lon"]
    alert["sname"]=data["sname"]

    print json.dumps(alert)
    requests.post(url, json=alert)

