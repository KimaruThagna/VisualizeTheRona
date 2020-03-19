import pandas as pd
'''
Main goal is to generate a filter list that can filter out african countries
'''
countries = pd.read_csv('countries.csv')
continent = pd.read_csv('continent.csv')
africa = continent[continent['Continent']=='Africa']
african_countries = africa['Country']
countries_with_coordinates = countries[countries['country'].isin(african_countries)]
countries_with_coordinates = countries_with_coordinates[['Country', 'latitude', 'longitude']]
print(countries_with_coordinates)
