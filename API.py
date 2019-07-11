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

    
    def indexYear(self, years):
        indexA = 0
        indexB = 0
        list_year = []
        list_year.append(self.dataHead[4:63])
        indexA = list_year[0].index(years[0]) + 4
        indexB = list_year[0].index(years[1]) + 4
        return indexA,indexB

    def indexCountries(self, country_list):
        indexes = []
        for i in country_list:
            indexes.append(self.countries().index(i))
        return indexes


    def minPoblacion(self, country_list, years):
        list1 = []
        list2 = []
        listeInt = []
        listeStr = []
        indexesCountries = self.indexCountries(country_list)
        indexYears = self.indexYear(years)
        for i in indexesCountries:
            list1.append(self.dataBase[i])
        for i in range(len(list1)):
            for j in range(indexYears[0], indexYears[1]):
                list2.append(list1[i][j])
        j = 0
        pas = int(len(list2) / len(indexesCountries))
        for i in range(len(list1)):
            listeStr.append(list2[j:pas])
            j=pas
            pas += pas

        for i in range(len(listeStr)):
            listeStr[i] = [int(i) for i in listeStr[i]]

        for i in range(len(listeStr)):
            listeInt.append(min(listeStr[i]))

        return listeInt

    def maxPoblacion(self, country_list, years):
        list1 = []
        list2 = []
        listeInt = []
        listeStr = []
        indexesCountries = self.indexCountries(country_list)
        indexYears = self.indexYear(years)
        for i in indexesCountries:
            list1.append(self.dataBase[i])
        for i in range(len(list1)):
            for j in range(indexYears[0], indexYears[1]):
                list2.append(list1[i][j])
        j = 0
        pas = int(len(list2) / len(indexesCountries))
        for i in range(len(list1)):
            listeStr.append(list2[j:pas])
            j=pas
            pas += pas

        for i in range(len(listeStr)):
            listeStr[i] = [int(i) for i in listeStr[i]]

        for i in range(len(listeStr)):
            listeInt.append(max(listeStr[i]))

        return listeInt


if __name__ == '__main__':

    API1 = Api()
    print(API1.countries())
    print(API1.dataHead)
    print(API1.indexYear(['1971', '2000']))
    print(API1.indexCountries(["Armenia", "Comoros"]))
    print(API1.minPoblacion(["Armenia", "Comoros", "Bahrain"],['1960', '1970']))
    print(API1.maxPoblacion(["Armenia", "Comoros", "Zimbabwe"],['1970', '1980']))
    
   
                

            

    
    
