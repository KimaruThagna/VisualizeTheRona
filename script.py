import geopandas as gpd
import requests

# download data from covid api
# Read in shapefile and examine data
africa = gpd.read_file('shapefiles/Africa.shp')
print(africa.head())