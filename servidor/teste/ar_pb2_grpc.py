# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ar_pb2 as ar__pb2


class ArStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ligarAr = channel.unary_unary(
            '/Ar/ligarAr',
            request_serializer=ar__pb2.ArTemperatura.SerializeToString,
            response_deserializer=ar__pb2.ArTemperatura.FromString,
        )
        self.desligarAr = channel.unary_unary(
            '/Ar/desligarAr',
            request_serializer=ar__pb2.ArTemperatura.SerializeToString,
            response_deserializer=ar__pb2.ArTemperatura.FromString,
        )


class ArServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ligarAr(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def desligarAr(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ArServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'ligarAr': grpc.unary_unary_rpc_method_handler(
            servicer.ligarAr,
            request_deserializer=ar__pb2.ArTemperatura.FromString,
            response_serializer=ar__pb2.ArTemperatura.SerializeToString,
        ),
        'desligarAr': grpc.unary_unary_rpc_method_handler(
            servicer.desligarAr,
            request_deserializer=ar__pb2.ArTemperatura.FromString,
            response_serializer=ar__pb2.ArTemperatura.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Ar', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class Ar(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ligarAr(request,
                target,
                options=(),
                channel_credentials=None,
                call_credentials=None,
                insecure=False,
                compression=None,
                wait_for_ready=None,
                timeout=None,
                metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ar/ligarAr',
                                             ar__pb2.ArTemperatura.SerializeToString,
                                             ar__pb2.ArTemperatura.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def desligarAr(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ar/desligarAr',
                                             ar__pb2.ArTemperatura.SerializeToString,
                                             ar__pb2.ArTemperatura.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)