from unittest import TestCase

from sqlalchemyy import Analyse


class TestAnalyse(TestCase):

    def setUp(self):
        self.data = Analyse()

    def test_countries(self):
        datas = self.data.countries()

        self.assertEqual( len(datas), 264)
        self.assertEqual(datas[0], 'Aruba')
        self.assertEqual(datas[-1], 'Zimbabwe')
        self.assertEqual(datas[131], 'St. Lucia')
        self.assertNotEqual(datas[50], 'Angola')

    def test_countries_code(self):

        codes = self.data.countries_code()
        self.assertEqual(len(codes), 264)
        self.assertEqual(codes[0], 'ABW')
        self.assertEqual(codes[-1], 'ZWE')
        self.assertEqual(codes[131], 'LCA')
        self.assertNotEqual(codes[127], 'ABC')

    def test_code_to_name(self):
        codes = self.data.countries_code()
        datas = self.data.countries()

        self.assertEqual(self.data.code_to_name(codes[0]), datas[0])
        self.assertEqual(self.data.code_to_name(codes[-1]), datas[-1])
        self.assertEqual(self.data.code_to_name(codes[131]), datas[131])
        self.assertNotEqual(self.data.code_to_name(codes[10]), datas[20])

    def test_name_to_code(self):
        codes = self.data.countries_code()
        datas = self.data.countries()

        self.assertEqual(self.data.name_to_code(datas[0]), codes[0])
        self.assertEqual(self.data.name_to_code(datas[-1]), codes[-1])
        self.assertEqual(self.data.name_to_code(datas[131]), codes[131])
        self.assertNotEqual(self.data.name_to_code(datas[10]), codes[20])

    def test_countries_data(self):
        datas = self.data.countries()
        self.assertEqual(self.data.countries_data([datas[0]], [1960, 1970])[datas[0]][0][1], 0)
        self.assertEqual(self.data.countries_data([datas[1]], [1960, 1970])[datas[1]][1][1], 548888895.555556)
        self.assertEqual(self.data.countries_data([datas[32], datas[50]], [1960, 1970])[datas[32]][0][1], 112155598.949571)
        self.assertNotEqual(self.data.countries_data([datas[-1]], [1960, 2018])[datas[-1]][-1][1], 0)

    def test_growth(self):
        datas = self.data.countries()
        self.assertEqual(self.data.max_growth([datas[1], datas[2]], [1990, 2000]), (15.0000000288634, {'Afghanistan': 0, 'Angola': 15.0000000288634}))
        self.assertEqual(self.data.max_growth([datas[-1], datas[-2]], [1990, 2000]), (10.3606967698065, {'Zambia': 6.79727404907118, 'Zimbabwe': 10.3606967698065}))

        self.assertEqual(self.data.min_growth([datas[1], datas[2]], [1990, 2000]), (-23.9834174420578, {'Afghanistan': 0, 'Angola': -23.9834174420578}))
        self.assertEqual(self.data.min_growth([datas[-1], datas[-2]], [1990, 2000]), (-9.01557008626092, {'Zambia': -8.6254419523128, 'Zimbabwe': -9.01557008626092}))

        self.assertNotEqual(self.data.av_growth([datas[8], datas[44], datas[20]], [1990, 1995]),
                            {datas[198]: 48861984.861827, datas[188]: 2521170662.67905, datas[205]: 215728296.915783})

        self.assertEqual(self.data.av_growth([datas[149], datas[188], datas[204]], [2001, 2006]),
                         {datas[149]: 3.0019064949716667, datas[188]: 3.6101258971329564, datas[204]: 7.016596579021644})

    def test_gdp(self):
        datas = self.data.countries()
        self.assertEqual(self.data.min_gdp([datas[142], datas[139], datas[130]], [1960, 2018]), (34579308.4138317,
 {'Lesotho': 34579308.4138317,
  'Libya': 20481889763.7795,
  'Luxembourg': 703925705.942958}))
        self.assertEqual(self.data.max_gdp([datas[142], datas[139], datas[130]], [1960, 2018]), (69487922619.3401,
 {'Lesotho': 2791762880.25884, 'Libya': 0, 'Luxembourg': 69487922619.3401}))

        self.assertNotEqual(self.data.min_gdp([datas[27], datas[168]], [1984, 2018]), (69487922619.3401,
 {'Lesotho': 2791762880.25884, 'Libya': 0, 'Luxembourg': 69487922619.3401}))
        self.assertNotEqual(self.data.max_gdp([datas[27], datas[168]], [1984, 2018]), (69487922619.3401,
 {'Lesotho': 2791762880.25884, 'Libya': 0, 'Luxembourg': 69487922619.3401}))

        self.assertEqual(self.data.av_gdp([datas[8], datas[44], datas[20]], [1990, 1995]),
                         {datas[8]: 1597122009.636872, datas[44]: 413608659.37108946, datas[20]: 5035726950.35461})

        self.assertNotEqual(self.data.av_gdp([datas[149], datas[188], datas[204]], [2001, 2006]),
                            {datas[149]: 48861984.861827, datas[188]: 2521170662.67905, datas[204]: 215728296.915783})


