from app.db.db import engine, Base
from app.db import models

# Создание всех таблиц
Base.metadata.create_all(bind=engine)
print("Таблицы успешно созданы!")
