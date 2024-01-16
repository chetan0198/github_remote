from confluent_kafka import Consumer, KafkaError
import json
from pyspark.sql import SparkSession
import pandas as pd

spark=SparkSession.builder.appName('test').getOrCreate()


# Define the Kafka consumer configuration
consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test',
    'auto.offset.reset': 'earliest'  # Set to 'latest' or 'earliest' based on your requirement
}

# Create a Kafka consumer instance
consumer = Consumer(consumer_config)

# Subscribe to the Kafka topic
topic = 'stock_data_topic2'
consumer.subscribe([topic])

# Poll for messages
try:
    while True:
        msg = consumer.poll(1.0)  # Adjust the timeout based on your requirements
        # print(f'msg:- {msg}')

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event, not an error
                continue
            else:
                print(f"Error: {msg.error()}")
                break

        # Process the received message
            
        result=msg.value().decode('utf-8')
        # print(f"Received message: {result}  result before json.loads {type(result)}")
        json_data = [json.loads(result)]

        # print(f"json data:--- {json_data}")
        # print("json_data.get('timestamp')---",json_data.get('timestamp'))
        # print(type(msg),type(msg.value),type(json_data))
        # print('')
        # print('type of message:-',type(msg.value().decode('utf-8')),'message',msg.value().decode('utf-8'))
        # print(json_data,"---json_data",  type(json_data),type(json_data[0]))

        df=spark.createDataFrame(json_data)
        print('pyspark df created')

        # #convert the pyspark df to pandas df and save to specific file
        pandas_df=df.toPandas()
        print('pandas df created')

        # csv_file_path = 'test13/file.csv'
        # df.to_csv(csv_file_path, mode='a', index=False, header=False)
        # print('csv done')

        # print(df.show())
        # print(type(df.collect()))

        # for i in df.collect()[0][0]:
        #     print(i)

        # df.toPandas()
        # print(dfpd.show())

        # dfpd.to_csv('test/test.csv',mode='a',index=False,header=False)

        # for i in json_data[0]
        # print(json_data)

        # df.repartition(1).write \
        # .mode("append") \
        # .csv("dftocsv1")

        # df.coalesce(1).write.save(path='test',format='csv',mode='overwrite',sep='\t')




        # df = spark.readStream \
        # .format("kafka") \
        # .option("kafka.bootstrap.servers", consumer_config['bootstrap.servers']) \
        # .option("subscribe", topic) \
        # .load()

        print('dtream done-----------')


except KeyboardInterrupt:
    pass
finally:
    # Close down consumer to commit final offsets.
    consumer.close()
