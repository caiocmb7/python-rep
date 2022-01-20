import grpc
from concurrent import futures
import time
import lampada_pb2
import lampada_pb2_grpc


class LampadaServicer(lampada_pb2_grpc.LampadaServicer):

    def ligarLampada(self, request, context):
        response = lampada_pb2.LampadaStatus()
        print(response)
        response.status = 500
        return response

    def desligarLampada(self, request, context):
        response = lampada_pb2.LampadaStatus()
        print(response)
        response.status = -1
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

lampada_pb2_grpc.add_LampadaServicer_to_server(
    LampadaServicer(), server)

print('Ligando server da lampada na porta: 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
