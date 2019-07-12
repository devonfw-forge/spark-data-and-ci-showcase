from unittest import TestCase


class TestAnalyse(TestCase):

    def setUp(self):
        self.data = Analyse()

    def test_countries(self):
        self.assertEqual(self.data.countries()[0], 'Aruba')

    def test_countries2(self):
        self.assertEqual(self.data.countries()[-1], 'Zimbabwe')

    def test_countries3(self):
        self.assertNotEqual(self.data.countries()[50], 'Angola')

    def test_code_to_name(self):
        self.assertEqual(self.data.code_to_name('ABW'), 'Aruba')

    def test_code_to_name2(self):
        self.assertEqual(self.data.code_to_name('ESP'), 'Spain')

    def test_code_to_name3(self):
        self.assertNotEqual(self.data.code_to_name('ARM'), 'Belgium')

    def test_name_to_code(self):
        self.assertEqual(self.data.name_to_code('Angola'), 'AGO')

    def test_name_to_code2(self):
        self.assertEqual(self.data.name_to_code('Burundi'), 'BDI')

    def test_name_to_code3(self):
        self.assertNotEqual(self.data.name_to_code('France'), 'AND')

    def test_data_country(self):
        self.assertEqual(self.data.data_country('Aruba')[0][1], '')

    def test_data_country2(self):
        self.assertEqual(self.data.data_country('Zimbabwe')[-1][1], 31000519447.175)

    def test_data_country3(self):
        self.assertNotEqual(self.data.data_country('Spain')[0][0], 1980)
    
        def test_max_growth_of_afghanistan_and_angola_between_1990_2000(self):
        self.assertEqual(self.data.max_growth(["Afghanistan","Angola"],[1990,2000]), 15.0000000288634)

    def test_min_growth_of_afghanistan_and_angola_between_1990_2000(self):
        self.assertEqual(self.data.min_growth(["Afghanistan","Angola"],[1990,2000]), -23.9834174420578)

    def test_max_growth_of_zambia_and_zimbabwe_between_1990_2000(self):
        self.assertEqual(self.data.max_growth(["Zambia","Zimbabwe"],[1990,2000]), 10.3606967698065)

    def test_min_growth_of_zambia_and_zimbabwe_between_1990_2000(self):
        self.assertEqual(self.data.min_growth(["Zambia","Zimbabwe"],[1990,2000]), -9.01557008626092)

