from datetime import datetime
import sqlalchemy as sa
from sqlmodel import SQLModel, Field

from models.StocksModel import StocksModel


class StockDataModel(SQLModel, table=True):
    __tablename__ = "stock_data"

    stock_data_id: int = Field(nullable=False, primary_key=True)
    low: int = Field(nullable=False)
    high: int = Field(nullable=False)
    close: int = Field(nullable=False)
    open: int = Field(nullable=False)
    time: datetime = Field(nullable=False)

    stock_id: int = Field(sa_column=sa.Column(sa.ForeignKey(StocksModel.stocks_id, ondelete="CASCADE",
                                                            onupdate="CASCADE")))
