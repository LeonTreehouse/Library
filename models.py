from sqlalchemy import create_engine, Column, Integer, String, Date

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///books.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column('Title', String)#the string makes the variable name look like the string so a capital t in the database will be shown. Not required only for the looks
    author = Column('Author', String)
    published_date = Column('Published', Date)
    price = Column('Price', Integer)

    def __repr__(self):
        return f'Title: {self.title} Author: {self.author} Published: {self.published_date} Price: {self.price}'

    

# create a database
#give it a name
#books.db
#create a model
#title author date publised price