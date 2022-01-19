import pika
import sys
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='smoke_sensor',exchange_type='direct')

while True:
    message = 'TA PEGANDO FOGO BIXO'
    channel.basic_publish(exchange='smoke_sensor', routing_key='smoke_sensor', body=message)
    print(" [x] Sent %r" % message)
    time.sleep(5)

connection.close()