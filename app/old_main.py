from app.db.db import SessionLocal
from app.db.crud import get_categories, get_books, get_books_by_category
from sqlalchemy.orm import joinedload

def main():
    # Создаем сессию
    db = SessionLocal()
    
    try:
        print("=" * 50)
        print("СОДЕРЖИМОЕ БАЗЫ ДАННЫХ octagon_db")
        print("=" * 50)
        
        # 1. Получаем все категории
        categories = get_categories(db)
        
        print(f"\n📚 КАТЕГОРИИ ({len(categories)}):")
        print("-" * 30)
        
        for category in categories:
            print(f"ID: {category.id}, Название: {category.title}")
            
            # 2. Получаем книги для каждой категории
            books = get_books_by_category(db, category.id)
            
            if books:
                print(f"   Книги в категории:")
                for book in books:
                    print(f"   - {book.title} (Цена: {book.price} руб.)")
            else:
                print(f"   Нет книг в этой категории")
            
            print()
        
        # 3. Получаем все книги
        all_books = get_books(db)
        print(f"\n📖 ВСЕГО КНИГ В БАЗЕ: {len(all_books)}")
        print("-" * 30)
        
        # Выводим статистику
        total_price = sum(book.price for book in all_books)
        avg_price = total_price / len(all_books) if all_books else 0
        
        print(f"Общая стоимость всех книг: {total_price:.2f} руб.")
        print(f"Средняя цена книги: {avg_price:.2f} руб.")
        
        # 4. Подробный список всех книг
        print(f"\n📋 ПОДРОБНЫЙ СПИСОК КНИГ:")
        print("-" * 50)
        
        for i, book in enumerate(all_books, 1):
            print(f"{i}. {book.title}")
            print(f"   Описание: {book.description}")
            print(f"   Цена: {book.price} руб.")
            print(f"   Категория ID: {book.category_id}")
            print(f"   URL: {book.url if book.url else 'Не указан'}")
            print()
        
    except Exception as e:
        print(f"Ошибка при чтении данных: {e}")
    
    finally:
        db.close()
    
    print("=" * 50)
    print("ВЫПОЛНЕНИЕ ЗАВЕРШЕНО")

if __name__ == "__main__":
    main()
