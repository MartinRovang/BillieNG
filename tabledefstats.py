from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///tutorial.db', echo=True)
Base = declarative_base()

########################################################################
class User(Base):
    number_of_user = 0
    """"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


    #----------------------------------------------------------------------
    def __init__(self, username, password,health,armor,dmg,money,id):
        """"""
        User.number_of_user += 1
        self.username = username
        self.password = password
        self.health = health
        self.armor = armor
        self.dmg = dmg
        self.money = money
        self.id = id
    def apply_money(self):
        self.money = int(self.money + 1000)


# create tables
Base.metadata.create_all(engine)
