from concurrent import futures
import grpc
import location_pb2
import location_pb2_grpc
from location_pb2_grpc import LocationServiceServicer
from kafka import KafkaProducer
import json


kafka_url = "kafka-service:9092"
kafka_topic = "locations"

class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):

        request = {
            'person_id': request.person_id,
            'longitude': request.longitude,
            'latitude': request.latitude
        }

        print('processing request ' + request)
        producer.send(kafka_topic, json.dumps(request, indent=2).encode('utf-8'))

        return location_pb2.Location(**request)


print("Connecting to kafka url: " + kafka_url)
print("Sending kafka topics: " + kafka_topic)

producer = KafkaProducer(bootstrap_servers=kafka_url)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))

location_pb2_grpc.add_LocationServiceServicer_to_server(
    LocationServiceServicer(), server
)

server.add_insecure_port("[::]:5555")
server.start()
server.wait_for_termination()