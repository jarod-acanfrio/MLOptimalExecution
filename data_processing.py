import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

from os import listdir
from os.path import isfile, join

# Data Import -----------------------------------------------------------------

ob_data_path = "/Users/jarodacanfrio/Documents/spring_2022/AIML/Project/OB_DATA"
ohlcv_data_path = "/Users/jarodacanfrio/Documents/spring_2022/AIML/Project/OHLCV_DATA/ohlcv_data.csv"

orderbook_files = [f for f in listdir(ob_data_path) if isfile(join(ob_data_path, f))]
orderbook_files.sort()

start_time = 1644433140
end_time = 1644438180

ask_data = []
bid_data = []

for file in orderbook_files:
    print(file)
    if file[0:4] == "asks":
        df_temp = pd.read_csv(ob_data_path+"/"+file, index_col=0)
        ask_data.append(df_temp)
        
    elif file[0:4] == "bids":
        df_temp = pd.read_csv(ob_data_path+"/"+file, index_col=0)
        bid_data.append(df_temp)
        
ohlcv_data = pd.read_csv(ohlcv_data_path, index_col=0)

# Orderbook Feature Creation --------------------------------------------------


# The factors:
# sum of size of bids - sum of size of asks
# divided by
# sum of size of bids + sum of size of asks

def BidAskImbalanceCumm(bid_data: list, ask_data: list) -> np.array:
    
    assert(len(bid_data) == len(ask_data))
    baic = []
    
    for idx in range(1,len(bid_data)):
        
        tot_bid = bid_data[idx].iloc[:,1].sum()
        tot_ask = ask_data[idx].iloc[:,1].sum()
        baic_temp = (tot_bid - tot_ask)/(tot_bid + tot_ask)
        baic.append(baic_temp)
        
    return np.array(baic)

baic = BidAskImbalanceCumm(bid_data, ask_data)
print(baic)
print(baic.mean())




# OHLCV Feature Creation ------------------------------------------------------









































