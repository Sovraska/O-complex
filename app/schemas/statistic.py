from pydantic import BaseModel


class StatisticCreate(BaseModel):
    city_name: str


class StatisticRead(BaseModel):
    city_name: str
    count: int
