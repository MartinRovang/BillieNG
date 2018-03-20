import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledefstats import *

engine = create_engine('sqlite:///tutorial.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin","password",100,10,20,10000,User.number_of_user)
session.add(user)


# commit the record the database
session.commit()

session.commit()
