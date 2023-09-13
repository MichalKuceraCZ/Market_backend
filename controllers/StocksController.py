from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import NoResultFound
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


@stocks_router.get("/{id}")
async def get_stock(*,
                    stocks_service: StocksService = Depends(get_stocks_service),
                    id: int
                    ):
    try:
        stock = await stocks_service.getById(id)
        return stock
    except NoResultFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": f"Stock not found [{id}]",
                "code": "STOCK_NOT_FOUND",
                "status": status.HTTP_404_NOT_FOUND
            }
        )


@stocks_router.post("/data/{ticker}")
async def create_stock_data(*,
                            polygon_service: PolygonService = Depends(get_polygon_service),
                            ticker: str
                            ):
    stock_data = await polygon_service.get_stock_data(ticker)
    await polygon_service.create_data(stock_data)
    return Response(status_code=status.HTTP_200_OK)
