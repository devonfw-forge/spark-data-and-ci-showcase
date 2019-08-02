import unittest
from pyspark import SparkContext
from FAO_spark import Spark

sc = SparkContext("local", "First App")

class Test_FAO_spark(unittest.TestCase):
    
    def setUp(self):
        self.S = Spark(sc) 
        
    def test_list_countries(self):
        self.assertEqual(len(self.S.list_countries()), 174)


unittest.main(argv=[''], verbosity=2, exit=False)