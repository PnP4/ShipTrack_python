import random
import time
import json
from lib.PnpLib import pnpprint, initPnp

while(True):
    try:
      while(True):
          lat=random.uniform(6.9218386,7.2418386)
          lon=random.uniform(79.8562055, 80.5062055)
          sname="Ship"+str(random.random())
          alert={}
          alert["lat"]=lat
          alert["lon"] = lon
          alert["sname"] = sname
          alert["time"] = time.time()
          alert["shiptype"] = "Navy"
          initPnp()
          tosend=json.dumps(alert)
          pnpprint(tosend)
          print tosend

    except Exception, e:
        print e