import grpc
import user_service_pb2
import user_service_pb2_grpc

HOST = 'localhost'
PORT = 50051
SERVER_ADDRESS = f'{HOST}:{PORT}'

channel = grpc.insecure_channel(SERVER_ADDRESS)
stub = user_service_pb2_grpc.UserServiceStub(channel)

response = stub.GetUser(user_service_pb2.GetUserRequest(username="Alice"))
print(response)
