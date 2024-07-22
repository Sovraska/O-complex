from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.statistic import Statistic


class CRUDStatistic(CRUDBase):
    async def create_city_statistic(self, city_name: dict, session):
        db_obj = await session.execute(
            select(self.model).where(self.model.city_name == city_name)
        )
        db_obj = db_obj.scalars().first()
        if db_obj:
            setattr(db_obj, 'count', db_obj.count + 1)
            session.add(db_obj)
            await session.commit()
            await session.refresh(db_obj)
            return db_obj

        db_obj = self.model(
            **
            {
                "city_name": city_name,
                'count': 1
            }
        )
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def get_ten_best_city(self, session: AsyncSession):
        db_obj = await session.execute(
            select(self.model).order_by(desc(self.model.count)).limit(10)
        )
        return db_obj.scalars().all()


statistic_crud = CRUDStatistic(Statistic)
