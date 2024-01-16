import random
import time
from datetime import datetime


stock_data_list = []

def data_gen():
    symbol = random.choice(["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"])
    price = round(random.uniform(100, 1000), 2)
    volume = random.randint(10000, 1000000)

    # Create a timestamp
    timestamp_val = str(datetime.now())
    print(type(timestamp_val))

    # Format the data as a dictionary
    stock_data = {"timestamp_key": timestamp_val, "symbol": symbol, "price": price, "volume": volume}

    # Append the data to the list
    stock_data_list.append(stock_data)

    

    # Print or process the generated stock market data
    print(f"{timestamp_val}: {symbol} - Price: {price}, Volume: {volume}")
    

    return stock_data