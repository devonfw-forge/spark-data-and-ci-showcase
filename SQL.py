from sqlalchemy import *
from sqlite3 import*
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

data_tables = create_engine('sqlite:///world-gdp.db')

Session = sessionmaker(bind=data_tables)
session = Session()

Base = declarative_base()


class Gdp(Base):
   __tablename__ = 'gdp'

   id = Column(Integer, primary_key=True)
   CountryCode = Column(String)
   Year = Column(Integer)
   gdp = Column(Integer)
   growth = Column(Integer)


class Analyse():

   def __init__(self):

      self.data = session.query(Gdp)

   def countries(self):
      country_list = []
      for country in session.query(Gdp.CountryCode).all():
         if country not in country_list:
            country_list.append(country)
      return country_list


T = Analyse()
print(T.countries())
