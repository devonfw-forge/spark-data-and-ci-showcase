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

    def countries(self):
        '''
        Returns the list of all the countries
        '''
        country_list = []
        for country in self.dataBase:
            country_list.append(country[0])
        return country_list

    def population(self, country, list_years):
        '''
        Returns, for a country and a period given, the list of the population
        '''
        years = [str(x) for x in list_years]

        for current_country in self.dataBase:
            if current_country[0] == country:
                pop = current_country[self.dataHead.index(years[0]): self.dataHead.index(years[1]) + 1]

        for elt in pop:
            if elt == "":
                pop[pop.index(elt)] = '0'
            pop[pop.index(elt)] = int(pop[pop.index(elt)])
        return pop

    def countries_pop(self, countries, list_years):
        '''
        Returns, for a list of countries and a period given, the list of the population for each country
        '''
        final_list = {}
        years = [str(x) for x in list_years]
        for country in countries:
            final_list[country] = self.population(country, years)
        return final_list

    def growth(self, listOfCountries, list_years):
        '''
        returns, for a given list of countries and year range, the list of the growth for each country
        '''
        
        indiceMin = 0
        indiceMax = 0
        result = {}
        years = [str(x) for x in years_l]
        for country in self.dataBase:

            if country[0] in listOfCountries:
                for i in range(len(self.dataHead)):
                    if years[0] == self.dataHead[i]:
                        indiceMin = i
                    if years[1] == self.dataHead[i]:
                        indiceMax = i

                minimum = country[indiceMin]
                maximum = country[indiceMax]


                difference = int(maximum) - int(minimum)
                result[country[0]] = difference

        return result

    def indexYear(self, years_l):
        years = [str(x) for x in years_l]
        list_year = []
        list_year.append(self.dataHead[4:63])
        indexA = list_year[0].index(years[0]) + 4
        indexB = list_year[0].index(years[1]) + 4
        return indexA, indexB

    def indexCountries(self, country_list):
        indexes = []
        for i in country_list:
            indexes.append(self.countries().index(i))
        return indexes

    def minPoblacion(self, country_list, years_l):
        years = [str(x) for x in years_l]
        list1 = []
        list2 = []
        listeInt = []
        listeStr = []
        indexesCountries = self.indexCountries(country_list)
        indexYears = self.indexYear(years)

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

    def maxPoblacion(self, country_list, years_l):
        years = [str(x) for x in years_l]
        list1 = []
        list2 = []
        listeInt = []
        listeStr = []
        indexesCountries = self.indexCountries(country_list)
        indexYears = self.indexYear(years)

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





                

            

    
    
