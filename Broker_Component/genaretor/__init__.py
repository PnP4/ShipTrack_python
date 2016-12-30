import time
import json
import random
import pika

import csv


csvfile=open(str(time.time())+'- GEN.csv', 'w')
fieldnames = ['id', 'msgtime', 'systime']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()



connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='datafilter')


def genarator():
    lat=random.uniform(6.9218386,7.2418386)
    lon=random.uniform(79.8562055, 80.5062055)
    sname="Ship"+str(random.random())

    alert={}
    alert["lat"]=lat
    alert["lon"] = lon
    alert["sname"] = sname
    alert["time"] = time.time()
    alert["shiptype"] = "Navy"

    print json.dumps(alert)
    writer.writerow({'id': alert["id"], 'msgtime': alert["msgtime"], 'systime': 'None'})
    csvfile.flush()
    channel.basic_publish(exchange='',
              routing_key='datafilter',
              body= json.dumps(alert))