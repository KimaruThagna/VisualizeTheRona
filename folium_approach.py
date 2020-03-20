import folium, requests, os, time
from pandas.io.json import json_normalize
import pandas as pd
import geopandas as gpd
from selenium import webdriver
# download data from covid api
url = 'https://api.covid19api.com/summary'
covid_data = requests.get(url)
covid_data = covid_data.json()
africa_shp = gpd.read_file('shapefiles/Africa.shp')
africa_shp.crs = {'init' :'epsg:3857'}


df = json_normalize(covid_data['Countries'])
countries_with_coordinates = pd.read_csv('african_countries_with_coords.csv')
covid_data_rich = pd.merge(df, countries_with_coordinates, on='Country')

choropleth_data = df[df['Country'].isin(africa_shp['COUNTRY'])]
choropleth_data.reset_index()
print(choropleth_data.head())
# add a latitude and logitude property to the countries json objects for plotting
# initialize map
africa = folium.Map([-0.7832, 28.5085], zoom_start=3.48, tiles=None)
folium.TileLayer(tiles='CartoDB positron',name="CartoDB Positron").add_to(africa)
folium.TileLayer(tiles='CartoDB dark_matter',name="CartoDB Dark_Matter").add_to(africa)
folium.LayerControl().add_to(africa)

for idx, country in covid_data_rich.iterrows():
    # generate and display marker
    icon = folium.DivIcon(html=f'<font color="red">{country["TotalConfirmed"]}</font>')
    folium.Marker([country['latitude'], country['longitude']], icon=icon).add_to(africa)

# Add the color for the chloropleth:
folium.GeoJson(africa_shp).add_to(africa)



# save to html
title_html = '''
             <h3 align="center" style="font-size:20px"><b>Covid-19 TotalConfirmed Cases Africa</b></h3>
             '''
africa.get_root().html.add_child(folium.Element(title_html))
africa.save('covid.html')

# driver = webdriver.Chrome(executable_path='/home/macbuntu/PycharmProjects/VisualizeTheRona/chromedriver')
# driver.set_window_size(4000, 3000)  # choose a resolution
# driver.get('file:///home/macbuntu/PycharmProjects/VisualizeTheRona/covid.html')
# # You may need to add time.sleep(seconds) here
#
# driver.save_screenshot('screenshot.png')