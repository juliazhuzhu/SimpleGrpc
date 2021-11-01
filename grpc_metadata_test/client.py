import grpc
from grpc_metadata_test.proto import hello_pb2
from grpc_metadata_test.proto import hello_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:

        stub = hello_pb2_grpc.GreeterStub(channel)
        hello_request = hello_pb2.HelloRequest()
        hello_request.name = "xiaoye"
        # hello_request.cast.extend([1, 2])
        # hello_request.cast.append(3)
        try:
            rsp, call = stub.SayHello.with_call(
                hello_request,
                metadata=(
                    ('token', 'asdkfojeadflajdajofioj'),

                ),
                timeout=3)
        except grpc.RpcError as e:
            d = e.details()
            print(d)
            status_code = e.code()
            print(status_code.name)
            print(status_code.value)
            return

        print(rsp.message)
        for key, value in call.trailing_metadata():
            print('%s %s' % (key, value))


if __name__ == "__main__":
    run()
