import json
import pika
from math import radians,sin,cos,asin,sqrt

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='datachecker')
channel.queue_declare(queue='dataview')

def haversine(lon1, lat1, lon2, lat2):
    # haversine formula
    dlon = radians(radians(lon2) - radians(lon1))
    dlat = radians(radians(lat2) - radians(lat1))
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371 * 1000  # get as meters
    return c * r


def callback(ch, method, properties, body):
    data = json.loads(body)
    dist=haversine(80.08063450635785,7.217592304415584,data["lon"],data["lat"])
    print data
    if(dist>100):
        channel.basic_publish(exchange='',
                              routing_key='dataview',
                              body=json.dumps(data))
