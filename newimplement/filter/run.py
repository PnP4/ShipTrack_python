import json
import __init__

#data=json.loads('{"lat": 7.217592304415584, "sname": "Ship0.284266547671", "lon": 80.08063450635785, "shiptype": "Navy", "time": 1474300567.82514}')



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

                tosend=json.dumps(alert)
                print tosend
                __init__.socket.send(tosend)
    except Exception, e:
        print e