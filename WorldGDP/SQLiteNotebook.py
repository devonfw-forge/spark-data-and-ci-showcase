from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.types import IntegerType, DoubleType, StringType
import plotly.graph_objs as go
from plotly.offline import iplot
import sqlite3
import pandas as pd 
pd.set_option('display.max_rows', 600)

class Spark_GDP(): 

    def __init__(self, sqlitedata, sparkSession):
        self.spark = sparkSession
        self.conn = sqlitedata
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
        spark_max_by_country_filtered = spark_max_by_country.filter(spark_max_by_country.CountryCode != 'HIC') \
                                        .filter(spark_max_by_country.CountryCode != 'WLD') \
                                        .filter(spark_max_by_country.CountryCode != 'OED') \
                                        .filter(spark_max_by_country.CountryCode != 'PST') \
                                        .filter(spark_max_by_country.CountryCode != 'IBT') 

        panda_max_by_country_filtered = spark_max_by_country_filtered.toPandas()
        return panda_max_by_country_filtered
    
    def PandaDFOfGDPperCountryfromSparkDF(self, filtered_spark_df, year_frame):
        spark_max_by_country_filtered = filtered_spark_df.filter(filtered_spark_df.CountryCode.isin('CHN','HKG','BRA','JPN','KOR','RUS','IND','ZAF','EUU','SGP'))
        spark_max_by_country_filtered = spark_max_by_country_filtered.filter(filtered_spark_df.Year.isin([x for x in range(year_frame[0],year_frame[1]+1)]))
        panda_max_by_country_filtered = spark_max_by_country_filtered.toPandas()
        return panda_max_by_country_filtered
    
    def add_groups(self,Data, geo_zone):
        Data = self.spark.createDataFrame(Data)
        Data_extended = Data.withColumn('GroupName', Data.CountryCode )
        return Data_extended.replace(geo_zone,1,'GroupName')
    
    def groups_data(self, Data, years_frame):
        dicc = {}
        for year in range(years_frame[0],years_frame[-1]+1):
            dicc[str(year)] = 'sum'
                  
        return Data.groupby('GroupName').agg(dicc).orderBy('GroupName')
    
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
        
        
    def plotLinesGrowthwithPandaDF(self, CountryGDP_panda_DF, year_frame):
        trace1 = go.Scatter(
                            x = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='BRA'].Year,
                            y = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='BRA'].growth,
                            mode = "lines",
                            name = "Brazil",
                            marker = dict(color = 'rgba(255, 0, 0, 0.8)'))

        trace2 = go.Scatter(
                            x = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='CHN'].Year,
                            y = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='CHN'].growth,
                            mode = "lines",
                            name = "China",
                            marker = dict(color = 'rgba(255, 128, 0, 0.8)'))

        trace3 = go.Scatter(
                            x = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='EUU'].Year,
                            y = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='EUU'].growth,
                            mode = "lines",
                            name = "Europe",
                            marker = dict(color = 'rgba(255, 255, 0, 0.8)'))

        trace4 = go.Scatter(
                            x = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='HKG'].Year,
                            y = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='HKG'].growth,
                            mode = "lines",
                            name = "Hong-Kong",
                            marker = dict(color = 'rgba(128, 255, 0, 0.8)'))

        trace5 = go.Scatter(
                            x = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='IND'].Year,
                            y = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='IND'].growth,
                            mode = "lines",
                            name = "India",
                            marker = dict(color = 'rgba(0, 255, 255, 0.8)'))

        trace6 = go.Scatter(
                            x = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='JPN'].Year,
                            y = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='JPN'].growth,
                            mode = "lines",
                            name = "Japon",
                            marker = dict(color = 'rgba(0, 128, 255, 0.6)'))

        trace7 = go.Scatter(
                            x = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='KOR'].Year,
                            y = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='KOR'].growth,
                            mode = "lines",
                            name = "South Korea",
                            marker = dict(color = 'rgb(127, 0, 255)'))

        trace8 = go.Scatter(
                            x = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='RUS'].Year,
                            y = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='RUS'].growth,
                            mode = "lines",
                            name = "Russia",
                            marker = dict(color = 'rgb(255, 0, 255)'))

        trace9 = go.Scatter(
                            x = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='ZAF'].Year,
                            y = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='ZAF'].growth,
                            mode = "lines",
                            name = "South Africa",
                            marker = dict(color = 'rgb(255, 0, 127)'))

        trace10 = go.Scatter(
                            x = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='SGP'].Year,
                            y = CountryGDP_panda_DF[CountryGDP_panda_DF['CountryCode']=='SGP'].growth,
                            mode = "lines",
                            name = "Singapour",
                            marker = dict(color = 'black'))
        
        data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10]
        layout = dict(title = 'Growth indicator from {} to {} for specific countries'.format(year_frame[0],year_frame[1]),
                        xaxis= dict(title= 'Years',ticklen= 5,zeroline= False),
                        yaxis = dict(title= 'Growth indicator in %',ticklen= 5,zeroline= False))
        fig = dict(data = data, layout = layout)
        iplot(fig)