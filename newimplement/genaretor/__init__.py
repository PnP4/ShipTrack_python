import random
import json
from nanomsg import Socket, BUS

socket = Socket(BUS)
socket.connect('tcp://127.0.0.1:5551')