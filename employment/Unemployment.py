from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import DoubleType,IntegerType
import plotly.graph_objects as go
import pandas as pd
from typing import Dict 
from pyspark.sql.types import DataType

class Employment():

    def __init__(self, data, sparkSession):
        self.spark = sparkSession         
        self.df_unemployment = data
        
    def extract_info(self, years: list, countries: list ) -> DataType:
        years = [str(year) for year in range(years[0], years[-1]+1)]
        
        return  self.df_unemployment\
                    .fillna(0)\
                    .select([c for c in self.df_unemployment.columns if c in ['CountryName'] + years]) \
                    .filter(self.df_unemployment.CountryName.isin(countries))\
                    
    def add_groups(self, data: DataType, geo_zone: dict) -> DataType:
        dataExtended = data.withColumn('GroupName', data.CountryName )
        return dataExtended.replace(geo_zone, 1, 'GroupName')
    
    def group_data(self, data: DataType, years:list) -> DataType:
        dicc = {}
        for year in range(years[0], years[-1]+1):
            dicc[str(year)] = 'sum'
        for column in data.columns[1:-1]:
            data = data.withColumn(column, F.regexp_replace(column,',','.'))
        
        return data.groupby('GroupName').agg(dicc).orderBy('GroupName')   
        
    
    def plot_unemployment(self, data: DataType, years: list, colorSettings) -> None:
            pandaDataframe= data.toPandas()
            years = [str(year) for year in range(years[0], years[-1]+1)]
            fig = go.Figure()

            for i, zone in enumerate(list(colorSettings.keys())):
                unemployment = pandaDataframe.iloc[i][1:-1]
                fig.add_trace(go.Scatter(x=years, 
                                         y=unemployment.iloc[::-1], 
                                         name=zone,
                                         line_color=colorSettings[zone]))

            fig.update_layout(title_text='Unemployment percentage from {} to {}'.format(years[0], years[1]), xaxis_rangeslider_visible=True)
            fig.show()          
            