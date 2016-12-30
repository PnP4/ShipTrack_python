import random
import sys
import time
import json
import __init__
import csv


csvfile=open(str(time.time())+'- GEN.csv', 'w')
fieldnames = ['id', 'msgtime', 'systime']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()


while(True):
    try:
      while(True):
          lat=random.uniform(6.9218386,7.2418386)
          lon=random.uniform(79.8562055, 80.5062055)
          sname="Ship"+str(random.random())
          alert={}
          alert["To"] = 2
          alert["lat"]=lat
          alert["lon"] = lon
          alert["sname"] = sname
          alert["time"] = time.time()

          alert["msgtime"] = time.time()
          alert["id"] = time.time()

          alert["shiptype"] = "Navy"
          message=json.dumps(alert)
          print message
          writer.writerow({'id': alert["id"] , 'msgtime': alert["msgtime"],'systime':'None'})
          csvfile.flush()
          __init__.socket.send(message)

    finally:
        print >>sys.stderr, 'closing socket'
