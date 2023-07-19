from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv")

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
                        html.Button("JSON", id="us-json-btn"),
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
        html.Div(
            [
                html.Div(
                    [
                        html.Li(children="United States (NYSE, NASDAQ, Amex)"),
                        html.Button("CSV", id="us-csv-btn", style={"cursor": "pointer"}),
                        html.Button("JSON", id="us-json-btn"),
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


if __name__ == "__main__":
    app.run(debug=True)
