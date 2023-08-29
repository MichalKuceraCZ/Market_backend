from data import StocksData


class StocksService:

    def __init__(self, context):
        self.session = context["session"]

    def create(self,data: StocksData):
        pass
