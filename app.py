from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine


CONN_STRING = "postgresql://postgres:postgresql123@localhost:5432/stocks"
ENGINE = create_engine(CONN_STRING)

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1(children="Financial Data Crawler", style={"textAlign": "center"}),
        html.H2(children="Global Stock Tickers"),
        html.Div(
            [
                html.Div(
                    [
                        html.Li(children="United States (NYSE, NASDAQ, Amex)"),
                        html.Button("CSV", id="us-csv-btn", style={"cursor": "pointer"}),
                        dcc.Download(id="download-df-csv"),
                        html.Button("Excel", id="us-excel-btn"),
                        dcc.Download(id="download-df-excel"),
                    ],
                    style={
                        "display": "flex",
                        "gap": "10px",
                        "justify-content": "start",
                        "align-items": "center",
                        "margin-left": "30px",
                    },
                )
            ],
            style={},
        ),
        html.H2(children="Financial News Headlines"),
    ]
)


@callback(Output("download-df-csv", "data"), Input("us-csv-btn", "n_clicks"), prevent_initial_call=True)
def download_csv(n_clicks):
    df = pd.read_sql("SELECT * FROM us_tickers_kr", ENGINE.connect())
    return dcc.send_data_frame(df.to_csv, "us_tickers_kr.csv")


@callback(Output("download-df-excel", "data"), Input("us-excel-btn", "n_clicks"), prevent_initial_call=True)
def download_excel(n_clicks):
    df = pd.read_sql("SELECT * FROM us_tickers_kr", ENGINE.connect())
    return dcc.send_data_frame(df.to_excel, "us_tickers_kr.xlsx", sheet_name="Sheet_name_1")


if __name__ == "__main__":
    app.run(debug=True)
