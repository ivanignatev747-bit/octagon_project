from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db import crud
from app.db.db import get_db
from app.schemas import Book, BookCreate, BookUpdate

router = APIRouter(prefix="/books", tags=["books"])

@router.get("", response_model=List[Book])  # Убрали / в начале
def read_books(
    skip: int = 0,
    limit: int = 100,
    category_id: Optional[int] = Query(None, description="Фильтр по категории"),
    db: Session = Depends(get_db)
):
    """Получить список книг с возможностью фильтрации по категории"""
    if category_id is not None:
        # Проверяем существование категории
        category = crud.get_category(db, category_id=category_id)
        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")
        books = crud.get_books_by_category(db, category_id=category_id)
    else:
        books = crud.get_books(db, skip=skip, limit=limit)
    return books

@router.get("/{book_id}", response_model=Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    """Получить книгу по ID"""
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.post("", response_model=Book, status_code=201)  # Убрали / в начале
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """Создать новую книгу"""
    # Проверяем существование категории
    category = crud.get_category(db, category_id=book.category_id)
    if category is None:
        raise HTTPException(status_code=400, detail="Category not found")
    
    return crud.create_book(
        db=db,
        title=book.title,
        description=book.description,
        price=book.price,
        url=book.url,
        category_id=book.category_id
    )

@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    """Обновить книгу"""
    # Если указан category_id, проверяем существование категории
    if book.category_id is not None:
        category = crud.get_category(db, category_id=book.category_id)
        if category is None:
            raise HTTPException(status_code=400, detail="Category not found")
    
    update_data = book.dict(exclude_unset=True)
    db_book = crud.update_book(db, book_id=book_id, **update_data)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Удалить книгу"""
    db_book = crud.delete_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return None
