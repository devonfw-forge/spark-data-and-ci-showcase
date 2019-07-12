from unittest import TestCase


class TestAnalyse(TestCase):

    def setUp(self):
        self.data = Analyse()

    def test_countries_first_country(self):
        self.assertEqual(self.data.countries()[0], 'Aruba')

    def test_countries_last_country(self):
        self.assertEqual(self.data.countries()[-1], 'Zimbabwe')

    def test_countries_random_country(self):
        self.assertNotEqual(self.data.countries()[50], 'Angola')

    def test_code_to_name_Aruba(self):
        self.assertEqual(self.data.code_to_name('ABW'), 'Aruba')

    def test_code_to_name_Spain(self):
        self.assertEqual(self.data.code_to_name('ESP'), 'Spain')

    def test_code_to_name_Belgium(self):
        self.assertNotEqual(self.data.code_to_name('ARM'), 'Belgium')

    def test_name_to_code_Angola(self):
        self.assertEqual(self.data.name_to_code('Angola'), 'AGO')

    def test_name_to_code_Burundi(self):
        self.assertEqual(self.data.name_to_code('Burundi'), 'BDI')

    def test_name_to_code_France(self):
        self.assertNotEqual(self.data.name_to_code('France'), 'AND')

    def test_countries_data_Aruba_first_gdp(self):
        self.assertEqual(self.data.countries_data(['Aruba'], [1960, 1970])['Aruba'][0][1], '')

    def test_countries_data_Spain_first_gdp(self):
        self.assertEqual(self.data.countries_data(['Spain', 'Andorra'], [1960, 1970])['Spain'][0][1], 12072126075.397)

    def test_countries_data_Zimbabwe_last_gdp(self):
        self.assertNotEqual(self.data.countries_data(['Zimbabwe'], [1960, 2018])['Zimbabwe'][-1][1], 0)
  
    def test_max_growth_of_afghanistan_and_angola_between_1990_2000(self):
        self.assertEqual(self.data.max_growth(["Afghanistan","Angola"],[1990,2000]), 15.0000000288634)

    def test_min_growth_of_afghanistan_and_angola_between_1990_2000(self):
        self.assertEqual(self.data.min_growth(["Afghanistan","Angola"],[1990,2000]), -23.9834174420578)

    def test_max_growth_of_zambia_and_zimbabwe_between_1990_2000(self):
        self.assertEqual(self.data.max_growth(["Zambia","Zimbabwe"],[1990,2000]), 10.3606967698065)

    def test_min_growth_of_zambia_and_zimbabwe_between_1990_2000(self):
        self.assertEqual(self.data.min_growth(["Zambia","Zimbabwe"],[1990,2000]), -9.01557008626092)
    
    def test_av_gdp_Armenia_Comoros_Bahrain_1990_1995(self):
        self.assertEqual(self.data.av_gdp(["Armenia", "Comoros", "Bahrain"], [1990, 1995]), {'Armenia': 1597122009.636872, 'Comoros': 413608659.37108946, 'Bahrain': 5035726950.35461})

    def test_av_gdp_Madagascar_Poland_Sudan_2001_2006(self):
        self.assertNotEqual(self.data.av_gdp(["Madagascar", "Poland", "Sudan"], [2001, 2006]), {'Madagascar': 48861984.861827, 'Poland': 2521170662.67905, 'Sudan': 215728296.915783})

    def test_av_growth_Armenia_Comoros_Bahrain_1990_1995(self):
        self.assertNotEqual(self.data.av_growth(["Armenia", "Comoros", "Bahrain"], [1990, 1995]), {'Qatar': 48861984.861827, 'Poland': 2521170662.67905, 'Senegal': 215728296.915783})

    def test_av_gdp_Madagascar_Poland_Sudan_2001_2006(self):
        self.assertEqual(self.data.av_growth(["Madagascar", "Poland", "Sudan"], [2001, 2006]), {'Madagascar': 3.0019064949716667, 'Poland': 3.6101258971329564, 'Sudan': 7.016596579021644})

    def test_min_gdp_Luxembourg_Lesotho_Libya_1960_2018(self):
        self.assertEqual(self.data.min_gdp(["Luxembourg", "Lesotho", "Libya"],[1960, 2018]), 34579308.4138317)

    def test_min_gdp_Brazil_North_America_1960_2018(self):
        self.assertNotEqual(self.data.min_gdp(["Brazil", "North America"], [1984, 2018]), 2023912696.839)

    def test_max_gdp_Luxembourg_Lesotho_Libya_1960_2018(self):
        self.assertEqual(self.data.max_gdp(["Luxembourg", "Lesotho", "Libya"],[1960, 2018]), 69487922619.3401)

    def test_max_gdp_Brazil_North_America_1960_2018(self):
        self.assertNotEqual(self.data.max_gdp(["Brazil", "North America"], [1984, 2018]), 2023912696.839)

