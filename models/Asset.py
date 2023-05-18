import datetime
from typing import Optional

from sqlmodel import SQLModel, Field

import sqlalchemy as sa

from models.Curreny import Currency
from models.Positions import Positions
from models.User import User


class Asset(SQLModel, table=True):
    __tablename__ = "asset"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(
        sa_column=sa.Column(sa.Integer, sa.ForeignKey(User.user_id, ondelete="CASCADE", onupdate="CASCADE")))

    positions_id: int = Field(
        sa_column=sa.Column(sa.Integer, sa.ForeignKey(Positions.positions_id, ondelete="CASCADE", onupdate="CASCADE")))

    currency_id: int = Field(
        sa_column=sa.Column(sa.Integer, sa.ForeignKey(Currency.currency_id, ondelete="CASCADE", onupdate="CASCADE")))

    created_at: datetime.datetime = Field(
        sa_column=sa.Column(sa.DateTime(timezone=True), default=datetime.datetime.now()))

    updated_at: Optional[datetime] = Field(
        sa_column=sa.Column(sa.DateTime(timezone=True), default=datetime.datetime.utcnow))
