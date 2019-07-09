import json


class Fao:

    def __init__(self):
        file = open("FAO+database.json", 'r')
        self.dataBase = json.load(file)

    def countries(self):
        country_list = []
        for element in self.dataBase:
            if element["Area"] not in country_list:
                country_list.append(element["Area"])
        return country_list
    
    def products(self, nameCountry): #function to have a list a product given the name country
        productList = []
        for elt in self.dataBase:
            if elt["Area"] == nameCountry:
                if elt["Item"] not in productList:
                    productList.append(elt["Item"])
        print(productList)

if __name__ == '__main__':

    FAO1 = FAO()
    FAO1.products("Zimbabwe")

