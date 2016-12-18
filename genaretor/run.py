import random
import sys
import time
import json
#import __init__
import os

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
          alert["shiptype"] = "Navy"
          message=json.dumps(alert)
          outpath = "/tmp/outFifo"
          try:
              os.mkfifo(outpath)
          except:
              print "file is exsist"

          fifoout = open(outpath, 'w')
          fifoout.write(message)
          fifoout.close()
          print message

    finally:
        print >>sys.stderr, 'closing socket'