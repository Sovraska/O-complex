from app.core.config import settings


DATABASE_URL_TEST = f'{settings.database_url}_test'

fixture_base = 'app.tests.fixtures'

pytest_plugins = [
    f'{fixture_base}.user',
]
