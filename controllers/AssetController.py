from fastapi import APIRouter, Body, Depends
from starlette import status

from deps import get_asset_service
from request import AssetCreateRequest
from services.AssetService import AssetService

asset_router = APIRouter(
    prefix="/ASSET",
    tags=["Asset"],
)


@asset_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_asset(*,
                      data: AssetCreateRequest = Body(),
                      asset_service: AssetService = Depends(get_asset_service),
                      ):
    new_asset = await asset_service.create_asset(data)
    return new_asset
