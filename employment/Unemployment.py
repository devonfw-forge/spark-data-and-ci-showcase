from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import DoubleType,IntegerType
import plotly.graph_objects as go
import pandas as pd

class Employment():

    def __init__(self):
        self.spark = SparkSession \
            .builder \
            .appName("Employment App") \
            .getOrCreate()
        
        self.df_unemployment = self.spark \
            .read \
            .format('csv') \
            .options(header='true', inferSchema='true', delimiter=';') \
            .load('../data2/Book2.csv')
        
    def extract_info(self, years_frame, countries_list ):
        years = [str(year) for year in range(years_frame[0],years_frame[-1]+1)]
        
        return  self.df_unemployment\
                .fillna(0)\
                .select([c for c in self.df_unemployment.columns if c in ['CountryName'] + years]) \
                .filter(self.df_unemployment.CountryName.isin(countries_list))\
                    
    def add_groups(self,Data, geo_zone):
        Data_extended = Data.withColumn('GroupName', Data.CountryName )
        return Data_extended.replace(geo_zone,1,'GroupName')
    
    def groups_data(self, Data, years_frame):
        dicc = {}
        for year in range(years_frame[0],years_frame[-1]+1):
            dicc[str(year)] = 'sum'
        for column in Data.columns[1:-1]:
            
            Data = Data.withColumn(column, F.regexp_replace(column,',','.'))
          
        return Data.groupby('GroupName').agg(dicc).orderBy('GroupName')   
        
    
    def plot_unemployment(self,Data, years_frame):
            
            dataframePanda = Data.toPandas()

            years = [str(year) for year in range(years_frame[0],years_frame[-1]+1)]
            fig = go.Figure()
            zone_list_plot = {'Asian Tigers':'red', 'BRICS':'blue', 'China':'yellow', 'Europe':'green', 'Japan':'magenta', 'US':'black'}
            for i,zone in enumerate(list(zone_list_plot.keys())):
                
                unemployment = dataframePanda.iloc[i][1:-1]
                fig.add_trace(go.Scatter(x=years, y=unemployment.iloc[::-1], name=zone,
                                         line_color=zone_list_plot[zone]))

            fig.update_layout(title_text='Unemployment percentage from {} to {}'.format(years_frame[0], years_frame[1]),
                                  xaxis_rangeslider_visible=True)
            fig.show()          
            