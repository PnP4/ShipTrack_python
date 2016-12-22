import json
from lib.PnpLib import pnpinput, initPnp

while(True):
    try:
        while(True):
            initPnp()
            print "Wait for fifo read"
            msg = pnpinput()
            data = json.loads(msg)
            print data

    except Exception, e:
        print e