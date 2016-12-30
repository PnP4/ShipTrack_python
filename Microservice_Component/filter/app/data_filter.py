import random
import socket
import sys
import json
import requests
import csv
import time

# Create a TCP/IP socket
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
#server_address = ('localhost', 4000)
#print >>sys.stderr, 'connecting to %s port %s' % server_address
#sock.connect(server_address)

#data=json.loads('{"lat": 7.217592304415584, "sname": "Ship0.284266547671", "lon": 80.08063450635785, "shiptype": "Navy", "time": 1474300567.82514}')
csvfile=open(str(time.time())+'- Filter.csv', 'w')
fieldnames = ['id', 'msgtime', 'systime']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

def filter(data):
    url = "http://localhost:5004"
    alert={}
    alert["lat"]=data["lat"]
    alert["lon"]=data["lon"]
    alert["sname"]=data["sname"]
    writer.writerow({'id': data["id"], 'msgtime': data["msgtime"], 'systime': time.time()})
    csvfile.flush()
    alert["msgtime"] = time.time()

    print json.dumps(alert)
    requests.post(url, json=alert)

