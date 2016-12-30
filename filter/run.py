import json
import __init__
import csv
import time

#data=json.loads('{"lat": 7.217592304415584, "sname": "Ship0.284266547671", "lon": 80.08063450635785, "shiptype": "Navy", "time": 1474300567.82514}')

csvfile=open(str(time.time())+'- Filter.csv', 'w')
fieldnames = ['id', 'msgtime', 'systime']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()


while True:
    try :
        while True:
            data = json.loads(__init__.socket.recv())
            if(data["To"] ==2):
                alert={}
                alert["To"] = 3
                alert["lat"]=data["lat"]
                alert["lon"]=data["lon"]
                alert["sname"]=data["sname"]

                writer.writerow({'id': data["id"], 'msgtime': data["msgtime"], 'systime': time.time()})
                csvfile.flush()

                alert["msgtime"] = time.time()
                tosend=json.dumps(alert)
                print tosend
                __init__.socket.send(tosend)
    except Exception, e:
        print e