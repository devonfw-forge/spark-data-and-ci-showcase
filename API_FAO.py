from FAO import Fao


class ApiFao:

    def __init__(self):
        '''
        Initializes the class
        '''
        self.fao1 = Fao()

    def list_presents_countries(self):
        return self.fao1.countries()

    def list_products_of_country(self, country_name):
        return self.fao1.products(country_name)

    def dict_products_of_countries(self, countries_list):
        return self.fao1.country_prod(countries_list)

    def dict_max_of_countries_productions(self, countries_list, years_filter):
        return self.fao1.max(countries_list, years_filter)

    def dict_min_of_countries_productions(self, countries_list, years_filter):
        return self.fao1.min(countries_list, years_filter)

    def dict_avg_of_countries_productions(self, countries_list, years_filter, production_filter, food_or_feed):
        return self.fao1.av(countries_list, years_filter, production_filter, food_or_feed)


fao1 = ApiFao()
print(fao1.dict_avg_of_countries_productions(["Afghanistan", "Angola"], [1990, 2000], "Wheat and products", "Food"))
print(fao1.dict_min_of_countries_productions(["Afghanistan", "Angola"], [1990, 2000]))
print(fao1.list_products_of_country("Angola"))
print(fao1.dict_max_of_countries_productions(["Afghanistan", "Angola"], [1990, 2000]))
print(fao1.list_presents_countries())






