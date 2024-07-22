# Weather gether

- написаны тесты ✅
- Проект обёрнут в Docker + docker-compose + nginx
- сделаны автодополнение (подсказки) при вводе города ✅
- при повторном посещении сайта будет предложено посмотреть погоду в городе,
в котором пользователь уже смотрел ранее ✅
- Сохраняется история поиска для каждого пользователя (Описан Стандартный класс с возможностью расширения функционала) ❌,
создан API, показывающее сколько раз вводили какой город✅

## О проекте

- Проект развернут в Docker-контейнерах;

## Стек технологий

- Python
- FastApi
- Alembic
- SQlite
- Docker
- pytest

## Зависимости

- Перечислены в файле requirements.txt

## **Как запустить проект**:

1. Установите (`у себя` \ `на сервере`) `docker` и `docker-compose`
2. Создайте файл `/infra/.env` Шаблон для заполнения файла находится в `/infra/.env.example`
3. Из директории `/infra/` выполните команду `docker-compose up -d --buld`
4. После чего можно перейти на [основную страницу](http://localhost/weather/)

Документация к API находится по адресу: <http://localhost/docs/>.

## Автор

- [Семён Новиков](https://github.com/Sovraska) 
