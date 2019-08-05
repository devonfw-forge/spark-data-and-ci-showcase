import unittest
from pyspark import SparkContext
from pyspark import SQLContext
import sys
#append the relative location you want to import from
sys.path.append("FAO")
from FAO_spark import Spark

class Test_FAO_spark(unittest.TestCase):
    
    def setUp(self):
        self.S = Spark("test/FAO/FAO+database.json")
        
    def test_list_countries(self):
        self.assertEqual(len(self.S.list_countries()), 174)


unittest.main(argv=[''], verbosity=2, exit=False)