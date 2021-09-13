import grpc
import location_pb2
import location_pb2_grpc

channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

location1 = location_pb2.LocationMessage(
    person_id=50,
    latitude=300,
    longitude=100
)

location2 = location_pb2.LocationMessage(
    person_id=51,
    latitude=100,
    longitude=200
)

response1 = stub.Create(location1)
response2 = stub.Create(location2)
