from unittest import TestCase
from fao import Fao


class TestFao(TestCase):
    def setUp(self):
        self.data = Fao()

    def test_countries(self):
        countries = self.data.countries()
        self.assertEqual(countries[0], "Afghanistan")
        self.assertEqual(countries[42], "Cyprus")
        self.assertEqual(countries[-1], "Zimbabwe")
        self.assertEqual(countries[137], "Senegal")
        self.assertEqual(len(countries), 174)


    def test_products(self):
        countries = self.data.countries()
        self.assertEqual(self.data.products(countries[0])[0], "Wheat and products")
        self.assertEqual(self.data.products(countries[-1])[0], "Wheat and products")

    def test_min(self):
        countries = self.data.countries()
        self.assertEqual(self.data.min([countries[0]], [2010, 2013])[countries[0]][0][-1], 0)

    def test_max(self):
        countries = self.data.countries()
        self.assertEqual(self.data.max([countries[0]], [2010, 2013])[countries[0]][-1], 5495)

    def test_av(self):
        countries = self.data.countries()
        self.assertEqual(self.data.av([countries[0], countries[42]], [1961, 1965], "Wheat and products","Food"),
                         {countries[0] : 1889.8, countries[42] : 67.4})

