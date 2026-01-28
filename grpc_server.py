from concurrent import futures
import grpc
import user_service_pb2
import user_service_pb2_grpc

HOST = '[::]'
PORT = '50051'
WORKERS = 10


class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        print(f'Получен запрос к методу GetUser от пользователя: {request.username}')
        return user_service_pb2.GetUserResponse(message=f"Привет, {request.username}!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=WORKERS))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    server.add_insecure_port(f'{HOST}:{PORT}')
    server.start()
    print("gRPC сервер запущен на порту 50051...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
