from sqlmodel import Session


class AssetService:
    def __init__(self, session: Session):
        self.session = session

    def create_asset(self, data):
        pass