import json
from lib.PnpLib import pnpinput, pnpprint, initPnp

#data=json.loads('{"lat": 7.217592304415584, "sname": "Ship0.284266547671", "lon": 80.08063450635785, "shiptype": "Navy", "time": 1474300567.82514}')



while True:
    try :
        while True:
            initPnp()
            print "Wait for fifo read"
            msg = pnpinput()
            data = json.loads(msg)
            alert={}
            alert["lat"]=data["lat"]
            alert["lon"]=data["lon"]
            alert["sname"]=data["sname"]

            tosend=json.dumps(alert)
            pnpprint(tosend)
            print tosend
    except Exception, e:
        print e