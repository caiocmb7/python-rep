import pika
import sys
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='temp_sensor',exchange_type='direct')

while True:
    message = 'QUENTE PRA CARALHOOOOOOO'
    channel.basic_publish(exchange='temp_sensor', routing_key='temp_sensor', body=message)
    print(" [x] Sent %r" % message)
    time.sleep(5)

connection.close()