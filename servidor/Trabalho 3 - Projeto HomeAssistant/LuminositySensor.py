import pika
import sys
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='lum_sensor',exchange_type='direct')

while True:
    message = 'TA ILUMINADO'
    channel.basic_publish(exchange='lum_sensor', routing_key='lum_sensor', body=message)
    print(" [x] Sent %r" % message)
    time.sleep(5)

connection.close()