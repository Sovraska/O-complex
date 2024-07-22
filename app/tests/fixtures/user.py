import pytest_asyncio

from httpx import AsyncClient

from app.main import app

USER_EMAIL = 'testuser@example.com'
USER_PASSWORD = 'string'
USER_USERNAME = 'testuser'


@pytest_asyncio.fixture
async def new_client(
) -> AsyncClient:
    """Фикстура создания нового клиента."""

    yield AsyncClient(
        app=app,
        base_url='http://test',
    )
