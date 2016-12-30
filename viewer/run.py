import json
import sys
import __init__
import csv
import time

csvfile=open(str(time.time())+'- Viwer.csv', 'w')
fieldnames = ['id', 'msgtime', 'systime']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()


while(True):
    try:
        while(True):
            data = json.loads(__init__.socket.recv())
            writer.writerow({'id': data["id"], 'msgtime': data["msgtime"], 'systime': time.time()})
            csvfile.flush()
            data["msgtime"] = time.time()
            if (data["To"]==4):
                print data

    finally:
        print >>sys.stderr, 'closing socket'
        __init__.sock.close()