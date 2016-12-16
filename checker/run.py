import json
import __init__

#data=json.loads('{"lat": 7.217592304415584, "sname": "Ship0.284266547671", "lon": 80.08063450635785}')



while(True):
    try:
        while(True):
            data = {} #recived data
            dist=__init__.haversine(80.08063450635785,7.217592304415584,data["lon"],data["lat"])

            if(dist>100):
                #should send data
                print json.dumps(data)

    except Exception, e:
        print e
