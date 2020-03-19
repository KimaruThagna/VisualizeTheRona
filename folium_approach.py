import folium, requests
from pandas.io.json import json_normalize
import pandas as pd
# download data from covid api
url = 'https://api.covid19api.com/summary'
covid_data = requests.get(url)
covid_data = covid_data.json()

df = json_normalize(covid_data['Countries'])
countries_with_coordinates = pd.read_csv('african_countries_with_coords.csv')
covid_data_rich = pd.merge(df, countries_with_coordinates, on='Country')

# add a latitude and logitude property to the countries json objects for plotting

# initialize map
africa = folium.Map([-0.7832, 28.5085], zoom_start=3.42)
folium.TileLayer(tiles='Stamen Toner',name="Stamen Toner").add_to(africa)
folium.TileLayer(tiles='Stamen Terrain',name="Stamen Terrain").add_to(africa)
folium.TileLayer(tiles='CartoDB dark_matter',name="CartoDB Dark_Matter").add_to(africa)
folium.LayerControl().add_to(africa)

for country in covid_data_rich.iterrows():
    # generate and display marker
    icon = folium.DivIcon(html=f'<font color="red">{country.NewDeaths}</font>')
    folium.Marker([country.latitude, country.longitude], icon=icon).add_to(africa)
# save to html
africa.save('covid.html')