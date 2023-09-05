from fastapi import APIRouter, Depends
from starlette import status
from starlette.responses import Response

from deps import get_stocks_service, get_polygon_service
from services.PolygonService import PolygonService
from services.StocksService import StocksService

stocks_router = APIRouter(
    prefix="/stocks",
    tags=["Stocks"]
)


@stocks_router.post("/")
async def create_stocks(
        *,
        stocks_service: StocksService = Depends(get_stocks_service),
        polygon_service: PolygonService = Depends(get_polygon_service),
):
    polygon_data = polygon_service.get_stocks()
    await stocks_service.create(polygon_data)

    return Response(status_code=status.HTTP_200_OK)


@stocks_router.get("/")
async def get_stocks(*,
                     stocks_service: StocksService = Depends(get_stocks_service)):
    stocks = await stocks_service.get()

    return stocks
    # return Response(status_code=status.HTTP_200_OK, content=stocks)
