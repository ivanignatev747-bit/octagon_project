# Проект: Работа с PostgreSQL и SQLAlchemy

Проект демонстрирует интеграцию PostgreSQL с Python через SQLAlchemy.

## Структура проекта
- `app/db/db.py` - подключение к базе данных
- `app/db/models.py` - модели данных (Category, Book)
- `app/db/crud.py` - CRUD операции
- `app/init_db.py` - инициализация базы данных
- `app/main.py` - вывод данных из базы
- `.env` - параметры подключения (не в git)

## Установка
1. Клонировать репозиторий
2. Создать виртуальное окружение: `python -m venv venv`
3. Активировать: `source venv/bin/activate`
4. Установить зависимости: `pip install -r requirements.txt`
5. Настроить `.env` файл с параметрами БД
6. Запустить: `python -m app.init_db` затем `python -m app.main`

## Технологии
- Python 3.x
- PostgreSQL
- SQLAlchemy
- psycopg2
