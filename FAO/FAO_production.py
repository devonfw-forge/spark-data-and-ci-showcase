from operator import add
from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import plotly.graph_objects as go

class FAO_production():
    
    def __init__(self, data, spark):
        self.df = data
        self.sparksession = spark
        
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
    
    def plot_production_sum(self, dataFrame):
        x = [int(row['_1']) for row in  dataFrame.select('_1').collect()]
        y = [int(row['_2']) for row in dataFrame.select('_2').collect()]

        plt.plot(x,y)
        plt.show()
        
    def get_geo_zone(self, dataSource):
        df_geo = self.sparksession \
                     .read \
                     .format('csv') \
                     .options(header='true', inferSchema='true', delimiter=';') \
                     .load(dataSource)

        return self.df.join(df_geo, self.df.Area == df_geo.Country)
    
    def get_prod_by_zones(self, geo_zones_df, year_ini, year_end, zones):
        dicc = {}
        prod_by_zones = {}

        for year in range(year_ini, year_end):
            dicc['Y'+ str(year)] = 'sum'
            prod_by_zones[str(year)] = []

        for zone in zones:
            prod_years = geo_zones_df.filter(geo_zones_df.Zone == zone).agg(dicc).schema.names
            prod_sum = geo_zones_df.filter(geo_zones_df.Zone == zone).agg(dicc).rdd.map(lambda line: line[0:54]).collect()[0]

            Sum = []
            for i, elt in enumerate(prod_years):
                Sum.append([elt[5:9], prod_sum[i]])

            Sum_ordered = sorted(Sum, key=lambda tup: tup[0])

            for year in Sum_ordered:
                prod_by_zones[year[0]] = prod_by_zones[year[0]] + [(zone, year[1])]
            
        return prod_by_zones

    
    
    def plot_production_zones(self, prod_zones_map, year_ini, year_end, color_zones):
        AP=[]
        E=[]
        AS=[]
        A=[]
        SA=[]
        U=[]
        NA=[]

        years = [str(x) for x in range(year_ini, year_end)]

        for year in years:
            AP.append(prod_zones_map[year][0][1])
            E.append(prod_zones_map[year][1][1])
            AS.append(prod_zones_map[year][2][1])
            A.append(prod_zones_map[year][3][1])
            SA.append(prod_zones_map[year][4][1])
            U.append(prod_zones_map[year][5][1])
            NA.append(prod_zones_map[year][6][1])

        fig = go.Figure()

        for i, zone in enumerate(list(color_zones.keys())):
            fig.add_trace(go.Bar(
                y=years,
                x=AP,
                name=zone,
                orientation='h',
                marker=dict(
                    color=color_zones[zone],
                    line=dict(color='black', width=0.25)
                )
           ))

        fig.update_layout(barmode='stack')
        fig.show()

    def group_prod_world(self, year, country_list):
        year_selected ={'Y' + str(year) :'sum'}
        return self.df.filter(self.df.Area.isin(country_list)).groupBy('Area').agg(year_selected)
        
    def production_world_refact(self, prod_world_grouped, year, country_list):
        panda_df = prod_world_grouped.toPandas()

        col = 'sum(Y' + str(year) + ')'
        # year_selected ={'Y' + str(year) :'sum'}

        prod = {}
        for country in country_list:
            prod[country] = panda_df.loc[panda_df['Area'] == country, [col][0]]
            
            
            
        #     prod[country].agg(year_selected).rdd.map(lambda line: line[0]).collect()[0]
            
        #     self.df.filter(self.df.Area == country).agg(year_selected).rdd.map(lambda line: line[0]).collect()[0]
        # for elt in list(prod.items()):
        #     if prod[elt[0]]== None:
        #         prod[elt[0]]=0
        return prod

    def production_world(self, year, country_list):
        year_selected ={'Y' + str(year) :'sum'}
        
        prod = {}
        for country in country_list:
            prod[country] = self.df.filter(self.df.Area == country).agg(year_selected).rdd.map(lambda line: line[0]).collect()[0]
        
        for elt in list(prod.items()):
            if prod[elt[0]]== None:
                prod[elt[0]]=0
                
        return prod
    
    
    def countries_coor(self):
        coor = self.df.select(*( self.df.columns[i] for i in [0,61,62] )).distinct().rdd.map(lambda line: (line[0], line[1], line[2])).collect()
        return self.sparksession.createDataFrame(coor)
    
    
    def plot_production_world(self, dataframe):
        coor = self.countries_coor()
            
        lati = [int(row['_2']) for row in   coor.select('_2').collect()]
        long = [int(row['_3']) for row in   coor.select('_3').collect()]
        name = [row['_1'] for row in   coor.select('_1').collect()]

        N = {}
        for i,elt in enumerate(name):
            N[elt] = (lati[i],long[i])

        N1 = list(N.items())
        N2 = sorted(N1, key=lambda tup: tup[0]) 

        produc = list(dataframe.values())

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