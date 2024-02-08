from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String)
    image_path = Column(String)
    price = Column(Integer)
    status = Column(Boolean)

    category_id = Column(Integer, ForeignKey('categories.id'))
    type_id = Column(Integer, ForeignKey('types.id')) 
    author_id = Column(Integer, ForeignKey('authors.id'))

    category = relationship('Category', back_populates='books')
    type = relationship('Type', back_populates='books')
    author = relationship('Author', back_populates='books')
    
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    books = relationship("Book", back_populates="category")

class Type(Base):
    __tablename__ = "types"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    books = relationship("Book", back_populates="type")
    
class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    books = relationship("Book", back_populates="author")
