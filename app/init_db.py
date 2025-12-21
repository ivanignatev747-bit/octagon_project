from app.db.db import SessionLocal, engine
from app.db import models
from app.db.crud import create_category, create_book

# Убедимся, что таблицы созданы
models.Base.metadata.create_all(bind=engine)

# Создаем сессию
db = SessionLocal()

try:
    # 1. Создаем категории
    print("Создание категорий...")
    fiction_category = create_category(db, title="Художественная литература")
    tech_category = create_category(db, title="Техническая литература")
    science_category = create_category(db, title="Научная литература")
    
    # 2. Создаем книги для каждой категории
    print("Создание книг...")
    
    # Книги для Художественной литературы
    create_book(
        db,
        title="Мастер и Маргарита",
        description="Роман Михаила Булгакова",
        price=450.0,
        url="",
        category_id=fiction_category.id
    )
    
    create_book(
        db,
        title="Преступление и наказание",
        description="Роман Фёдора Достоевского",
        price=380.0,
        url="",
        category_id=fiction_category.id
    )
    
    create_book(
        db,
        title="1984",
        description="Роман-антиутопия Джорджа Оруэлла",
        price=520.0,
        url="",
        category_id=fiction_category.id
    )
    
    # Книги для Технической литературы
    create_book(
        db,
        title="Чистый код",
        description="Создание, анализ и рефакторинг",
        price=1200.0,
        url="",
        category_id=tech_category.id
    )
    
    create_book(
        db,
        title="Совершенный код",
        description="Практическое руководство по разработке ПО",
        price=1350.0,
        url="",
        category_id=tech_category.id
    )
    
    create_book(
        db,
        title="Грокаем алгоритмы",
        description="Иллюстрированное пособие для программистов",
        price=890.0,
        url="",
        category_id=tech_category.id
    )
    
    create_book(
        db,
        title="Python. К вершинам мастерства",
        description="Лучшие практики и примеры",
        price=1100.0,
        url="",
        category_id=tech_category.id
    )
    
    # Книги для Научной литературы
    create_book(
        db,
        title="Краткая история времени",
        description="От большого взрыва до черных дыр",
        price=670.0,
        url="",
        category_id=science_category.id
    )
    
    create_book(
        db,
        title="Космос",
        description="Эволюция Вселенной, жизни и цивилизации",
        price=750.0,
        url="",
        category_id=science_category.id
    )
    
    print("✅ База данных успешно инициализирована!")
    print(f"   Создано категорий: 3")
    print(f"   Создано книг: 8")
    
except Exception as e:
    print(f"❌ Ошибка при инициализации: {e}")
    db.rollback()
finally:
    db.close()
