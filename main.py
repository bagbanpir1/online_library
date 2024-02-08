from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()


#Category
@app.post("/catergory/add", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db:Session=Depends(get_db)):
    return crud.create_category(db=db, category=category)

@app.get("/category/all", response_model=list[schemas.Category])
def get_all_categoryies(db:Session=Depends(get_db)):
    db_categories = crud.get_all_categories(db=db)
    return db_categories

@app.get("/category/{category_id}")
def get_category(category_id: int, db:Session=Depends(get_db)):
    db_category = crud.get_category(db=db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not Found")
    return db_category


#Type
@app.post("/type/add", response_model=schemas.Type)
def create_type(type:schemas.TypeCreate, db:Session=Depends(get_db)):
    return crud.create_type(db=db, type=type)

@app.get("/type/all", response_model=list[schemas.Type])
def get_all_types(db:Session=Depends(get_db)):
    db_types = crud.get_all_types(db=db)
    return db_types

@app.get("/type/{type_id}")
def get_type(type_id: int, db:Session=Depends(get_db)):
    db_type = crud.get_type(db=db, type_id=type_id)
    if db_type is None:
        raise HTTPException(status_code=404, detail="Type not Found")
    return db_type


#Author
@app.post("/author/add", response_model=schemas.Author)
def create_author(author:schemas.AuthorCreate, db:Session=Depends(get_db)):
    return crud.create_author(db=db, author=author)

@app.get("/author/all", response_model=list[schemas.Author])
def get_all_authors(db:Session=Depends(get_db)):
    db_authors = crud.get_all_authors(db=db)
    return db_authors

@app.get("/author/{author_id}")
def get_author(author_id: int, db:Session=Depends(get_db)):
    db_author = crud.get_author(db=db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not Found")
    return db_author

#Book
@app.post("/book/add", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, category_id: int, type_id: int, author_id: int, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book, category_id=category_id, type_id=type_id, author_id=author_id)

@app.get("/book/all", response_model=list[schemas.Book])
def get_all_books(db:Session=Depends(get_db)):
    db_book = crud.get_all_books(db=db)
    return db_book

@app.get("/book/{book_id}")
def get_book(book_id:int, db: Session=Depends(get_db)):
    db_book = crud.get_book(book_id=book_id, db=db)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not Found")
    return db_book

@app.get("/book/category/{category_id}")
def get_books_by_category(category_id:int, db:Session=Depends(get_db)):
    db_books_by_category = crud.get_books_by_category(category_id=category_id, db=db)
    return db_books_by_category

@app.get("/book/author/{author_id}")
def get_books_by_author(author_id:int, db:Session=Depends(get_db)):
    db_books_by_author = crud.get_books_by_author(author_id=author_id, db=db)
    return db_books_by_author

@app.get("/book/type/{type_id}")
def get_books_by_type(type_id:int, db:Session=Depends(get_db)):
    db_books_by_type = crud.get_books_by_type(type_id=type_id, db=db)
    return db_books_by_type
