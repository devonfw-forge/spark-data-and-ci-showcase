#!/usr/bin/env python
# coding: utf-8

# In[6]:


import unittest
import sqlite3
import sys
from pyspark import SparkContext


sys.path.append("WorldGDP")
from SQLiteNotebook import Spark_GDP


# In[13]:
datapath = "test/WorldGDP/world-gdp.db"
sqlitedata = sqlite3.connect(datapath)
spark = SparkSession.builder.appName("Crisis_analyse").getOrCreate()

class TestSQLiteNotebook(unittest.TestCase):
    
    def setUp(self):
        self.S = Spark_GDP(sqlitedata, spark)
        
    def test_list_countries(self):
        pandaDF = self.S.createGDPPandaDF()
        sparkDF = self.S.createSparkDFfromPandaDF(pandaDF)
        sparkDF_filtered = self.S.replaceNullValuesTo0fromSparkDF(sparkDF, "all", ["gdp", "growth"])
        pandaDF_filtered = sparkDF_filtered.toPandas()
        self.assertEqual(pandaDF_filtered['growth'][0],0.0)


unittest.main(argv=[''], verbosity=2, exit=False)





