import csv


class WorldBank:

    def __init__(self):
        '''
        Starts the class by saving the file data and the name of the columns in two different attributes
        '''
        self.dataBase = []
        self.dataHead = []
        with open("API_SP.POP.TOTL_DS2_en_csv_v2_162.csv") as csv_file:
            for row in csv.reader(csv_file, delimiter=','):
                self.dataBase.append(row)
        self.dataHead = self.dataBase[4]
        self.dataBase = self.dataBase[5:]

    def list_countries(self):
        '''
        Returns the list of all the countries
        :return: country_list
        '''
        country_list = []
        for country in self.dataBase:
            country_list.append(country[0])
        return country_list

    def list_population(self, country, years):
        '''
        Returns, for a country and a period given, the list of the population
        :param country:
        :param years:
        :return: population_list
        '''
        years_list_str = [str(x) for x in years]

        for current_country in self.dataBase:
            if current_country[0] == country:
                population_list = current_country[self.dataHead.index(years_list_str[0]): self.dataHead.index(years_list_str[1]) + 1]

        for elt in population_list:
            if elt == "":
                population_list[population_list.index(elt)] = '0'
            population_list[population_list.index(elt)] = int(population_list[population_list.index(elt)])
        return population_list

    def countries_population(self, countries, years):
        '''
        Returns, for a list of countries and a period given, the list of the population of each country
        :param countries:
        :param years:
        :return:population_dic
        '''
        population_dic = {}
        years_list_str = [str(x) for x in years]
        for country in countries:
            population_dic[country] = self.list_population(country, years_list_str)
        return population_dic

    def growth_countries_in_years_range(self, listOfCountries, years):
        '''
        Returns a dictionary with the growth of each country given in a fixed period
        :param listOfCountries:
        :param years:
        :return: growth_dic
        '''
        indiceMin = 0
        indiceMax = 0
        growth_dic = {}
        years_list_str = [str(x) for x in years]
        for country in self.dataBase:

            if country[0] in listOfCountries:
                for i in range(len(self.dataHead)):
                    if years_list_str[0] == self.dataHead[i]:
                        indiceMin = i
                    if years_list_str[1] == self.dataHead[i]:
                        indiceMax = i

                minimum = country[indiceMin]
                maximum = country[indiceMax]

                difference = int(maximum) - int(minimum)
                growth_dic[country[0]] = difference

        return growth_dic

    def index_years(self, years_tuple):
        '''
        Return the indexes in the self.DataHead of the two years entered in the parameter years_tuple. This function help for the min and max functions
        :param years_tuple: this parameter has to be a tuple of two years, which the first is the the beginning of the range and the last the end of it.
        :return: indexA, indexB
        '''
        years = [str(x) for x in years_tuple]
        list_year = []
        list_year.append(self.dataHead[4:63])
        indexA = list_year[0].index(years[0]) + 4
        indexB = list_year[0].index(years[1]) + 4
        return indexA, indexB

    def index_countries(self, country_list):
        '''
            Return a list of indexes encountered in the country_list parameter of the different countries in it. This function help for the min and max functions
            :param country_list: this parameter is the list of countries we want to know the indexes
            :return: indexes
        '''
        indexes = []
        for i in country_list:
            indexes.append(self.list_countries().index(i))
        return indexes

    def min_populations_in_range(self, country_list, years_l):
        '''
            Return the minimum population of each country specified in the list parameter years_l
            :param country_list: this parameter is the list of countries we want to know the minimum population
            :param years_l: this parameter is list of two years in order to apply a range for the study
            :return: dicc: this is the dictionary returned with the countries as the key and the minimum as the value
        '''
        years = [str(x) for x in years_l]
        list1 = []
        list2 = []
        listeInt = []
        listeStr = []
        indexesCountries = self.index_countries(country_list)
        indexYears = self.index_years(years)

        dicc = {}

        for i in indexesCountries:
            list1.append(self.dataBase[i])
        for i in range(len(list1)):
            for j in range(indexYears[0], indexYears[1]):
                list2.append(list1[i][j])
        j = 0
        pas = int(len(list2) / len(indexesCountries))
        for i in range(len(list1)):
            listeStr.append(list2[j:pas])
            j = pas
            pas += pas

        for i in range(len(listeStr)):
            listeStr[i] = [int(i) for i in listeStr[i]]

        for i in range(len(listeStr)):
            listeInt.append(min(listeStr[i]))

        for i, country in enumerate(country_list):
            dicc[country] = listeInt[i]

        return dicc

    def max_populations_in_range(self, country_list, years_l):
        '''
            Return the maximum population of each country specified in the list parameter years_l
            :param country_list: this parameter is the list of countries we want to know the maximum population
            :param years_l: this parameter is list of two years in order to apply a range for the study
            :return: dicc: this is the dictionary returned with the countries as the key and the maximum as the value
        '''
        years = [str(x) for x in years_l]
        list1 = []
        list2 = []
        listeInt = []
        listeStr = []
        indexesCountries = self.index_countries(country_list)
        indexYears = self.index_years(years)

        dicc = {}
        for i in indexesCountries:
            list1.append(self.dataBase[i])
        for i in range(len(list1)):
            for j in range(indexYears[0], indexYears[1]):
                list2.append(list1[i][j])
        j = 0
        pas = int(len(list2) / len(indexesCountries))
        for i in range(len(list1)):
            listeStr.append(list2[j:pas])
            j = pas
            pas += pas

        for i in range(len(listeStr)):
            listeStr[i] = [int(i) for i in listeStr[i]]

        for i in range(len(listeStr)):
            listeInt.append(max(listeStr[i]))

        for i, country in enumerate(country_list):
            dicc[country] = listeInt[i]

        return dicc

