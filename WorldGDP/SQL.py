from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import csv
from difflib import SequenceMatcher


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

    def list_countries(self):
        '''
        Return the list of all the countries
        :return: list_countries
        '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()
        list_countries = [x[0] for x in session.query(Countries.CountryName).all()]
        session.close()
        return list_countries

    def geo_zone(self):
        '''
        Returns a dictionary that associates each country with it zone.
        :return: geo_dic
        '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()

        geo_dic = {}
        dataCountry = []
        dataZone = []

        with open("Book1.csv") as csv_file:
            for row in csv.reader(csv_file, delimiter=';'):
                dataCountry.append(row[0])
                dataZone.append(row[1])
        for i, country in enumerate(dataCountry):
            if country in self.list_countries():
                geo_dic[country] = dataZone[i]
        session.close()
        return geo_dic

    def countries_code(self):
        '''
        Returns the list of all the countries' codes.
        :return: countries_code
        '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()
        countries_code = [x[0] for x in session.query(Countries.CountryCode).all()]
        session.close()
        return countries_code

    def code_to_name(self, code):
        '''
        Returns the name of the country from its country code.
        :param code:
        :return: name
        '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()
        name = session.query(Countries.CountryName).filter_by(CountryCode=code).first()[0]
        session.close()
        return name

    def name_to_code(self, name):
        '''
        Returns the name of the country from its country code.
        :param name:
        :return: code
        '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()
        code = session.query(Countries.CountryCode).filter_by(CountryName=name).first()[0]
        session.close()
        return code

    def similar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def countries_data(self, countries, years):
        '''
        Returns a dictionary of countries with each country a list of years with a data set (gdp and growth).
        :param countries:
        :param years:
        :return: countries_data_dic
        '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()

        countries_data_dic = {}
        years_vect = [x for x in range(years[0], years[1] + 1)]
        for country in countries:
            countries_data_dic[country] = list(session.query(Gdp.Year, Gdp.gdp, Gdp.growth)\
                .filter_by(CountryCode=self.name_to_code(country)).filter(Gdp.gdp != '').filter(Gdp.Year.in_(years_vect)).all())
            for i, elt in enumerate(countries_data_dic[country]):
                countries_data_dic[country][i] = list(countries_data_dic[country][i])

        session.close()
        return countries_data_dic

    def average_gdp(self, countries, years):
        '''
        Returns the average value of the gdp for a country list and a fixed period.
        :param countries:
        :param years:
        :return: av_dic
        '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()

        av_dic = {}
        for country in countries:
            CC = self.name_to_code(country)
            years_vec = [x for x in range(years[0], years[1] + 1)]
            av_dic[country] = session.query(func.avg(Gdp.gdp))\
                .filter_by(CountryCode=CC).filter(Gdp.gdp != '').filter(Gdp.Year.in_(years_vec)).first()[0]
        session.close()
        return av_dic

    def average_growth(self, countries, years):
        '''
        Returns the average value of the growth for a country list and a fixed period.
        :param countries:
        :param years:
        :return: av_dic
        '''
        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()

        av_dic = {}
        for country in countries:
            CC = self.name_to_code(country)
            years_vect = [x for x in range(years[0], years[1] + 1)]
            av_dic[country] = session.query(func.avg(Gdp.growth)) \
                .filter_by(CountryCode=CC).filter(Gdp.growth != '').filter(Gdp.Year.in_(years_vect)).first()[0]
        session.close()
        return av_dic

    def world_health(self, years):
        '''
        Returns the world health and the geographic place of the countries in crisis
        :param years:
        :return: world health, region dic and unknown countries number
        '''
        crisis = 0
        exception = 0
        health = 0
        unknown_countries = 0
        dic = self.geo_zone()
        dic_keys = list(dic.keys())
        region_dic ={'Asia & Pacific':0 ,'Europe':0 , 'Arab States':0 , 'Africa':0 , \
                      'South/Latin America':0 , 'Unknown':0, 'North America':0}

        for country in self.list_countries():

            past_gdp = self.average_growth([country], [years[0]-5, years[0]-1])[country]
            now_gdp = self.average_growth([country], years)[country]

            if past_gdp == None or now_gdp == None:
                exception += 1
            else:

                if now_gdp < past_gdp:
                    crisis += 1
                    for elt in dic_keys:
                        if self.similar(elt, country) > 0.7:
                            region = dic[elt]
                            region_dic[region] += 1
                            break

                else:
                    health += 1

        list_countries_len = len(self.list_countries())
        health_percentage = (health / list_countries_len)*100
        crisis_percentage = (crisis / list_countries_len)*100
        exception_percentage = (exception / list_countries_len)*100

        print("Percentage of healthy countries : {}% \nPercentage of countries in crisis : {}% \nPercentage of not enougth data : {}%"\
              .format(round(health_percentage), round(crisis_percentage), round(exception_percentage)))

        max_of_three = max([health_percentage, crisis_percentage, exception_percentage ])

        if max_of_three == exception_percentage:
            return ('Not enought data')

        elif max_of_three == crisis_percentage:
            return ('World in crisis', region_dic, unknown_countries)

        elif max_of_three == health_percentage:
            return ('World is good', region_dic, unknown_countries)

    def min_gdp(self, listOfCountries, years):
        '''
        Returns the minimum gdp of each countries of listOfCountries for the given period years, and the global minimum
        :param listOfCountries:
        :param years:
        :return: global min and min for each country
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
        session.close()
        return min(list(list_of_code.values())), list_of_code

    def max_gdp(self, listOfCountries, years):
        '''
         Returns the maximum gdp of each countries of listOfCountries for the given period years, and the global maximum
         :param listOfCountries:
         :param years:
         :return: global max and max for each country
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
        session.close()
        return max(list(list_of_code.values())), list_of_code

    def min_growth(self, listOfCountries, years):
        '''
         Returns the minimum growth of each countries of listOfCountries for the given period years, and the global minimum
         :param listOfCountries:
         :param years:
         :return: global min and min for each country
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
        session.close()
        return min(list(list_of_code.values())), list_of_code

    def max_growth(self, listOfCountries, years):
        '''
         Returns the maximum growth of each countries of listOfCountries for the given period years, and the global maximum
         :param listOfCountries:
         :param years:
         :return: global max and max for each country
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
        session.close()
        return max(list(list_of_code.values())), list_of_code
    
        
        def av_gdp_growth_prod(self, countries_list, years_list, production_type):
        '''
        Returns a list with the countries and their average gdp, growth and production in years_list
        '''

        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()

        gdp = []
        growth = []
        prod = []
        f = Fao()
        result_list = {}
        for country in countries_list:

            growth.append(list(self.av_growth([country], years_list).values())[0])
            gdp.append(list(self.av_gdp([country], years_list).values())[0])
            prod.append(list(f.average_production([country], years_list, production_type, "Food").values())[0])


            result_list[country] = ["average growth: "+str(list(self.av_growth([country], years_list).values())[0]),"average gdp: "+str(list(self.av_gdp([country], years_list).values())[0]), "average production: "+ str(list(f.average_production([country], years_list, production_type, "Food").values())[0])]

        return result_list
        print(prod)
        session.close()

    def conclusion_gdp_growth_prod(self, countries_list, year_range_1, year_range_2, production_type):
        '''
        Returns a list with the countries and their average gdp, growth and production in years_list
         '''

        data_tables = create_engine('sqlite:///world-gdp.db')
        Session = sessionmaker(bind=data_tables)
        session = Session()

        gdp = []
        growth = []
        prod = []
        diff_growth =[]
        diff_gdp = []
        diff_prod = []
        f = Fao()
        diff = []

        for country in countries_list:
            for fao_country in f.list_countries():
                if self.similar(country, fao_country) == 1:

                    growth.append(list(self.av_growth([country], year_range_1).values())[0])
                    gdp.append(list(self.av_gdp([country], year_range_1).values())[0])
                    prod.append(list(f.average_production([country], year_range_1, production_type, "Food").values())[0])

                    growth.append(list(self.av_growth([country], year_range_2).values())[0])
                    gdp.append(list(self.av_gdp([country], year_range_2).values())[0])
                    prod.append(list(f.average_production([country], year_range_2, production_type, "Food").values())[0])
                    break

        for i in range(0,2*len(countries_list),2):
                diff_growth.append(growth[i + 1] - growth[i])
                diff_gdp.append(gdp[i + 1] - gdp[i])
                diff_prod.append(prod[i + 1] - prod[i])

        for i in range(len(diff_prod)):
            diff+=[str(countries_list[i])+": 'growth difference' : "+str(diff_growth[i]) + ": 'gdp difference' : "+str(diff_gdp[i]) +", production difference : "+str(diff_prod[i])]
        return diff

        session.close()

A= Analyse()
f = Fao()




#print(A.conclusion_gdp_growth_prod(liste,year_range_1, year_range_2, f.country_products(liste)))


L= ['Afghanistan', 'Albania', 'Algeria', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'Colombia', 'Costa Rica']

#print(L)

#print(A.av_gdp_growth_prod(L,[1985,1989], f.country_products(L)))
#print(A.av_gdp_growth_prod(L,[1990,1992], f.country_products(L)))
print(A.conclusion_gdp_growth_prod(L,[1985,1989], [1990,1992], f.country_products(L)))
