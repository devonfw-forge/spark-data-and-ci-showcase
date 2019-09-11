from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.types import IntegerType, DoubleType, StringType
import plotly.graph_objs as go
from plotly.offline import iplot
import sqlite3
import pandas as pd 
pd.set_option('display.max_rows', 600)

class Gdp(): 

    def __init__(self, sqlitedata, sparkSession):
        self.spark = sparkSession
        self.conn = sqlitedata
        self.queryGDP = 'SELECT * from gdp'
        self.queryCountries = 'SELECT * from countries'

    def create_panda_gdp(self):
        return pd.read_sql_query(self.queryGDP, self.conn)
        
    def create_spark_gdp(self, pandaDataFrame):
        dataFrame = self.spark.createDataFrame(pandaDataFrame.astype(str))
        dataFrame = dataFrame.withColumn("id", dataFrame["id"].cast(IntegerType())) \
                             .withColumn("gdp", dataFrame["gdp"].cast(DoubleType())) \
                             .withColumn("growth", dataFrame["growth"].cast(DoubleType())) \
                             .withColumn("Year", dataFrame["Year"].cast(IntegerType()))
        return dataFrame

    def create_gdp(self):
        return self.create_spark_gdp(self.create_panda_gdp())
        
        #subset is a list filled with the names of the columns on which we want to aplicate the function (here GDP and Growth)
    def replace_null_values(self, sparkDf, how, subset):
        return sparkDf.dropna(how = how, subset = subset).fillna(0)
    
    def getMaxGDPByCountryCode(self, sparkDataframe, countryCodes):
        df = sparkDataframe.groupby('CountryCode')  \
                           .agg({'gdp': 'max'})     \
                           .orderBy('CountryCode')  \
                           .withColumnRenamed("max(gdp)","maxGDP")
        
        df = sparkDataframe.filter(sparkDataframe.CountryCode.isin(countryCodes)) 

        return df.toPandas()
    
    def get_gdp_by_country_code(self, sparkDataframe, years, countryCodes):
        df = sparkDataframe.filter(sparkDataframe.CountryCode.isin(countryCodes))
        df = df.filter(sparkDataframe.Year.isin([x for x in range(years[0],years[1]+1)]))
        return df.toPandas()
    
    def addGroups(self, data, geo_zone):
        dataFrame = self.spark.createDataFrame(data).withColumn('GroupName', data.CountryCode )
        return dataFrame.replace(geo_zone, 1, 'GroupName')
    
    def groupData(self, data, years):
        dicc = {}
        for year in range(years[0],years[-1]+1):
            dicc[str(year)] = 'sum'
                  
        return data.groupby('GroupName').agg(dicc).orderBy('GroupName')
    
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
        
        
    def plot_gdp_growth(self, pandaDataFrame, years, countryMap, colorSettings):
        data = []
        for i, code in enumerate(list(countryMap.keys())):
            data.append(go.Scatter( x = pandaDataFrame[pandaDataFrame['CountryCode']==list(countryMap.keys())[i]].Year,
                                    y = pandaDataFrame[pandaDataFrame['CountryCode']==list(countryMap.keys())[i]].growth,
                                    mode = "lines",
                                    name = countryMap.get(code),
                                    marker = dict(color = colorSettings.get(code))))        

        layoutTitle = 'Growth indicator from {} to {} for specific countries'
        titlex = 'Years'
        titley = 'Growth indicator in %'
        layout = dict(title = layoutTitle.format(years[0],years[1]),
                      xaxis= dict(title= titlex, ticklen= 5, zeroline= False),
                      yaxis = dict(title= titley, ticklen= 5, zeroline= False))

        fig = go.Figure(data = data, layout = layout)
        iplot(fig)