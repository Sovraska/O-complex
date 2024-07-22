from fastapi import APIRouter

from app.api.endpoints import user_router, index_router, city_router

main_router = APIRouter()

main_router.include_router(user_router)
main_router.include_router(city_router, prefix="/city", tags=["Main"])
main_router.include_router(index_router, prefix="/weather", tags=["Main"])
