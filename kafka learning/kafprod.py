import time
import random_data_generator as r
import json

from confluent_kafka import Producer

# Kafka broker configuration
kafka_config = {
    'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka broker(s)
}

# Create a Kafka producer instance
producer = Producer(kafka_config)

# Function to deliver messages asynchronously to the Kafka topic
def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Initialize an empty list to store stock market data

var=True
while var:
    stock_data=r.data_gen()
    print(f"stock-data:   {stock_data}")

    # Produce the data to the Kafka topic
    producer.produce('stock_data_topic2', value=json.dumps(stock_data), callback=delivery_report)

    # Wait for one second
    time.sleep(10)
    # var=False

# Flush any outstanding messages and close the producer
producer.flush()
# producer.close()
