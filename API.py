import csv


class Api:

    def __init__(self):
        self.dataBase = []
        self.dataHead = []
        with open("API_SP.POP.TOTL_DS2_en_csv_v2_162.csv") as csv_file:
            for row in csv.reader(csv_file, delimiter=','):
                self.dataBase.append(row)
        self.dataHead = self.dataBase[4]
        self.dataBase = self.dataBase[5:-1]

    def countries(self):
        country_list = []
        for country in self.dataBase:
            country_list.append(country[0])
        return country_list

    def population(self, country):

        for current_country in self.dataBase:
            if current_country[0] == country:
               pop = current_country[4:-1]

        return pop

    def countries_pop(self, countries):
        final_list = []
        for country in countries:
            int_list = [country]
            int_list.append(self.population(country))
            final_list.append(int_list)
        return final_list

