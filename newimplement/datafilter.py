import random
import socket
import sys
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
#server_address = ('localhost', 4000)
#print >>sys.stderr, 'connecting to %s port %s' % server_address
#sock.connect(server_address)

data=json.loads('{"lat": 7.217592304415584, "sname": "Ship0.284266547671", "lon": 80.08063450635785, "shiptype": "Navy", "time": 1474300567.82514}')

alert={}
alert["lat"]=data["lat"]
alert["lon"]=data["lon"]
alert["sname"]=data["sname"]

tosend=json.dumps(alert)
print tosend

# while(True):
#     sock.sendall("dfilter&pathchecker^test")
#     try:
#         while(True):
#             data = sock.recv(1024)
#             print >> sys.stderr, 'received "%s"' % data
#
#
#             message = 'dfilter&pathchecker^'
#             #continue
#             body=data.split("^")[1]
#             bodyls=body.split("|")
#             print bodyls
#             for t in range(0,len(bodyls)-3):
#                 message=message+bodyls[t]+"|"
#             message=message+"|"
#             print >>sys.stderr, 'sending "%s"' % message
#             sock.sendall(message)
#
#             '''# Look for the response
#             amount_received = 0
#             amount_expected = len(message)
#
#             while amount_received < amount_expected:
#                 data = sock.recv(16)
#                 amount_received += len(data)
#                 print >>sys.stderr, 'received "%s"' % data'''
#
#     finally:
#         print >>sys.stderr, 'closing socket'
#         #sock.close()