import geopandas as gpd
import requests
from matplotlib import pyplot as plt
# download data from covid api
url = 'https://api.covid19api.com/summary'
covid_data = requests.get(url)

# Read in shapefile and examine data
africa = gpd.read_file('shapefiles/Africa.shp')
africa.plot()
plt.axis("off")
plt.show()

