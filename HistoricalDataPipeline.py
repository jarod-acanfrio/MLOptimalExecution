from client import FtxClient
import pandas as pd

api = "h9EApq8k8zGIZgVzy3x8xBFX3oLCGErMbsC1YAYc"
secret = "Ja5aY4i7FxM5GXbwOJSDK_skdjhKjYLwylcYFses"

ftx_client = FtxClient(api_key=api, api_secret=secret)

start_time = 1644433140
end_time = 1644438180

ohlc_dict = ftx_client.get_historical_prices(market="BTC/USD", resolution=60, start_time=start_time, end_time=end_time)

start_time = []
time = []
high_price = []
low_price = []
open_price = []
close_price = [] 
volume = []

idx = 0
for candle in ohlc_dict:
    # each entry is a dictionary
    start_time.append(candle["startTime"])
    time.append(candle["time"]/1000)
    open_price.append(candle["open"])
    close_price.append(candle["close"])
    high_price.append(candle["high"])
    low_price.append(candle["low"])
    volume.append(candle["volume"])

ohlc_data = pd.DataFrame({"start_time": start_time, "time": time, "open": open_price, "close": close_price, "high": high_price, "low": low_price, "volume": volume})
print(ohlc_data.head())
ohlc_data.to_csv("OHLCV_DATA/ohlcv_data.csv")