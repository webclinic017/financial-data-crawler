import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
import tqdm

#!/usr/bin/python
from config import config

params = config()

CONN_STRING = (
    f"postgresql://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['database']}"
)
ENGINE = create_engine(CONN_STRING)

# prices = yf.download("AAPL")
# prices

symbols = pd.read_sql("SELECT * FROM us_tickers_kr", con=ENGINE.connect())

errors_list = []

for symbol in symbols["Symbol"][3:5]:
    # try:
    prices = yf.download(symbol, progress=False)
    prices = prices.reset_index()
    prices["symbol"] = symbol
    prices.columns = ["date", "open", "high", "low", "close", "Adj Close", "volume", "symbol"]
    prices.set_index("date", inplace=True)

    prices.to_sql("global_prices", if_exists="append", con=ENGINE.connect())

# except:
#     raise Exception
#     errors_list.append(symbol)

print(errors_list)
