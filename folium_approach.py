import folium, requests

# download data from covid api
url = 'https://api.covid19api.com/summary'
covid_data = requests.get(url)
covid_data = covid_data.json()
print(covid_data['Countries'])

# initialize map
africa = folium.Map([-0.7832, 28.5085], zoom_start=3.42)
folium.TileLayer(tiles='Stamen Toner',name="Stamen Toner").add_to(africa)
folium.TileLayer(tiles='Stamen Terrain',name="Stamen Terrain").add_to(africa)
folium.TileLayer(tiles='CartoDB dark_matter',name="CartoDB Dark_Matter").add_to(africa)
folium.LayerControl().add_to(africa)

icon = folium.DivIcon(html="<font color='red'>20</font>")
folium.Marker([-0.7832, 28.5085], icon=icon).add_to(africa)
# save to html
africa.save('covid.html')