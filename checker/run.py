import json
import __init__
import os
from lib.PnpLib import pnpinput, pnpprint, initPnp

#data=json.loads('{"lat": 7.217592304415584, "sname": "Ship0.284266547671", "lon": 80.08063450635785}')


while(True):
    try:
        while(True):
            initPnp()
            print "Wait for fifo read"
            msg = pnpinput()
            data = json.loads(msg)
            dist=__init__.haversine(80.08063450635785,7.217592304415584,data["lon"],data["lat"])
            if(dist>100):
                tosend = json.dumps(data)
                pnpprint(tosend)
                print json.dumps(tosend)

    except Exception, e:
        print e
