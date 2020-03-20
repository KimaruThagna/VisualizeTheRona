import geopandas as gpd
import pandas as pd
import requests
import matplotlib.pyplot as plt
from pandas.io.json import json_normalize
# download data from covid api
url = 'https://api.covid19api.com/summary'

# Read in shapefile and examine data
africa = gpd.read_file('shapefiles/Africa.shp')
africa.drop_duplicates(subset='CODE',inplace=True)# remove duplicates
# request data from resource
covid_data = requests.get(url)
df = json_normalize(covid_data.json()['Countries'])
# filter out african countries
afrca_updates = df[df['Country'].isin(africa['COUNTRY'])]
merged_dataset = pd.merge(africa, afrca_updates, left_on='COUNTRY', right_on='Country')


# plotting data on merged dataset
fig, ax = plt.subplots(1, figsize=(10, 6))
africa.plot(ax=ax, alpha=0.2)
colors = 'YlOrRd'
merged_dataset.plot(column='TotalConfirmed', cmap=colors,ax=ax)


# Add Labels
merged_dataset['coords'] = merged_dataset['geometry'].apply(lambda x: x.representative_point().coords[:])# generate coord points for labels
merged_dataset['coords'] = [coords[0] for coords in merged_dataset['coords']]
# annotate each african country
for idx, row in merged_dataset.iterrows():
    plt.annotate(s=f'{row["TotalDeaths"]}', xy=row['coords'],horizontalalignment='right')

# Create colorbar as a legend
sm = plt.cm.ScalarMappable(cmap=colors, norm=plt.Normalize(vmin=0, vmax=10))
# add the colorbar to the figure
cbar = fig.colorbar(sm)
# if you wish for the colorbar to be horizontal
#fig.colorbar(sm, orientation="horizontal", fraction=0.036, pad=0.1, aspect = 30)
# create an annotation for the data source
ax.annotate('Source: www.covid19api.com',xy=(0.1, .08),
            xycoords='figure fraction', horizontalalignment='left',
            verticalalignment='top', fontsize=12, color='#555555')

ax.annotate('Note:Blue regions lack data from api ',xy=(0.1, .03),
            xycoords='figure fraction', horizontalalignment='left',
            verticalalignment='top', fontsize=10, color='#F70D1A')
plt.title("Covid19 Data. TotalDeaths(number) vs TotalConfirmed Cases(shade)")
plt.axis("off")
plt.show()
fig.savefig('covid.png')