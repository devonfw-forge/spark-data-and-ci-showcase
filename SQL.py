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


   def countries(self):
      country_list = []
      for country in session.query(Gdp.CountryCode).all():
         if self.code_to_name(country[0]) not in country_list:
            country_list.append(self.code_to_name(country[0]))

      return country_list

   def code_to_name(self, code):
      return session.query(Countries.CountryName).filter_by(CountryCode=code).first()[0]

   def name_to_code(self, name):
      return session.query(Countries.CountryCode).filter_by(CountryName=name).first()[0]

   def data_country(self, country):
      data_country = []
      for line in session.query(Gdp).filter_by(CountryCode=self.name_to_code(country)).all():
         data_country.append([line.Year, line.gdp, line.growth])
      return data_country

   def countries_data(self):
      countries_data_list = {}
      for country in self.countries():
         countries_data_list[country] = self.data_country(country)

      return countries_data_list
   
   def av_growth(self, countries, years):
      av_list = {}
      for country in countries:
         CC = self.name_to_code(country)
         av_list[country] = session.query(func.avg(Gdp.growth)).filter_by(CountryCode=CC).filter(Gdp.Year.in_(years)).first()[0]
      
      return av_list

