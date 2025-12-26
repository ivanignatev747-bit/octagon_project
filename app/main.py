from fastapi import FastAPI
from app.api.categories import router as categories_router
from app.api.books import router as books_router
from app.db.db import engine, Base
from app.db import models

# Создаём таблицы при старте (если их нет)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bookstore API",
    description="API для управления книгами и категориями",
    version="1.0.0"
    # Убрали redirect_slashes=False - пусть работает стандартное поведение
)

# Подключаем роутеры
app.include_router(categories_router)
app.include_router(books_router)

@app.get("/health")
def health_check():
    """Проверка работоспособности API"""
    return {"status": "ok", "message": "API is running"}

@app.get("/")
def root():
    """Корневой endpoint"""
    return {
        "message": "Добро пожаловать в Bookstore API",
        "docs": "/docs",
        "health": "/health",
        "categories": "/categories/",
        "books": "/books/"
    }
