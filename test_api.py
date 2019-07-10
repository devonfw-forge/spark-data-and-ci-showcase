from unittest import TestCase


class TestApi(TestCase):

   def test_growth(self):
        self.assertEqual(self.data.growth(["Aruba"], ["1960", "1961"]), 1227)

    def test_growth2(self):
        self.assertNotEqual(self.data.growth(["Aruba"], ["1960", "1961"]), 1287)
