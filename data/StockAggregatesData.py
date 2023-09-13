from pydantic import BaseModel


# "v": 80716808,
# "vw": 126.0883,
# "o": 127.13,
# "c": 125.02,
# "h": 127.77,
# "l": 124.76,
# "t": 1672894800000,
# "n": 665458

class StockAggregatesData(BaseModel):
    c: float
    h: float
    l: float
    n: float
    o: float
    t: float
    v: float
    vw: float
