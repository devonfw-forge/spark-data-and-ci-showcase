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



