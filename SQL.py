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

class Countries(Base):
   __tablename__ = 'countries'

   CountryCode = Column(String, primary_key=True)
   CountryName = Column(String)


class Analyse:

   def __init__(self):

      self.data = session.query(Gdp)

   def countries(self):
      country_list = []
      for country in session.query(Gdp.CountryCode).all():
         if self.code_to_name(country[0]) not in country_list:
            country_list.append(self.code_to_name(country[0]))

      return country_list

   def code_to_name(self, code):
      return session.query(Countries.CountryName).filter_by(CountryCode=code).first()[0]


