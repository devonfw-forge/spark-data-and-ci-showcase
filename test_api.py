from unittest import TestCase
from API import Api


class TestApi(TestCase):
    def setUp(self):
        self.data = Api()

    def test_countries(self):
        self.assertEqual(self.data.countries()[0], "Aruba")

    def test_countries2(self):
        self.assertNotEqual(self.data.countries()[1], "Andorra")

    def test_population(self):
        self.assertEqual(self.data.population("Aruba")[0], "54211")

    def test_population2(self):
        self.assertNotEqual(self.data.population("Aruba")[2], "59063")

    def test_countries_pop(self):
        self.assertEqual(self.data.countries_pop(["Aruba"])[0][1][0], "54211")

    def test_countries_pop2(self):
        self.assertNotEqual(self.data.countries_pop(["Aruba"])[0][1][1], "57032")
   
   def test_growth(self):
        self.assertEqual(self.data.growth(["Aruba"], ["1960", "1961"]), 1227)

    def test_growth2(self):
        self.assertNotEqual(self.data.growth(["Aruba"], ["1960", "1961"]), 1287)
