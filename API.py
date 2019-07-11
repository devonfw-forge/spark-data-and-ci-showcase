import csv


class Api:

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

    def population(self, country, years):
        '''
        Returns, for a country and a period given, the list of the population
        '''

        for current_country in self.dataBase:
            if current_country[0] == country:
                pop = current_country[self.dataHead.index(years[0]) : self.dataHead.index(years[1])+1]
                
        for elt in pop:
            if elt == "":
                pop[pop.index(elt)] = '0'
                
        return pop

    def countries_pop(self, countries, years):
        '''
        Returns, for a list of countries and a period given, the list of the population of each country
        '''
        final_list = []
        for country in countries:
            int_list = [country]
            int_list.append(self.population(country, years))
            final_list.append(int_list)
        return final_list

     def growth(self, listOfCountries, years):

        minimum = 0
        maximum = 0
        indiceMin = 0
        indiceMax = 0
        difference = 0
        result = []

        for country in self.dataBase:


            if country[0] in listOfCountries :
                for i in range(len(self.dataHead)):
                    if years[0] == self.dataHead[i]:
                        indiceMin = i
                    if years[1] == self.dataHead[i]:
                        indiceMax = i

                minimum = country[indiceMin]
                maximum = country[indiceMax]

                difference = int(maximum) - int(minimum)
                result += [country[0]+":"+ str(difference)]
                maximum = 0
                minimum = 0
                difference = 0
                
                    return result
                
        self.int_list = []
        for elt in self.pop:
            integr = []
            for elt2 in elt:
                if elt2 != '':
                    integr.append(int(elt2))
                self.int_list.append(integr)
                
        self.list_max = []               
        for elt in self.int_list:
            if elt != []:
                if max(elt) not in self.list_max:
                    self.list_max.append(max(elt))        
        
        def maxim(self, country):
            if country in self.countries():
                return self.list_max[self.countries.index(country)]
            else:
                return 'error'
            

    
    
