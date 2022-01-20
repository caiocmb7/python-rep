import grpc
from concurrent import futures
import time
import exaustor_pb2
import exaustor_pb2_grpc


class ExaustorServicer(exaustor_pb2_grpc.ExaustorServicer):

    def ligarExaustor(self, request, context):
        response = exaustor_pb2.StatusExaustor()
        print(response)
        response.status = 1
        return response

    def desligarExaustor(self, request, context):
        response = exaustor_pb2.StatusExaustor()
        print(response)
        response.status = -1
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

exaustor_pb2_grpc.add_ExaustorServicer_to_server(
    ExaustorServicer(), server)

print('Ligando server do exaustor na porta: 50053.')
server.add_insecure_port('[::]:50053')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
