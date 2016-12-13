import json
from nanomsg import Socket, BUS


socket = Socket(BUS)
socket.connect('tcp://192.168.1.7:5551')