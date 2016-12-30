import pika
import json
import csv
import time

csvfile=open(str(time.time())+'- Viwer.csv', 'w')
fieldnames = ['id', 'msgtime', 'systime']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='dataview')

def callback(ch, method, properties, body):
	data = json.loads(body)
	writer.writerow({'id': data["id"], 'msgtime': data["msgtime"], 'systime': time.time()})
	csvfile.flush()
	data["msgtime"] = time.time()
	print json.dumps(data)