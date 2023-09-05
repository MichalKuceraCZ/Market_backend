from sqlmodel import select

from data import StocksData
from models.StocksModel import StocksModel


class StocksService:

    def __init__(self, context):
        self.session = context["session"]

    async def create(self, data: list[StocksData]) -> None:
        new_stocks = []

        for stock in data:
            stock_model = StocksModel(
                ticker=stock["ticker"],
                name=stock["name"],
                currency_name=stock["currency_name"],
            )
            new_stocks.append(stock_model)

        self.session.add_all(new_stocks)
        await self.session.commit()

    async def get(self):
        query = (
            select(StocksModel)
            .offset(0)
            .limit(10)
        )

        result = await self.session.execute(query)
        return result.all()
