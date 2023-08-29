from sqlmodel import SQLModel, Field


class StocksModel(SQLModel, table=True):
    stocks_id: int = Field(default=None, primary_key=True)

    ticker: str = Field(nullable=False, unique=True)
    name: str = Field(nullable=False)
    currency_name: str = Field(nullable=False)
