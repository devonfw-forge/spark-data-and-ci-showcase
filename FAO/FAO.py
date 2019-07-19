import json
import statistics
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'FAO+database.json')

class Fao:

    def __init__(self):
        '''
        Initializes the class by importing the data from the file
        '''
        file = open(my_file, 'r')
        self.dataBase = json.load(file)
        file.close()

    def list_countries(self):
        '''
        Returns a list of all countries present in the file without doubles.
        :return: country_list
        '''
        country_list = []
        for element in self.dataBase:
            if element["Area"] not in country_list:
                country_list.append(element["Area"])
        return country_list

    def list_products_country(self, country):
        '''
        Returns a list of all the products for a given country.
        :param country:
        :return: products_list
        '''
        products_list = []
        for element in self.dataBase:
            if element["Area"] == country and element["Item"] not in products_list:
                products_list.append(element["Item"])
        return products_list

    def list_products_countries(self, country_list):
        """
        Returns a list of countries with each country its production list.
        :param country_list:
        :return: products_countries_dic
        """
        products_countries_dic = {}
        for country in country_list:
            products_countries_dic[country] = self.list_products_country(country)
        return products_countries_dic

    def max_production(self, country_list, years_range):
        """
        Returns the maximum of production (production, year and quantity) for some given countries and a fixed date.
        :param country_list:
        :param years_range:
        :return: country_dic
        """
        country_dic = {}
        years_list = []

        for date in range(years_range[0], years_range[-1] + 1):
            years_list.append("Y" + str(date))

        for country in country_list:
            country_dic[country] = ["init", "Yinit", 0]
            othermax = []

            for production in self.list_products_country(country):

                for element in self.dataBase:

                    if element["Area"] == country and element["Item"] == production:
                        currentyield = {key: element[key] for key in years_list}

                        for elt in currentyield.items():
                            if elt[1] == "":
                                currentyield[elt[0]] = 0

                        if currentyield[max(currentyield)] > country_dic[country][-1]:
                            country_dic[country] = [production, max(currentyield), currentyield[max(currentyield)]]

                        if othermax != [] and currentyield[max(currentyield)] > othermax[-1][2]:
                            othermax = []

                        elif currentyield[max(currentyield)] == country_dic[country][-1]:
                            othermax.append([production, max(currentyield), currentyield[max(currentyield)]])

            if othermax != []:
                othermax.append(country_dic[country])
                country_dic[country] = othermax

        return country_dic

    def min_production(self, country_list, years_range):
        '''
        Returns the minimum of production (production, year and quantity) for some given countries and a fixed date.
        :param country_list:
        :param years_range:
        :return: country_dic
        '''
        country_dic = {}
        years_list = []

        for date in range(years_range[0], years_range[-1] + 1):
            years_list.append("Y" + str(date))

        for country in country_list:
            country_dic[country] = ["init", "Yinit", float('inf')]
            othermin = []

            for production in self.list_products_country(country):

                for element in self.dataBase:

                    if element["Area"] == country and element["Item"] == production:
                        currentyield = {key: element[key] for key in years_list}


                        for elt in currentyield.items():
                            if elt[1] == "":
                                currentyield[elt[0]] = 0

                        if currentyield[min(currentyield)] < country_dic[country][-1]:
                            country_dic[country] = [production, min(currentyield), currentyield[min(currentyield)]]

                        if othermin != [] and currentyield[min(currentyield)] < othermin[-1][2]:
                            othermin = []

                        if currentyield[min(currentyield)] == country_dic[country][-1]:
                            othermin.append([production, min(currentyield), currentyield[min(currentyield)]])

            if othermin != []:
                othermin.append(country_dic[country])
                country_dic[country] = othermin

        return country_dic

    def min_production_countries(self, country_list, years_range):
        '''
        Returns the minimum of each production (production, year and quantity) for some given countries and a fixed date.
        :param country_list:
        :param years_range:
        :return: country_dic
        '''
        country_dic = {}
        years_list = []

        for date in range(years_range[0], years_range[-1] + 1):
            years_list.append("Y" + str(date))

        for country in country_list:
            prod_list = []
            for production in self.list_products_country(country):

                for element in self.dataBase:

                    if element["Area"] == country and element["Item"] == production:
                        currentyield = {key: element[key] for key in years_list}


                        for elt in currentyield.items():
                            if elt[1] == "":
                                currentyield[elt[0]] = 0

                prod_list.append([production, min(currentyield), currentyield[min(currentyield)]])

        country_dic[country] = prod_list

        return country_dic

    def max_production_countries(self, country_list, years_range):
        '''
         Returns the maximum of each production (production, year and quantity) for some given countries and a fixed date.
         :param country_list:
         :param years_range:
         :return: country_dic
         '''
        country_dic = {}
        years_list = []

        for date in range(years_range[0], years_range[-1] + 1):
            years_list.append("Y" + str(date))

        for country in country_list:
            prod_list = []
            for production in self.list_products_country(country):

                for element in self.dataBase:

                    if element["Area"] == country and element["Item"] == production:
                        currentyield = {key: element[key] for key in years_list}


                        for elt in currentyield.items():
                            if elt[1] == "":
                                currentyield[elt[0]] = 0

                prod_list.append([production, max(currentyield), currentyield[max(currentyield)]])

        country_dic[country] = prod_list

        return country_dic

    def average_production(self, country_list, years_range, production_type, direction):
        '''
        Returns the average of production  for some given countries, a fixed date and a production type given
        :param country_list:
        :param years_range:
        :param production_type:
        :param direction:
        :return: av_dic
        '''
        av_dic = {}
        years_list = []

        for date in range(years_range[0], years_range[-1] + 1):
            years_list.append("Y" + str(date))

        for country in country_list:
            for prod in production_type:
                result_list = []
                for element in self.dataBase:
                    if element["Area"] == country and element["Item"] in production_type and element["Element"] == direction:

                        for i in years_list:
                            if element[i] == "":
                                element[i] = 0
                            result_list.append(element[i])
                av_dic[country] = statistics.mean(result_list)

        return av_dic

    def country_products(self, listOfCountries):
        '''
        Returns all products for a given country.
        '''
        products_list = []
        for country in listOfCountries:
            for element in self.dataBase:
                if element["Area"] == country and element["Item"] not in products_list:
                    products_list.append(element["Item"])
        return products_list
    
    



