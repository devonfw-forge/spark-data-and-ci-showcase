from operator import add
from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import plotly.graph_objects as go

class FAO_production():
    
    def __init__(self,data):

        self.df = data
        self.sparksession = SparkSession.builder.getOrCreate()
        
    def list_countries(self):
        '''
        Returns all countries list.
        :return: list
        '''
        test = []
        return self.df.rdd.map(lambda line: line[0]).distinct().collect()
    
    def countries_productions(self):
        return self.df.rdd.map(lambda line: (line[0], [line[5]])).reduceByKey(lambda accum, n: accum + n).collect()
    
    def production_sum(self):
        
        dicc = {}
        for year in range(1961,2014):
            dicc['Y'+ str(year)] = 'sum'

        prod_years = self.df.agg(dicc).schema.names
        prod_sum = self.df.agg(dicc).rdd.map(lambda line: line[0:54]).collect()[0]
        
        Sum = []
        for i,elt in enumerate(prod_years):
            Sum.append([elt[5:9],prod_sum[i]])

        Sum_ordered = sorted(Sum, key=lambda tup: tup[0])

        return  self.sparksession.createDataFrame(Sum_ordered)
    
    def plot_production_sum(self):
        
        df2 = self.production_sum()
        
        x = [int(row['_1']) for row in  df2.select('_1').collect()]
        y = [int(row['_2']) for row in df2.select('_2').collect()]

        plt.plot(x,y)
        plt.show()
        
    def add_geo_zone(self):
        df_geo = self.sparksession \
            .read \
            .format('csv') \
            .options(header='true', inferSchema='true', delimiter=';') \
            .load('../data2/Book1.csv')

        return self.df.join(df_geo, self.df.Area == df_geo.Country)
    
    def zones_production(self):
        df_extended = self.add_geo_zone()
               
        dicc = {}
        for year in range(1961,2014):
            dicc['Y'+ str(year)] = 'sum'
    
        prod_by_zones = {}
        for year in range(1961,2014):
            prod_by_zones[str(year)] = []
    
        for zone in ['Asia & Pacific', 'Europe', 'Arab States', 'Africa','South/Latin America', 'Unknown', 'North America']:
    
            prod_years = df_extended.filter(df_extended.Zone == zone).agg(dicc).schema.names
            prod_sum = df_extended.filter(df_extended.Zone == zone).agg(dicc).rdd.map(lambda line: line[0:54]).collect()[0]
              
            Sum = []
            for i,elt in enumerate(prod_years):
                Sum.append([elt[5:9],prod_sum[i]])

            Sum_ordered = sorted(Sum, key=lambda tup: tup[0])

            for year in Sum_ordered:
                prod_by_zones[year[0]] = prod_by_zones[year[0]] + [(zone,year[1])]
            
        return prod_by_zones
    
    def plot_zones_production(self):
        dicc_prod_by_zones = self.zones_production()
        AP=[]
        E=[]
        AS=[]
        A=[]
        SA=[]
        U=[]
        NA=[]

        years = [str(x) for x in range(1961,2014)]

        for year in years:
            AP.append(dicc_prod_by_zones[year][0][1])
            E.append(dicc_prod_by_zones[year][1][1])
            AS.append(dicc_prod_by_zones[year][2][1])
            A.append(dicc_prod_by_zones[year][3][1])
            SA.append(dicc_prod_by_zones[year][4][1])
            U.append(dicc_prod_by_zones[year][5][1])
            NA.append(dicc_prod_by_zones[year][6][1])

        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=years,
            x=AP,
            name='Asia & Pacific',
            orientation='h',
            marker=dict(
                color='red',
                line=dict(color='black', width=0.25)
            )
        ))
        fig.add_trace(go.Bar(
            y=years,
            x=E,
            name='Europe',
            orientation='h',
            marker=dict(
                color='blue',
                line=dict(color='black', width=0.25)
            )
        ))
        fig.add_trace(go.Bar(
            y=years,
            x=AS,
            name='Arab States',
            orientation='h',
            marker=dict(
                color='green',
                line=dict(color='black', width=0.25)
            )
        ))
        fig.add_trace(go.Bar(
            y=years,
            x=A,
            name='Africa',
            orientation='h',
            marker=dict(
                color='yellow',
                line=dict(color='black', width=0.25)
            )
        ))
        fig.add_trace(go.Bar(
            y=years,
            x=SA,
            name='South/Latin America',
            orientation='h',
            marker=dict(
                color='orange',
                line=dict(color='black', width=0.25)
            )
        ))
        fig.add_trace(go.Bar(
            y=years,
            x=NA,
            name='North America',
            orientation='h',
            marker=dict(
                color='magenta',
                line=dict(color='black', width=0.25)
            )
        ))

        fig.update_layout(barmode='stack')
        fig.show()
        
    def production_world(self, year):
        year_selected ={'Y' + str(year) :'sum'}
        
        prod = {}
        for country in self.list_countries():
            prod[country] = self.df.filter(self.df.Area == country).agg(year_selected).rdd.map(lambda line: line[0]).collect()[0]
        
        for elt in list(prod.items()):
            if prod[elt[0]]== None:
                prod[elt[0]]=0
                
        return prod
    
    
    def countries_coor(self):
        
        coor = self.df.select(*( self.df.columns[i] for i in [0,61,62] )).distinct().rdd.map(lambda line: (line[0], line[1], line[2])).collect()
        return self.sparksession.createDataFrame(coor)
    
    
    def plot_production_world(self,year):
        coor = self.countries_coor()
            
        lati = [int(row['_2']) for row in   coor.select('_2').collect()]
        long = [int(row['_3']) for row in   coor.select('_3').collect()]
        name = [row['_1'] for row in   coor.select('_1').collect()]

        N = {}
        for i,elt in enumerate(name):
            N[elt] = (lati[i],long[i])

        N1 = list(N.items())
        N2 = sorted(N1, key=lambda tup: tup[0]) 

        produc = list(self.production_world(year).values())

        latitude = []
        longitude = []
        names = []
        for elt in N2:
            latitude.append(elt[1][0])
            longitude.append(elt[1][1])
            names.append(elt[0])
            
        fig = go.Figure(data=go.Scattergeo(
                lon = longitude,
                lat = latitude,
                text = names,
                mode = 'markers',
                marker = dict(
                    size = 8,
                    opacity = 0.8,
                    reversescale = False,
                    autocolorscale = False,
                    symbol = 'square',
                    line = dict(
                        width=1,
                        color='rgba(102, 102, 102)'
                    ),
                    colorscale = 'Blues',
                    cmin = 0,
                    color = produc,
                    cmax =100000,
                    colorbar_title="Food production (1000 tonnes)"
                )))

        fig.update_layout(
                title = 'Countries 2013',
                geo = dict(
                    scope='world',
                    #projection_type='albers usa',
                    showland = True,
                    landcolor = "rgb(250, 250, 250)",
                    subunitcolor = "rgb(217, 217, 217)",
                    countrycolor = "rgb(217, 217, 217)",
                    countrywidth = 0.5,
                    subunitwidth = 0.5
                ),
            )

        fig.show()