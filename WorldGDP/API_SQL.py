from SQL import Analyse


class ApiSql:

    def __init__(self):
        '''
        Initializes the class
        '''
        self.DB = Analyse()

    def list_presents_countries(self):
        return self.DB.countries()

    def country_name_with_code(self, country_code):
        return self.DB.code_to_name(country_code)

    def country_code_with_name(self, country_name):
        return self.DB.name_to_code(country_name)

    def dict_data_countries(self, countries_list, years_filter):
        return self.DB.countries_data(countries_list,years_filter)

    def dict_average_gdp_countries(self, countries_list, years_filter):
        return self.DB.av_gdp(countries_list, years_filter)

    def dict_average_growth_countries(self, countries_list, years_filter):
        return self.DB.av_growth(countries_list, years_filter)

    def min_gdp_countries(self, countries_list, years_filter):
        return self.DB.min_gdp(countries_list, years_filter)

    def max_gdp_countries(self, countries_list, years_filter):
        return self.DB.max_gdp(countries_list, years_filter)

    def min_growth_countries(self, countries_list, years_filter):
        return self.DB.min_growth(countries_list, years_filter)

    def max_growth_countries(self, countries_list, years_filter):
        return self.DB.max_growth(countries_list, years_filter)


DB = ApiSql()
print(DB.max_gdp_countries(["Afghanistan", "Angola"], [1990, 2000]))
print(DB.min_gdp_countries(["Afghanistan", "Angola"], [1990, 2000]))
print(DB.max_growth_countries(["Afghanistan", "Angola"], [1990, 2000]))
print(DB.list_presents_countries())
print(DB.dict_data_countries(["Afghanistan", "Angola"], [1990, 2000]))
print(DB.dict_average_growth_countries(["Afghanistan", "Angola"], [1990, 2000]))
