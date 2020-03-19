import geopandas as gpd
import requests

# download data from covid api
url = 'https://api.covid19api.com/summary'
covid_data = requests.get(url)
print(covid_data.json())
# Read in shapefile and examine data
africa = gpd.read_file('shapefiles/Africa.shp')
print(africa.head())