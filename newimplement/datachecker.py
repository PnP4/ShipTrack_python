import random
import socket
import sys
import json
from math import radians,sin,cos,asin,sqrt
# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Connect the socket to the port where the server is listening
# server_address = ('localhost', 4000)
# print >>sys.stderr, 'connecting to %s port %s' % server_address
# sock.connect(server_address)

data=json.loads('{"lat": 7.217592304415584, "sname": "Ship0.284266547671", "lon": 80.08063450635785}')

def haversine(lon1, lat1, lon2, lat2):
    # haversine formula
    dlon = radians(radians(lon2) - radians(lon1))
    dlat = radians(radians(lat2) - radians(lat1))
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371 * 1000  # get as meters
    return c * r

dist=haversine(80.08063450635785,7.217592304415584,data["lon"],data["lat"])

if(dist>100):
    print json.dumps(data)

# while(True):
#     sock.sendall("pathchecker&mapper^test")
#     try:
#         while(True):
#             data = sock.recv(1024)
#             print >> sys.stderr, 'received "%s"' % data
#
#             body = data.split("^")[1]
#             bodyls = body.split("|")
#
#             message = 'pathchecker&mapper^'
#             if((float(bodyls[0])>7.0) or (float(bodyls[0])>80.2)):
#                 print >>sys.stderr, 'sending "%s"' % message
#                 message=message+"|"+bodyls[0]+"|"+bodyls[1]+"||"
#                 sock.sendall(message)
#
#             '''# Look for the response
#             amount_received = 0
#             amount_expected = len(message)
#
#             while amount_received < amount_expected:
#                 data = sock.recv(16)
#                 amount_received += len(data)
#                 print >>sys.stderr, 'received "%s"' % data'''
#     except Exception,e:
#         print e
#     finally:
#         print >>sys.stderr, 'closing socket'
#         #sock.close()