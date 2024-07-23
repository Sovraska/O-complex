# Weather gether

- написаны тесты ✅
- Проект обёрнут в Docker + docker-compose + nginx
- сделаны автодополнение (подсказки) при вводе города ✅
- при повторном посещении сайта будет предложено посмотреть погоду в городе,
в котором пользователь уже смотрел ранее ✅
- Сохраняется история поиска для каждого пользователя (Описан Стандартный класс с возможностью расширения функционала) ❌,
создан API, показывающее сколько раз вводили какой город✅

## О проекте

- Небольшой погодный Агригатор по городам (с плюшками)

## Стек технологий

- Python
- FastApi
- Alembic
- SQlite
- Docker
- pytest

## Зависимости

- Перечислены в файле requirements.txt

## **Как запустить проект на сервере **:

1. Установите на сервере `docker` и `docker-compose`
2. Создайте файл `/infra/.env` Шаблон для заполнения файла находится в `/infra/.env.example`
3. Из директории `/infra/` выполните команду `docker-compose up -d --buld`
4. Примените миграции `alembic upgrade head`
5. После чего можно перейти на [основную страницу](http://localhost/weather/)

## **Как запустить проект Локально **:
1. создайте виртуальное окружение `venv`
2. установите зависимости из requirements.txt -> `pip install -r requirements.txt --no-cache-dir --no-dependencies` ()
3. Примините миграции `alembic upgrade head`
4. Запустите приложение из корневой папки `uvicorn app.main:app --host "0.0.0.0 --port 8000 --proxy-headers`

Документация к API находится по адресу: <http://localhost/docs/>.

## Автор

- [Семён Новиков](https://github.com/Sovraska) 
