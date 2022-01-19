import pika
import threading

def Smoke_Sensor_Consumer():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='smoke_sensor',exchange_type='direct')

    result = channel.queue_declare(queue='smoke_sensor', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='smoke_sensor', queue=queue_name)

    print('Smoke Sensor working')

    def callback(ch, method, properties, body):
        print(body)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

def Temp_Sensor_Consumer():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='temp_sensor',exchange_type='direct')

    result = channel.queue_declare(queue='temp_sensor', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='temp_sensor', queue=queue_name)

    print('temp sensor working')

    def callback(ch, method, properties, body):
        print(body)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()



def Lumonisity_Sensor_Consumer():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='lum_sensor',exchange_type='direct')

    result = channel.queue_declare(queue='lum_sensor', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='lum_sensor', queue=queue_name)

    print('lum sensor working')

    def callback(ch, method, properties, body):
        print(body)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


if __name__ == "__main__":
    thread_temp_sensor = threading.Thread(target=Temp_Sensor_Consumer, args=())
    thread_smoke_sensor = threading.Thread(target=Smoke_Sensor_Consumer, args=())
    thread_lum_sensor = threading.Thread(target=Lumonisity_Sensor_Consumer, args=())
    thread_lum_sensor.start()
    thread_smoke_sensor.start()
    thread_temp_sensor.start()
