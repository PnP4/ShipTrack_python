import json
import __init__
import os

#data=json.loads('{"lat": 7.217592304415584, "sname": "Ship0.284266547671", "lon": 80.08063450635785, "shiptype": "Navy", "time": 1474300567.82514}')



while True:
    try :
        while True:
            inpath = "/tmp/inpFifo"
            outpath = "/tmp/outFifo"
            try:
                os.mkfifo(inpath)
            except:
                print "file is exsist"
            try:
                os.mkfifo(outpath)
            except:
                print "file is exsist"

            print "Wait for fifo read"
            fifoin = open(inpath, 'r')
            msg = fifoin.read()
            fifoin.close()
            data = json.loads(msg)
            alert={}
            alert["lat"]=data["lat"]
            alert["lon"]=data["lon"]
            alert["sname"]=data["sname"]

            tosend=json.dumps(alert)
            fifoout = open(outpath, 'w')
            fifoout.write(tosend)
            fifoout.close()
            print tosend
    except Exception, e:
        print e