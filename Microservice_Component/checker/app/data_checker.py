import random
import socket
import sys
import json
from math import radians,sin,cos,asin,sqrt
import requests
import csv
import time

csvfile=open(str(time.time())+'- Checker.csv', 'w')
fieldnames = ['id', 'msgtime', 'systime']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Connect the socket to the port where the server is listening
# server_address = ('localhost', 4000)
# print >>sys.stderr, 'connecting to %s port %s' % server_address
# sock.connect(server_address)

#data=json.loads('{"lat": 7.217592304415584, "sname": "Ship0.284266547671", "lon": 80.08063450635785}')

def haversine(lon1, lat1, lon2, lat2):
    # haversine formula
    dlon = radians(radians(lon2) - radians(lon1))
    dlat = radians(radians(lat2) - radians(lat1))
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371 * 1000  # get as meters
    return c * r

def check(data):
    url = "http://localhost:5005"
    dist=haversine(80.08063450635785,7.217592304415584,data["lon"],data["lat"])
    writer.writerow({'id': data["id"], 'msgtime': data["msgtime"], 'systime': time.time()})
    csvfile.flush()
    data["msgtime"] = time.time()
    if(dist>100):
        print json.dumps(data)
        requests.post(url, json=data)
