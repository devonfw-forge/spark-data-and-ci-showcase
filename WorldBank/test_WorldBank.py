from unittest import TestCase
from WorldBank import WorldBank


class TestApi(TestCase):
    def setUp(self):
        self.data = WorldBank()

    def test_list_countries(self):
        countries = self.data.list_countries() 
        self.assertEqual(countries[0], "Aruba")
        self.assertNotEqual(countries[1], "Andorra")

    def test_list_population(self):
        countries = self.data.list_countries() 
        self.assertEqual(self.data.list_population(countries[0], [1960, 1962])[0], 54211)

        self.assertNotEqual(self.data.list_population(countries[0], [1960, 1962])[2], 59063)

    def test_countries_population(self):
        countries = self.data.list_countries() 
        self.assertEqual(self.data.countries_population([countries[0], countries[1]], [1960, 1962])[countries[0]][0], 54211)
        self.assertNotEqual(self.data.countries_population([countries[0], countries[1]], [1960, 1962])[countries[1]][1], 57032)

    def test_growth_countries_in_years_range(self):
        countries = self.data.list_countries() 
        self.assertEqual(self.data.growth_countries_in_years_range([countries[0], countries[1]], [1960, 1965]),
                         {countries[0]: 3149, countries[1] : 959347})

        self.assertNotEqual(self.data.growth_countries_in_years_range([countries[0]], [1960, 1961]), {"Aruba": 3149 })

    def test_min_populations_in_range(self):
        countries = self.data.list_countries() 
        self.assertEqual(self.data.min_populations_in_range([countries[8], countries[12], countries[15]], [1960, 1970]),
                         {countries[8]: 1874121, countries[12]: 7047539, countries[15]: 9153489})

        self.assertNotEqual(self.data.min_populations_in_range([countries[7], countries[14], countries[20]], [1960, 1980]),
                            {countries[0]: 1874121, countries[10]: 162427, countries[15]: 191121})

    def test_max_populations_in_range(self):
        countries = self.data.list_countries() 
        self.assertEqual(self.data.max_populations_in_range([countries[8], countries[12], countries[15]], [1970, 1980]),
                         {countries[8]: 3049109, countries[12]: 7599038, countries[15]: 9848382})

        self.assertNotEqual(self.data.max_populations_in_range([countries[0], countries[1], countries[2]], [1960, 1980]),
                            [4587, 191121, 162427])
