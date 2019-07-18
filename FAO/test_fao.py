from unittest import TestCase
from FAO import Fao


class TestFao(TestCase):
    def setUp(self):
        self.data = Fao()

    def test_countries(self):
        countries = self.data.list_countries()
        self.assertEqual(countries[0], "Afghanistan")
        self.assertEqual(countries[42], "Cyprus")
        self.assertEqual(countries[-1], "Zimbabwe")
        self.assertEqual(countries[137], "Senegal")
        self.assertEqual(len(countries), 174)


    def test_products(self):
        countries = self.data.list_countries()
        self.assertEqual(self.data.list_products_countries(countries[0])[0], "Wheat and products")
        self.assertEqual(self.data.list_products_countries(countries[-1])[0], "Wheat and products")

    def test_min(self):
        countries = self.data.list_countries()
        self.assertEqual(self.data.min_production_countries([countries[0]], [2010, 2013])[countries[0]][0][-1], 0)

    def test_max(self):
        countries = self.data.list_countries()
        self.assertEqual(self.data.max_production_countries([countries[0]], [2010, 2013])[countries[0]][-1], 5495)

    def test_average_production(self):
        countries = self.data.list_countries()
        self.assertEqual(self.data.average_production([countries[0], countries[42]], [1961, 1965], "Wheat and products","Food"),
                         {countries[0] : 1889.8, countries[42] : 67.4})

