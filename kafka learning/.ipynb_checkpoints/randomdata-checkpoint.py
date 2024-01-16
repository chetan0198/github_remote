# import time
# import random

# while True:
#     # Generate random data (replace this with your data generation logic)
#     random_number = random.randint(1, 100)
#     timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

#     # Print or process the generated data
#     print(f"{timestamp}: Random Number: {random_number}")

#     # Wait for one second
#     time.sleep(1)


# import time
# import random

# # Initialize an empty list to store stock market data
# stock_data_list = []

# while True:
#     # Generate random stock market data
#     symbol = random.choice(["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"])
#     price = round(random.uniform(100, 1000), 2)
#     volume = random.randint(10000, 1000000)

#     # Create a timestamp
#     timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

#     # Format the data and append to the list
#     stock_data = {"timestamp": timestamp, "symbol": symbol, "price": price, "volume": volume}
#     stock_data_list.append(stock_data)

#     # Print or process the generated stock market data
#     print(f"{timestamp}: {symbol} - Price: {price}, Volume: {volume}")

#     # Wait for one second
#     time.sleep(1)

# import random_data_generator as r

# r.data_gen()


import json

# Example string with dictionary content
# string_with_dict = '{"key1": "value1", "key2": "value2", "key3": 3}'
received_data = "'timestamp': '2024-01-15 13:48:59', 'symbol': 'AMZN', 'price': 238.81, 'volume': 147536"


# Convert the string to a dictionary
# dictionary_from_string = json.loads("string_with_dict")

# lst=string_with_dict.split(',')

# data_dict = dict(item.split(":") for item in received_data.split(","))

# for item in received_data.split(","):
#     print(item,type(item))
#     data=item.split(':')
#     print(data,type(data))
#     print()

# print(data_dict)

import pysprk


# print(lst[0])
# prin

# Print the resulting dictionary
# print(dictionary_from_string,type(dictionary_from_string))
