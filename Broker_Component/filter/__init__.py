import json
import pika

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

    channel.basic_publish(exchange='',
                          routing_key='datachecker',
                          body=json.dumps(alert))