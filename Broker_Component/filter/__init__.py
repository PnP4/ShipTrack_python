import json
import pika
import csv
import time

#data=json.loads('{"lat": 7.217592304415584, "sname": "Ship0.284266547671", "lon": 80.08063450635785, "shiptype": "Navy", "time": 1474300567.82514}')

csvfile=open(str(time.time())+'- Filter.csv', 'w')
fieldnames = ['id', 'msgtime', 'systime']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='datafilter')
channel.queue_declare(queue='datachecker')

def callback(ch, method, properties, body):
    data = json.loads(body)
    alert={}
    alert["lat"]=data["lat"]
    alert["lon"]=data["lon"]
    alert["sname"]=data["sname"]

    print data
    writer.writerow({'id': data["id"], 'msgtime': data["msgtime"], 'systime': time.time()})
    csvfile.flush()

    alert["msgtime"] = time.time()
    channel.basic_publish(exchange='',
                          routing_key='datachecker',
                          body=json.dumps(alert))