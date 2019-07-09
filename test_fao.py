from unittest import TestCase
from FAO import Fao


class TestFao(TestCase):
    def setUP(self):
        self.data = Fao()

    def show_countries(self):
        self.assertEqual(self.data.countries()[0], "Afghanistan")

    def show_products(self):
        self.asserEqual(self.data.products("Afghanistan")[0], "Wheat and products")

    def show_min(self):
        self.assertEqual(self.data.min(["Afghanistan"], ['Y1961', 'Y2013']), )

    def show_max(self):
        self.assertEqual(self.data.max(["Afghanistan"], ['Y1961', 'Y2013']), ["Wheat and products", "Y2013"])

    def show_av(self):
        self.assertEqual(self.data.av(["Afghanistan"], ['Y1961', 'Y1965'], "Wheat and products"), 1889.8)
