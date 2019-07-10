from unittest import TestCase
from FAO import Fao


class TestFao(TestCase):
    def setUp(self):
        self.data = Fao()

    def test_countries(self):
        self.assertEqual(self.data.countries()[0], "Afghanistan")

    def test_products(self):
        self.assertEqual(self.data.products("Afghanistan")[0], "Wheat and products")

    def test_min(self):
        self.assertEqual(self.data.min(["Afghanistan"], [2010, 2013])["Afghanistan"][0][-1], 0)

    def test_max(self):
        self.assertEqual(self.data.max(["Afghanistan"], [2010, 2013])["Afghanistan"][-1], 5495)

    def test_av(self):
        self.assertEqual(self.data.av(["Afghanistan","Cyprus"], ['Y1961', 'Y1965'], "Wheat and products"), ["Afghanistan:1889.8","Cyprus:67.5"])


        

