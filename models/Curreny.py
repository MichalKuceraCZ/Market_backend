import datetime
from typing import Optional

import sqlalchemy as sa

from sqlmodel import SQLModel, Field

from models.Positions import Positions
from models.User import User


class Currency(SQLModel, table=True):
    __tablename__ = "currency"

    currency_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(
        sa_column=sa.Column(sa.Integer, sa.ForeignKey(User.user_id, ondelete="CASCADE", onupdate="CASCADE")))

    positions_id: int = Field(
        sa_column=sa.Column(sa.Integer, sa.ForeignKey(Positions.positions_id, ondelete="CASCADE", onupdate="CASCADE")))

    created_at: datetime.datetime = Field(
        sa_column=sa.Column(sa.DateTime(timezone=True), default=datetime.datetime.now()))

    updated_at: Optional[datetime] = Field(
        sa_column=sa.Column(sa.DateTime(timezone=True), default=datetime.datetime.utcnow))
