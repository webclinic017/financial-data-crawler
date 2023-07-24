from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine
from config import config

params = config()

CONN_STRING = (
    f"postgresql://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['database']}"
)
ENGINE = create_engine(CONN_STRING)

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1(children="Financial Data Crawler", style={"textAlign": "center"}),
        html.H2(children="Global Stock Tickers"),
        html.H3(children="United States"),
        html.Div(
            [
                html.Div(
                    [
                        html.Li(children="By Exchanges (NYSE, NASDAQ, Amex)"),
                        html.Button("CSV", id="us-csv-btn", style={"cursor": "pointer"}),
                        dcc.Download(id="download-df-csv"),
                        html.Button("Excel", id="us-excel-btn", style={"cursor": "pointer"}),
                        dcc.Download(id="download-df-excel"),
                    ],
                    style={
                        "display": "flex",
                        "gap": "10px",
                        "justify-content": "start",
                        "align-items": "center",
                        "margin-left": "30px",
                        "margin-bottom": "10px",
                    },
                ),
                html.Div(
                    [
                        html.Li(children="S&P 500"),
                        html.Button("CSV", id="us-sp500-csv-btn", style={"cursor": "pointer"}),
                        dcc.Download(id="download-sp500-csv"),
                        html.Button("Excel", id="us-sp500-excel-btn", style={"cursor": "pointer"}),
                        dcc.Download(id="download-sp500-excel"),
                    ],
                    style={
                        "display": "flex",
                        "gap": "10px",
                        "justify-content": "start",
                        "align-items": "center",
                        "margin-left": "30px",
                        "margin-bottom": "10px",
                    },
                ),
                html.Div(
                    [
                        html.Li(children="NASDAQ 100"),
                        html.Button("CSV", id="us-nasdaq100-csv-btn", style={"cursor": "pointer"}),
                        dcc.Download(id="download-nasdaq100-csv"),
                        html.Button("Excel", id="us-nasdaq100-excel-btn", style={"cursor": "pointer"}),
                        dcc.Download(id="download-nasdaq100-excel"),
                    ],
                    style={
                        "display": "flex",
                        "gap": "10px",
                        "justify-content": "start",
                        "align-items": "center",
                        "margin-left": "30px",
                        "margin-bottom": "10px",
                    },
                ),
            ],
            style={},
        ),
        html.H2(children="Price Data"),
        html.H2(children="Financial Satements Data"),
    ]
)


@callback(Output("download-df-csv", "data"), Input("us-csv-btn", "n_clicks"), prevent_initial_call=True)
def download_by_us_exchanges_csv(n_clicks):
    df = pd.read_sql("SELECT * FROM us_tickers_kr", ENGINE.connect())
    df = df[["Symbol", "Exchange"]]
    return dcc.send_data_frame(df.to_csv, "us_tickers_by_exchanges.csv")


@callback(Output("download-df-excel", "data"), Input("us-excel-btn", "n_clicks"), prevent_initial_call=True)
def download_by_us_exchanges_excel(n_clicks):
    df = pd.read_sql("SELECT * FROM us_tickers_kr", ENGINE.connect())
    df = df[["Symbol", "Exchange"]]
    return dcc.send_data_frame(df.to_excel, "us_tickers_by_exchanges.xlsx", sheet_name="US_Exchanges")


@callback(Output("download-sp500-csv", "data"), Input("us-sp500-csv-btn", "n_clicks"), prevent_initial_call=True)
def download_sp500_tickers_csv(n_clicks):
    df = pd.read_sql("SELECT * FROM sp500_tickers", ENGINE.connect())
    return dcc.send_data_frame(df.to_csv, "sp500_tickers.csv")


@callback(Output("download-sp500-excel", "data"), Input("us-sp500-excel-btn", "n_clicks"), prevent_initial_call=True)
def download_sp500_tickers_excel(n_clicks):
    df = pd.read_sql("SELECT * FROM sp500_tickers", ENGINE.connect())
    return dcc.send_data_frame(df.to_excel, "sp500_tickers.xlsx", sheet_name="S&P500")


@callback(
    Output("download-nasdaq100-csv", "data"), Input("us-nasdaq100-csv-btn", "n_clicks"), prevent_initial_call=True
)
def download_nasdaq100_tickers_csv(n_clicks):
    df = pd.read_sql("SELECT * FROM nasdaq100_tickers", ENGINE.connect())
    return dcc.send_data_frame(df.to_csv, "nasdaq100_tickers.csv")


@callback(
    Output("download-nasdaq100-excel", "data"), Input("us-nasdaq100-excel-btn", "n_clicks"), prevent_initial_call=True
)
def download_nasdaq100_tickers_excel(n_clicks):
    df = pd.read_sql("SELECT * FROM nasdaq100_tickers", ENGINE.connect())
    return dcc.send_data_frame(df.to_excel, "nasdaq100_tickers.xlsx", sheet_name="NASDAQ100")


if __name__ == "__main__":
    app.run(debug=True)
