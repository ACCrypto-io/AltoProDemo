
TIME_COLUMN = "created_utc"
COIN_SYMBOL_COLUMN = "coin_symbol"

# This file contain the Maximum/Minimum price change in 7 days (168 hours) for every hour
# Example: for created_utc 1455145200 (February 10, 2016 11:00:00 PM) the maximum price change for BTC in the next
# 7 days is 10.179% while the minimum price change is -1.2609%.
BTC_PRICE_CHANGE_FILE = 'Data/btc-price-change-7days.csv.gz'
ACC_DATA_PATH = 'Data/BTC-Samples.csv.gz'

BTC_PRICE_CHANGE_MAX_NAME = 'open_max_change'
BTC_PRICE_CHANGE_MIN_NAME = 'open_min_change'

FEATURE_NAME_COLUMN = 'feature_name'
CORR_RES_MAX_CHANGE = 'corr_max_change'
CORR_RES_MIN_CHANGE = 'corr_min_change'

NORM_DATA = True
WINDOW_SIZE = 24

ACC_WEBSITE = 'https://ACCrypto.io'
