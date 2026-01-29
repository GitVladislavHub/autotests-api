from concurrent import futures
import grpc
import course_service_pb2
import course_service_pb2_grpc

HOST = '[::]'
PORT = '50051'
WORKERS = 10


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    def GetCourse(self, request, context):
        print(f"Успешно получен запрос к методу GetCourse от курса: {request.course_id}")
        return course_service_pb2.GetCourseResponse(
            course_id=request.course_id,
            title="Автотесты API",
            description="Будем изучать написание API автотестов"
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=WORKERS))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)
    server.add_insecure_port(f'{HOST}:{PORT}')
    server.start()
    print("gRPC сервер успешно запущен на порту 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()