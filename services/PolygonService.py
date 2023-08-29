import requests


class PolygonService:

    def __init__(self, context):
        self.context = context

    def get_stocks(self):
        response = requests.get(
            f"https://api.polygon.io/v3/reference/tickers?type=CS&market=stocks&exchange=XNAS&active=true&limit=10"
            f"&apiKey={self.context['api_key']}")
        stocks = response.json()

        return stocks["results"]
