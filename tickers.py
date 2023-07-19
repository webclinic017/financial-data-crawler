import json
import requests as rq
import pandas as pd
import pymysql
import time
import datetime as dt

# from investing.com
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import math
from tqdm import tqdm


def get_us_ticker_data():
    """
    Retrieves US ticker data from hankyung.com.

    Returns
    -------
    None.

    """

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
            "industry_nm": "Industry",
            "market_cap": "Market Cap",
        }
    )

    stock_bind_select = stock_bind[["Name", "Symbol", "Exchange", "Sector", "Industry", "Market Cap", "Date"]]

    con = pymysql.connect(user="root", passwd="mysql123", host="127.0.0.1", db="equities", charset="utf8")

    mycursor = con.cursor()

    query = """
        insert into us_tickers_kr (Name, Symbol, Exchange, Sector, Industry, `Market Cap`, Date)
        values (%s,%s,%s,%s,%s,%s,%s) as new
        on duplicate key update
        Exchange=new.Exchange, Sector=new.Sector, Industry=new.Industry, `Market Cap`=new.`Market Cap`;
    """

    args = stock_bind_select.values.tolist()

    mycursor.executemany(query, args)
    con.commit()

    con.close()


get_us_ticker_data()
