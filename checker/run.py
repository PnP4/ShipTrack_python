import json
import __init__
import csv
import time

csvfile=open(str(time.time())+'- Checker.csv', 'w')
fieldnames = ['id', 'msgtime', 'systime']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()


#data=json.loads('{"lat": 7.217592304415584, "sname": "Ship0.284266547671", "lon": 80.08063450635785}')



while(True):
    try:
        while(True):
            data = json.loads(__init__.socket.recv())
            writer.writerow({'id': data["id"], 'msgtime': data["msgtime"], 'systime': time.time()})
            csvfile.flush()
            data["msgtime"] = time.time()
            if (data["To"] == 3):
                dist=__init__.haversine(80.08063450635785,7.217592304415584,data["lon"],data["lat"])

                if(dist>100):
                    data["To"] = 4
                    __init__.socket.send(json.dumps(data))
                    print json.dumps(data)

    except Exception, e:
        print e
