# schemas.py

from typing import Union
from pydantic import BaseModel

# Book
class BookBase(BaseModel):
    title: str
    description: str
    image_path: str
    price: int
    status: bool

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    category_id: int
    type_id: int
    author_id: int

    class Config:
        orm_mode = True

# Category
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

# Type
class TypeBase(BaseModel):
    name: str

class TypeCreate(TypeBase):
    pass

class Type(TypeBase):
    id: int

    class Config:
        orm_mode = True

# Author
class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True



class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str = None