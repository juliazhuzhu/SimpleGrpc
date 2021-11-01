import grpc
from concurrent import futures

from grpc_metadata_test.proto import hello_pb2
from grpc_metadata_test.proto import hello_pb2_grpc


class Greeter(hello_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        for key, value in context.invocation_metadata():
            print('Received meta data key=%s value %s' % (key, value))
        if True:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("not coded.")
            return None
        return hello_pb2.HelloReply(message='Hello, %s' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
