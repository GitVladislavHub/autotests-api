import grpc
import course_service_pb2
import course_service_pb2_grpc

HOST = 'localhost'
PORT = 50051
SERVER_ADDRESS = f'{HOST}:{PORT}'

channel = grpc.insecure_channel(SERVER_ADDRESS)
stub = course_service_pb2_grpc.CourseServiceStub(channel)

response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="api-course"))
print(response)
