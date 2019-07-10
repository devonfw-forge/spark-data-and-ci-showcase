import csv


class Api:

    def __init__(self):
        self.dataBase = []
        with open("API_SP.POP.TOTL_DS2_en_csv_v2_162.csv") as csv_file:
            for column in csv.reader(csv_file, delimiter=','):
                self.dataBase.append(column)
        self.dataBase = self.dataBase[4:-1]


