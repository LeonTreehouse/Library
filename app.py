from models import (Base, session, Book, engine)

#import models
#main menue add- search - analysis, exit, view
# add books to data base
#edit books
#delete them
#search books
#data clearing
#loops runs program

if __name__ == '__main__':
    Base.metadata.create_all(engine)