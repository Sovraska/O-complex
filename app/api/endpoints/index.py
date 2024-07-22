from pathlib import Path

from fastapi import APIRouter, Form, Request, status, Depends

from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.statistic import statistic_crud
from app.services.utils import get_weather

router = APIRouter()

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

templates = Jinja2Templates(directory=str(BASE_DIR.absolute() / 'templates'))


@router.get("/", response_class=HTMLResponse)
async def get_main_page(
        request: Request,
        city_name: str = None,
        session: AsyncSession = Depends(get_async_session)
):
    if city_name:
        temperature, time = await get_weather(city_name)
        data = await statistic_crud.get_ten_best_city(session=session)
        score_board = [
            (stat_obj.city_name, stat_obj.count)
            for stat_obj in data
        ]
        response = templates.TemplateResponse(
            "index.html", {
                "request": request,
                "temperature": temperature,
                "city_name": city_name,
                "time": time,
                "score_board": score_board
            }
        )
        response.set_cookie(key='city_name', value=city_name)
        return response
    response = templates.TemplateResponse(
        "index.html", {
            "request": request,
        }
    )
    return response


@router.post("/form")
async def form_main_page(
        city_name: str = Form(...),
):
    return RedirectResponse(
        f'/weather/?city_name={city_name}',
        status_code=status.HTTP_303_SEE_OTHER
    )
