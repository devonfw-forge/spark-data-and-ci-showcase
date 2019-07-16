from WORLD_BANK import WorldBank


class ApiWorldBank:

    def __init__(self):
        '''
        Initializes the class
        '''
        self.WB = WorldBank()

    def dict_presents_countries(self):
        return self.WB.countries()

    def dict_country_populations(self, country_name, years_filter):
        return self.WB.population(country_name, years_filter)

    def dict_countries_populations(self, countries_list, years_filter):
        return self.WB.countries_pop(countries_list, years_filter)

    def dict_countries_growth(self, countries_list, years_filter):
        return self.WB.growth(countries_list, years_filter)

    def dict_min_of_countries_populations(self, countries_list, years_filter):
        return self.WB.minPoblacion(countries_list, years_filter)

    def dict_max_of_countries_populations(self, countries_list, years_filter):
        return self.WB.maxPoblacion(countries_list, years_filter)


WB = ApiWorldBank()
print(WB.dict_countries_populations(["Afghanistan", "Angola"], ['1990', '2000']))
print(WB.dict_min_of_countries_populations(["Afghanistan", "Angola"], ['1990', '2000']))
print(WB.dict_country_populations("Angola", ['1990', '2000']))
print(WB.dict_presents_countries())
print(WB.dict_max_of_countries_populations(["Afghanistan", "Angola"], ['1990', '2000']))