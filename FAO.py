import json


class Fao:

    def __init__(self):
        '''
        Initializes the class by importing the data from the file
        '''
        file = open("FAO+database.json", 'r')
        self.dataBase = json.load(file)
        file.close()

    def countries(self):
        '''
        Returns all countries present in the file without doubles.
        '''
        country_list = []
        for element in self.dataBase:
            if element["Area"] not in country_list:
                country_list.append(element["Area"])
        return country_list

    def products(self, country):
        '''
        Returns all products for a given country.
        '''
        products_list = []
        for element in self.dataBase:
            if element["Area"] == country and element["Item"] not in products_list:
                products_list.append(element["Item"])
        return products_list

        def max(self, country_list, years):
        '''
        Returns the maximum of production (production, year and quantity) for some given countries and a fixed date.
        '''
        country_dic = {}
        years_list = []

        for date in range(years[0], years[-1]+1):
            years_list.append("Y" + str(date))

        for country in country_list:
            country_dic[country] = ["init", "Yinit", 0]
            othermax = []

            for production in self.products(country):

                for element in self.dataBase:

                    if element["Area"] == country and element["Item"] == production:
                        currentyield = {key: element[key] for key in years_list}

                        if currentyield[max(currentyield)] > country_dic[country][-1]:
                            country_dic[country] = [production, max(currentyield), currentyield[max(currentyield)]]

                        elif currentyield[max(currentyield)] == country_dic[country][-1]:
                            othermax.append([production, max(currentyield), currentyield[max(currentyield)]])

            if othermax != []:
                country_dic[country] = [country_dic[country], othermax]

        return country_dic

    def min(self, country_list, years):
        '''
        Returns the minimum of production (production, year and quantity) for some given countries and a fixed date.
        '''
        country_dic = {}
        years_list = []

        for date in range(years[0], years[-1]+1):
            years_list.append("Y" + str(date))

        for country in country_list:
            country_dic[country] = ["init", "Yinit", float('inf')]
            othermin = []

            for production in self.products(country):

                for element in self.dataBase:

                    if element["Area"] == country and element["Item"] == production:
                        currentyield = {key: element[key] for key in years_list}

                        if currentyield[min(currentyield)] < country_dic[country][-1]:
                            country_dic[country] = [production, min(currentyield), currentyield[min(currentyield)]]

                        elif currentyield[min(currentyield)] == country_dic[country][-1]:
                            othermin.append([production, min(currentyield), currentyield[min(currentyield)]])

            if othermin != []:
                country_dic[country] = [country_dic[country], othermin]

        return country_dic



    
    def products(self, nameCountry): #function to have a list a product given the name country
        productList = []
        for elt in self.dataBase:
            if elt["Area"] == nameCountry:
                if elt["Item"] not in productList:
                    productList.append(elt["Item"])
        return productList

if __name__ == '__main__':

    FAO1 = FAO()
    FAO1.products("Zimbabwe")

