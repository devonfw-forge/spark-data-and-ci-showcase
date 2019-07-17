from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Gdp(Base):
    '''
   Initializes the Gdp table.
   '''

    __tablename__ = 'gdp'

    id = Column(Integer, primary_key=True)
    CountryCode = Column(String)
    Year = Column(Integer)
    gdp = Column(Integer)
    growth = Column(Integer)


class Countries(Base):
    '''
   Initializes the countries table.
   '''

    __tablename__ = 'countries'

    CountryCode = Column(String, primary_key=True)
    CountryName = Column(String)


class Analyse:
    '''
   Class with all the data analyse functions.
   '''

    def countries(self):
        '''
      Returns the list of all the countries.
      '''

        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()
        return [x[0] for x in session.query(Countries.CountryName).all()]
        session.close()
        
    def countries_code(self):
        '''
      Returns the list of all the countries.
      '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()
        return [x[0] for x in session.query(Countries.CountryCode).all()]
        session.close()

    def code_to_name(self, code):
        '''
      Returns the name of the country from its country code.
      '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()
        return session.query(Countries.CountryName).filter_by(CountryCode=code).first()[0]
        session.close()

    def name_to_code(self, name):
        '''
      Returns the code of the country from its country name.
      '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()
        return session.query(Countries.CountryCode).filter_by(CountryName=name).first()[0]
        session.close()

    def countries_data(self, countries, years):
        '''
      Returns a list of countries with each country a list of years with a dataset (gdp and growth).
      '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()

        countries_data_list = {}
        years_vect = [x for x in range(years[0], years[1] + 1)]
        for country in countries:
            countries_data_list[country] = list(session.query(Gdp.Year, Gdp.gdp, Gdp.growth). \
                filter_by(CountryCode=self.name_to_code(country)).filter(Gdp.Year.in_(years_vect)).all())
            for i, elt in enumerate(countries_data_list[country]):
                countries_data_list[country][i] = list(countries_data_list[country][i])
                if elt[1] == '':
                    countries_data_list[country][i][1] = 0
                if elt[2] == '':
                    countries_data_list[country][i][2] = 0

        return countries_data_list
        session.close()

    def av_gdp(self, countries, years):
        '''
      Returns the average value of the gdp for a country list and a fixed period.
      '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()

        av_list = {}
        for country in countries:
            CC = self.name_to_code(country)
            years_vec = [x for x in range(years[0], years[1] + 1)]
            av_list[country] = \
            session.query(func.avg(Gdp.gdp)).filter_by(CountryCode=CC).filter(Gdp.Year.in_(years_vec)).first()[0]
        return av_list
        session.close()

    def av_growth(self, countries, years):
        '''
      Returns the average value of the growth for a country list and a fixed period.
      '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()

        av_list = {}
        for country in countries:
            CC = self.name_to_code(country)
            years_vect = [x for x in range(years[0], years[1] + 1)]
            av_list[country] = \
            session.query(func.avg(Gdp.growth)).filter_by(CountryCode=CC).filter(Gdp.Year.in_(years_vect)).first()[0]
        return av_list
        session.close()

    def min_gdp(self, listOfCountries, years):
        '''
      Returns the minimum gdp between countries of listOfCountries for the given period years
      '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()

        list_of_code = {}
        for country in listOfCountries:
            name = self.name_to_code(country)
            years_vect = [x for x in range(years[0], years[1] + 1)]
            list_of_code[country] = \
            session.query(func.min(Gdp.gdp)).filter_by(CountryCode=name).filter(Gdp.Year.in_(years_vect)).first()[0]
        for elt in list(list_of_code.items()):
            if elt[1] == '':
                list_of_code[elt[0]] = 0
        return min(list(list_of_code.values())), list_of_code
        session.close()

    def max_gdp(self, listOfCountries, years):
        '''
      Returns the maximum gdp between countries of listOfCountries for the given period years
      '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()

        list_of_code = {}
        for country in listOfCountries:
            name = self.name_to_code(country)
            years_vect = [x for x in range(years[0], years[1] + 1)]
            list_of_code[country] = \
            session.query(func.max(Gdp.gdp)).filter_by(CountryCode=name).filter(Gdp.Year.in_(years_vect)).first()[0]
        for elt in list(list_of_code.items()):
            if elt[1] == '':
                list_of_code[elt[0]] = 0
        return max(list(list_of_code.values())), list_of_code
        session.close()

    def min_growth(self, listOfCountries, years):
        '''
      Returns the minimum growth between countries of listOfCountries for the given period years
      '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()

        list_of_code = {}
        for country in listOfCountries:
            name = self.name_to_code(country)
            years_vect = [x for x in range(years[0], years[1] + 1)]
            list_of_code[country] = \
            session.query(func.min(Gdp.growth)).filter_by(CountryCode=name).filter(Gdp.Year.in_(years_vect)).first()[0]
        for elt in list(list_of_code.items()):
            if elt[1] == '':
                list_of_code[elt[0]] = 0
        return min(list(list_of_code.values())), list_of_code
        session.close()

    def max_growth(self, listOfCountries, years):
        '''
      Returns the maximum growth between countries of listOfCountries for the given period years
      '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()

        list_of_code = {}
        for country in listOfCountries:
            name = self.name_to_code(country)
            years_vect = [x for x in range(years[0], years[1] + 1)]
            list_of_code[country] = \
            session.query(func.max(Gdp.growth)).filter_by(CountryCode=name).filter(Gdp.Year.in_(years_vect)).first()[0]
        for elt in list(list_of_code.items()):
            if elt[1] == '':
                list_of_code[elt[0]] = 0
        return max(list(list_of_code.values())), list_of_code
        session.close()
