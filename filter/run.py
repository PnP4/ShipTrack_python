import json
import __init__

#data=json.loads('{"lat": 7.217592304415584, "sname": "Ship0.284266547671", "lon": 80.08063450635785, "shiptype": "Navy", "time": 1474300567.82514}')



while True:
    try :
        while True:
            data = {} #recived data
            alert = filter(data)
            tosend=json.dumps(alert)
            print alert
    except Exception, e:
        print e