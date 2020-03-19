import folium

africa = folium.Map([-8.7832, 34.5085], zoom_start=8)
folium.TileLayer(tiles='Stamen Toner',name="Stamen Toner").add_to(africa)
folium.TileLayer(tiles='Stamen Terrain',name="Stamen Terrain").add_to(africa)
folium.TileLayer(tiles='CartoDB dark_matter',name="CartoDB Dark_Matter").add_to(africa)
folium.LayerControl().add_to(africa)
africa.save('covid.html')