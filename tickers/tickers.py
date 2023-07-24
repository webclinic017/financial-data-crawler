import datetime as dt
import json
import math
import time

import pandas as pd
import psycopg2
import requests as rq
from bs4 import BeautifulSoup

# from investing.com
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from sqlalchemy import create_engine
from tqdm import tqdm
from webdriver_manager.chrome import ChromeDriverManager

#!/usr/bin/python
from config import config

params = config()

CONN_STRING = (
    f"postgresql://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['database']}"
)
ENGINE = create_engine(CONN_STRING)


def get_us_tickers_data():
    """
    Retrieves US ticker data from hankyung.com and stores them in local Postgresql DB.

    Returns
    -------
    None.

    """

    DB_TABLE_NAME = "us_tickers_kr"

    market = ["nyse", "nasdaq", "amex"]

    stocks = []

    for mkt in tqdm(market):
        url = f"https://www.hankyung.com/globalmarket/data/price?type={mkt}&sort=market_cap_top&sector_nm=&industry_nm=&chg_net_text="

        data = rq.get(url).json()
        data_pd = pd.json_normalize(data["list"])

        # Remove '-US' and replace '.' to '-' in symbol column
        data_pd["symbol"] = data_pd["symbol"].str.replace("-US", "")
        data_pd["symbol"] = data_pd["symbol"].str.replace(".", "-")

        stocks.append(data_pd)
        time.sleep(3)

    stock_bind = pd.concat(stocks)

    stock_bind["Date"] = dt.datetime.today().strftime("%Y-%m-%d")

    stock_bind = stock_bind.rename(
        columns={
            "symbol": "Symbol",
            "hname": "Name",
            "primary_exchange_name": "Exchange",
            "sector_nm": "Sector",
            "market_cap": "MarketCap",
        }
    )

    stock_bind_select = stock_bind[["Name", "Symbol", "Exchange", "Sector", "MarketCap", "Date"]]

    stock_bind_select.to_sql(DB_TABLE_NAME, con=ENGINE.connect(), if_exists="replace", index=False)


if __name__ == "__main__":
    # update US ticker data
    get_us_tickers_data()
