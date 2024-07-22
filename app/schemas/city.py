from pydantic import BaseModel


class CityCreate(BaseModel):
    city_name: str
    temperature: str
    score_voard: str
    time: str
