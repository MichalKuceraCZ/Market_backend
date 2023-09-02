import requests

from data import StocksData


class PolygonService:

    def __init__(self, context):
        self.context = context

    def get_stocks(self) -> list[StocksData]:
        response = requests.get(
            f"https://api.polygon.io/v3/reference/tickers?type=CS&market=stocks&exchange=XNAS&active=true&limit=10"
            f"&apiKey={self.context['api_key']}")
        stocks = response.json()

        return stocks["results"]
