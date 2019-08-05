#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.types import IntegerType, DoubleType, StringType
import plotly.graph_objs as go
from plotly.offline import iplot
import sqlite3
import pandas as pd 


# In[2]:

datapath = "WorldGDP/world-gdp.db"

class Spark_SQLite():

    def __init__(self, datapath):
        self.spark = SparkSession.builder.appName("SQLite demo").getOrCreate()
        self.conn = sqlite3.connect(datapath)
        self.queryGDP = 'SELECT * from gdp'
        self.queryCountries = 'SELECT * from countries'


    def createGDPPandaDF(self):
        panda_df = pd.read_sql_query(self.queryGDP, self.conn)
        return panda_df
        
    def createSparkDFfromPandaDF(self, panda_df):
        spark_df = self.spark.createDataFrame(panda_df.astype(str))
        spark_df = spark_df.withColumn("id", spark_df["id"].cast(IntegerType()))
        spark_df = spark_df.withColumn("gdp", spark_df["gdp"].cast(DoubleType()))
        spark_df = spark_df.withColumn("growth", spark_df["growth"].cast(DoubleType()))
        spark_df = spark_df.withColumn("Year", spark_df["Year"].cast(IntegerType()))
        return spark_df
        
        #subset is a list filled with the names of the columns on which we want to aplicate the function (here GDP and Growth)
    def replaceNullValuesTo0fromSparkDF(self, spark_df, how, subset):
        filtered_spark_df = spark_df.dropna(how = how, subset = subset)
        filtered_spark_df = filtered_spark_df.fillna(0)
        return filtered_spark_df
    
    def PandaDFOfMaxGDPperCountryfromSparkDF(self, filtered_spark_df):
        spark_max_by_country = filtered_spark_df.groupby('CountryCode').agg({'gdp': 'max'}).orderBy('CountryCode')
        spark_max_by_country = spark_max_by_country.withColumnRenamed("max(gdp)","maxGDP")
        spark_max_by_country_filtered = spark_max_by_country.filter(spark_max_by_country.CountryCode != 'HIC')                                         .filter(spark_max_by_country.CountryCode != 'WLD')                                         .filter(spark_max_by_country.CountryCode != 'OED')                                         .filter(spark_max_by_country.CountryCode != 'PST')                                         .filter(spark_max_by_country.CountryCode != 'IBT') 

        panda_max_by_country_filtered = spark_max_by_country_filtered.toPandas()
        return panda_max_by_country_filtered
    
    def createBarGraphwithPandaDF(self, xData, yData, title, nameXAxis, nameYAxis):
        trace1 = go.Bar(
                        x = xData,
                        y = yData,
                        marker = dict(color = 'rgba(255, 0, 0, 3)', line=dict(color='rgb(0,0,0)',width=1)))
        data = [trace1]
        fig = go.Figure(data = data)
        fig.update_layout(
            title=go.layout.Title(
                text=title,
                xref="paper",
                x=0
            ),
            xaxis=go.layout.XAxis(
                title=go.layout.xaxis.Title(
                    text=nameXAxis,
                    font=dict(
                        family="Courier New, monospace",
                        size=17,
                        color="#7f7f7f"
                    )
                )
            ),
            yaxis=go.layout.YAxis(
                title=go.layout.yaxis.Title(
                    text=nameYAxis,
                    font=dict(
                        family="Courier New, monospace",
                        size=17,
                        color="#7f7f7f"
                    )
                )
            )
        )
        iplot(fig)




