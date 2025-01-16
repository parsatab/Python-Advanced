from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, Integer, String

engine = create_engine('sqlite:///books.db')
Base = declarative_base()


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)
    isbn = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def insert(title, author, year, isbn):
    new_book = Book(title=title, author=author, year=year, isbn=isbn)
    session.add(new_book)
    session.commit()


def view():
    books = session.query(Book).all()
    return books

def search(title="", author="", year="", isbn=""):
    query = session.query(Book)
    if title:
        query = query.filter(Book.title == title)
    if author:
        query = query.filter(Book.author == author)
    if year:
        query = query.filter(Book.year == year)
    if isbn:
        query = query.filter(Book.isbn == isbn)

    return query


def delete(id):
    book_to_delete = session.query(Book).filter(Book.id == id).first()
    if book_to_delete:
        session.delete(book_to_delete)
        session.commit()


def update(id, title, author, year, isbn):
    book_to_update = session.query(Book).filter(Book.id == id).first()
    if book_to_update:
        book_to_update.title = title
        book_to_update.author = author
        book_to_update.year = year
        book_to_update.isbn = isbn
        session.commit()


Base.metadata.create_all(engine)

# insert("Js", "JavaScript", 2018, 98082)
# print(view())
# print(search(author="Luciano Ramalho"))
# update(4, "C#", 'Ordookhani', 2022, 98765)
# delete(4)

session.close()