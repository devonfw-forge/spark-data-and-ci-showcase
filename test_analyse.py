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

