import json
import __init__
import os

#data=json.loads('{"lat": 7.217592304415584, "sname": "Ship0.284266547671", "lon": 80.08063450635785}')




while(True):
    try:
        while(True):
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
            dist=__init__.haversine(80.08063450635785,7.217592304415584,data["lon"],data["lat"])
            if(dist>100):
                fifoout = open(outpath, 'w')
                fifoout.write(json.dumps(data))
                fifoout.close()
                print json.dumps(data)

    except Exception, e:
        print e
