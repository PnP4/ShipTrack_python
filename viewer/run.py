import json
import sys
import __init__


while(True):
    try:
        while(True):
            data = json.loads(__init__.socket.recv())
            if (data["To"]==4):
                print data

    finally:
        print >>sys.stderr, 'closing socket'
        __init__.sock.close()