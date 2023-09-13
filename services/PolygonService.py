import requests

from data import StocksData
from data.StockAggregatesData import StockAggregatesData


class PolygonService:

    def __init__(self, context):
        self.context = context

    def get_stocks(self) -> list[StocksData]:
        response = requests.get(
            f"https://api.polygon.io/v3/reference/tickers?type=CS&market=stocks&exchange=XNAS&active=true&limit=10"
            f"&apiKey={self.context['api_key']}")
        stocks = response.json()

        return stocks["results"]

    def get_stock_data(self, ticker: str) -> list[StockAggregatesData]:
        response = requests.get(f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/2023-01-05/2023-01-20"
                                f"?adjusted=true&sort=asc&limit=120&apiKey={self.context['api_key']}")

        data = response.json()

        return data["results"]
