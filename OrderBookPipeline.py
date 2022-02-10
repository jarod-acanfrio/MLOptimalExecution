import time
import hmac
from requests import Request
from client import FtxClient
import pandas as pd

api = "h9EApq8k8zGIZgVzy3x8xBFX3oLCGErMbsC1YAYc"
secret = "Ja5aY4i7FxM5GXbwOJSDK_skdjhKjYLwylcYFses"

ftx_client = FtxClient(api_key=api, api_secret=secret)

while True:

    t = float(time.time())

    if(t%60==0):

        orderbook = ftx_client.get_orderbook(market="BTC/USD", depth=50)

        orderbook_asks = pd.DataFrame(orderbook['asks'])
        orderbook_bids = pd.DataFrame(orderbook['bids'])

        ask_file = "DATA/asks_" + str(int(t)) + ".csv"
        bid_file = "DATA/bids_" + str(int(t)) + ".csv"
            
        orderbook_asks.to_csv(ask_file)
        orderbook_bids.to_csv(bid_file)





























