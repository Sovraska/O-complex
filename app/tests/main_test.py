import re

import pytest
from bs4 import BeautifulSoup
from httpx import AsyncClient

from fastapi import status

from app.services.utils import get_weather


class TestWeather:

    @pytest.mark.asyncio
    async def test_get_main(
            self,
            new_client: AsyncClient,
    ):
        """test."""
        response = await new_client.get('/weather/')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.skip(reason="problems with sessions")
    @pytest.mark.asyncio
    async def test_post_form(
            self,
            new_client: AsyncClient,
    ):
        city = 'london'
        data = {
            "city_name": city
        }
        response = await new_client.post(
            '/weather/form', data=data, follow_redirects=True
        )
        assert response.status_code == status.HTTP_200_OK
        soup = BeautifulSoup(response.text)
        script = soup.find('script', {'id': 'my-script'}).text
        data_time = re.search('time = "(.+).+?;', script)
        data_time = data_time.group(1).replace(
            '[', ''
        ).replace(
            ']', ''
        ).split(',')
        data_temp = re.search('temperature = "(.+).+?;', script)
        data_temp = data_temp.group(1).replace(
            '[', ''
        ).replace(
            ']', ''
        ).split(',')
        data = await get_weather(city)
        data_time2 = []
        for x in data_time:
            if x[0] == ' ':
                data_time2.append(int(x[1:]))
            else:
                data_time2.append(int(x))

        assert (list(map(float, data_temp)), data_time2) == data
