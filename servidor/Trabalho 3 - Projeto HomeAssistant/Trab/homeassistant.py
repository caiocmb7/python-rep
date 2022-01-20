#!/usr/bin/env python
#!/usr/bin/python
import socket
import threading
import grpc
import json
from concurrent import futures
import pika
import sys
import os
import lampada_pb2
import lampada_pb2_grpc
import ar_pb2
import ar_pb2_grpc
import exaustor_pb2
import exaustor_pb2_grpc

ip = "127.0.0.1"
porta = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((str(ip), int(porta)))
sock.listen(10)
sock.setblocking(False)
clientes = []

# Ar
sensor_ar = []
sensor_ar.append(0)
ar_valor = []
ar_valor.append(0)

# Exaustor
sensor_fumaca = []
sensor_fumaca.append(0)
fumaca_valor = []
fumaca_valor.append(0)

# Lampada
sensor_iluminacao = []
sensor_iluminacao.append(0)
lampada_valor = []
lampada_valor.append(0)

def conexao_global():
    print("####     Método de conexão global iniciado    ####")
    global sensor_iluminacao
    global lampada_valor
    global clientes
    global sock
    while True:
        try:
            exaustor_status = ""
            conn, addr = sock.accept()
            conn.setblocking(False)
            clientes.append(conn)
            valorluminosidade = int(lampada_valor[len(
                lampada_valor)-1]) - int(sensor_iluminacao[len(sensor_iluminacao)-1])

            if int(ar_valor[len(ar_valor)-1]) >= 0 and len(ar_valor) > 1:
                valortemperatura = int(ar_valor[len(ar_valor)-1])
            else:
                valortemperatura = sensor_ar[len(sensor_ar)-1]

            if valorluminosidade < 0:
                valorluminosidade *= -1

            if len(fumaca_valor) > 1:
                if fumaca_valor[len(fumaca_valor)-1] >= 1:
                    exaustor_status = "Ligado"
                else:
                    exaustor_status = "Desligado"
            else:
                if sensor_fumaca[len(sensor_fumaca)-1] >= 1:
                    exaustor_status = "Aberto"
                else:
                    exaustor_status = "Fechado"

            conn.send(('HTTP/1.0 200 OK\n').encode('utf-8'))
            conn.send(('Content-Type: text/html\n').encode('utf-8'))

            conn.send(('\n').encode('utf-8'))
            conn.send(("""
			    <html>
			    <meta charset="utf-8"/>
			        <body>
			            <h1>Sistemas Distríbuidos - Trabalho 3 - RabbitMQ e gRPC </h1>
			            <h3>Nivel de luminosidade (Candela): {}</h3>
			            <h3>Temperatura (C°): {}</h3>
			            <h3>Exaustor: {}</h3>
			            <br><a href="http://localhost:8080/">Modificar Estado</a>
			        </body>
			    </html>
			""").format(valorluminosidade, valortemperatura, exaustor_status).encode('utf-8'))
            # time.sleep(3)
        except:
            pass

def inicializar():
    print("####     Conexões iniciadas     ####")
    global clientes
    while True:
        if len(clientes) > 0:
            for c in clientes:
                try:
                    data = c.recv(1024)
                    teste = data.decode('utf-8')
                    if data:
                        y = json.loads(teste)
                        print(y)
                        processo(y)
                except:
                    pass

def processo(y):
    if int(y['lampada']) == 1:
        comando = 'ligar'
        lampada(comando)
    else:
        comando = 'desligar'
        lampada(comando)
    if int(y['ar']) == 1:
        ar(float(y['temperatura']))
    else:
        ar(0)
    if int(y['exaustor']) > 0:
        exaustor(int(y['exaustor']))
    else:
        exaustor(int(y['exaustor']))

def ar_fila():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='temp_sensor', exchange_type='direct')

    result = channel.queue_declare(queue='temp_sensor', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='temp_sensor', queue=queue_name)

    def callback(ch, method, properties, body):
        temp = int(float(body.decode()))
        global sensor_ar
        sensor_ar.append(temp)

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

def exaustor_fila():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='smoke_sensor', exchange_type='direct')

    result = channel.queue_declare(queue='smoke_sensor', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='smoke_sensor', queue=queue_name)

    def callback(ch, method, properties, body):
        fumaca_state = body.decode()

        global sensor_fumaca
        sensor_fumaca.append(int(fumaca_state))

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

def lampada_fila():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='lum_sensor', exchange_type='direct')

    result = channel.queue_declare(queue='lum_sensor', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='lum_sensor', queue=queue_name)

    def callback(ch, method, properties, body):
        luminosity = int(float(body.decode()))
        global sensor_iluminacao
        sensor_iluminacao.append(luminosity)

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

def ar(comando):
    channel = grpc.insecure_channel('localhost:50052')
    stub = ar_pb2_grpc.ArStub(channel)

    if float(comando) > 0:
        status = ar_pb2.ArTemperatura(temperatura=float(comando))
        response = stub.ligarAr(status)
    else:
        status = ar_pb2.ArTemperatura(temperatura=-1)
        response = stub.desligarAr(status)

    ar_valor.append(response.temperatura)

def exaustor(comando):
    channel = grpc.insecure_channel('localhost:50053')
    stub = exaustor_pb2_grpc.ExaustorStub(channel)

    if float(comando) >= 0:
        status = exaustor_pb2.StatusExaustor(status=float(comando))
        response = stub.ligarExaustor(status)
    else:
        status = exaustor_pb2.StatusExaustor(status=float(comando))
        response = stub.desligarExaustor(status)

    fumaca_valor.append(response.status)

def lampada(comando):
    channel = grpc.insecure_channel('localhost:50051')
    stub = lampada_pb2_grpc.LampadaStub(channel)
    status = lampada_pb2.LampadaStatus(stauts=1)

    if comando == 'desligar':
        response = stub.desligarLampada(status)
    else:
        response = stub.ligarLampada(status)

    lampada_valor.append(response.stauts)

t = threading.Thread(target=lampada_fila)
t.start()

t3 = threading.Thread(target=ar_fila)
t3.start()

t4 = threading.Thread(target=exaustor_fila)
t4.start()

thread_conexao_global = threading.Thread(target=conexao_global)
thread_conexao_global.start()

thread_inicializar = threading.Thread(target=inicializar)
thread_inicializar.start()

while True:
    try:
        comando = input('')

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
            sock.close()
        except SystemExit:
            sock.close()
            os._exit(0)
