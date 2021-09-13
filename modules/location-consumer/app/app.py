import psycopg2
from kafka import KafkaConsumer
import os
import json

kafka_url = "kafka-service:9092"
kafka_topic = "locations"

db_username = os.environ["DB_USERNAME"]
db_password = os.environ["DB_PASSWORD"]
db_host = os.environ["DB_HOST"]
db_port = os.environ["DB_PORT"]
db_name = os.environ["DB_NAME"]

kafka_consumer = KafkaConsumer(kafka_topic, bootstrap_servers=kafka_url)


def insert_location_to_db(location):
    db_connection = psycopg2.connect(
        dbname=db_name,
        port=db_port,
        user=db_username,
        password=db_password,
        host=db_host,
    )
    cursor = db_connection.cursor()
    person_id = int(location["person_id"])
    latitude, longitude = int(location["latitude"]), int(location["longitude"])
    sql = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}))".format(
        person_id, latitude, longitude
    )
    cursor.execute(sql)
    db_connection.commit()
    cursor.close()
    db_connection.close()


for location in kafka_consumer:
    print(location)
    message = location.value.decode("utf-8")
    location_json = json.loads(message)
    insert_location_to_db(location_json)
