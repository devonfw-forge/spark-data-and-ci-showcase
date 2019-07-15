from unittest import TestCase
from API import Api


class TestApi(TestCase):
    def setUp(self):
        self.data = Api()

    def test_first_country(self):
        self.assertEqual(self.data.countries()[0], "Aruba")

    def test_second_country(self):
        self.assertNotEqual(self.data.countries()[1], "Andorra")

    def test_population_aruba_1960(self):
        self.assertEqual(self.data.population('Aruba',['1960','1962'])[0], "54211")

    def test_population_aruba_1962(self):
        self.assertNotEqual(self.data.population('Aruba',['1960','1962'])[2], "59063")

    def test_countries_pop_aruba(self):
        self.assertEqual(self.data.countries_pop(['Aruba','Andorra'],['1960','1962'])[0][1][0], "54211")

    def test_countries_pop_andorra(self):
        self.assertNotEqual(self.data.countries_pop(['Aruba','Andorra'],['1960','1962'])[0][1][1], "57032")
   
    def test_growth_Aruba_and_Afgha_1960_to_1965(self):
        self.assertEqual(self.data.growth(["Aruba","Afghanistan"], ["1960", "1965"]), ["Aruba:3149", "Afghanistan:959347"])

    def test_growth_Aruba_1960_to_1961(self):
        self.assertNotEqual(self.data.growth(["Aruba"], ["1960", "1961"]),["Aruba:3149"])
        
    def test_minpoblacion(self):
        self.assertEqual(self.data.minPoblacion(["Armenia", "Comoros", "Bahrain"],['1960', '1970']), [1874121, 191121, 162427])

    def test_minpoblacion2(self):
        self.assertNotEqual(self.data.minPoblacion(["Brazil", "Barbados", "Gabon"],['1960', '1980']), [1874121, 191121, 162427])

    def test_maxpoblacion(self):
        self.assertEqual(self.data.maxPoblacion(["Armenia", "Comoros", "Zimbabwe"], ['1970', '1980']),[3049109, 297447, 7160023])

    def test_maxpoblacion2(self):
        self.assertNotEqual(self.data.maxPoblacion(["Brazil", "Austria", "Gabon"], ['1960', '1980']),[4587, 191121, 162427])
