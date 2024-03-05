from sqlalchemy.orm import Session
import models
import schemas

#Category
def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_all_categories(db: Session):
    return db.query(models.Category).all()

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

#Type
def get_type(db: Session, type_id: int):
    return db.query(models.Type).filter(models.Type.id == type_id).first()

def get_all_types(db: Session):
    return db.query(models.Type).all()

def create_type(db: Session, type: schemas.TypeCreate):
    db_type = models.Type(name=type.name)
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type

#Author
def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()

def get_all_authors(db: Session):
    return db.query(models.Author).all()

def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


#Book

def create_book(db: Session, book: schemas.BookCreate, category_id: int, type_id: int, author_id: int):
    db_book = models.Book(
        title=book.title,
        description=book.description,
        price=book.price,
        image_path=book.image_path,
        status=book.status,
        category_id=category_id, 
        type_id=type_id,
        author_id=author_id 
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_all_books(db: Session):
    return db.query(models.Book).all()

def get_book(db: Session, book_id:int):
    return db.query(models.Book).filter(book_id == models.Book.id).first()

def get_books_by_category(db: Session, category_id: int):
    return db.query(models.Book).filter(models.Book.category_id==category_id).all()

def get_books_by_type(db: Session, type_id: int):
    return db.query(models.Book).filter(models.Book.type_id==type_id).all()

def get_books_by_author(db: Session, author_id: int):
    return db.query(models.Book).filter(models.Book.author_id==author_id).all()

def books_filter(db: Session, category_id=0, author_id=0, type_id=0):
    books_query = db.query(models.Book)
    
    if category_id != 0:
        books_query = books_query.filter(models.Book.category_id == category_id)
    if author_id != 0:
        books_query = books_query.filter(models.Book.author_id == author_id)
    if type_id != 0:
        books_query = books_query.filter(models.Book.type_id == type_id)
    
    filtered_books = books_query.all()
    return filtered_books

