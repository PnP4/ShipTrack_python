import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='dataview')

def callback(ch, method, properties, body):
	data = json.loads(body)
	print json.dumps(data)