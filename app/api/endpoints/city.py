from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.statistic import statistic_crud
from app.schemas.statistic import StatisticCreate
from app.services.utils import get_ten_city

router = APIRouter()


@router.post("/")
async def find_city(data: StatisticCreate):
    data = await get_ten_city(data.city_name)
    return data


@router.get("/statistic")
async def get_city_statistic(
        session: AsyncSession = Depends(get_async_session)
):
    data = await statistic_crud.get_ten_best_city(session=session)
    return data


@router.post("/statistic")
async def create_statistic(
        data: StatisticCreate,
        session: AsyncSession = Depends(
            get_async_session
        )
):
    data = await statistic_crud.create_city_statistic(
        city_name=data.city_name, session=session
    )
    return data
