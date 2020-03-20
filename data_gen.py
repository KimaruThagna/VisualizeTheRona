import pandas as pd
'''
Main goal is to generate a filter list that can filter out african countries
'''
countries = pd.read_csv('countries.csv')
continent = pd.read_csv('continent.csv')
africa = continent[continent['Continent']=='Africa']
african_countries = africa['Country']
countries_with_coordinates = countries[countries['Country'].isin(african_countries)]
countries_with_coordinates = countries_with_coordinates[['Country', 'latitude', 'longitude']]
print(len(countries))
print(len(african_countries))
print(len(countries_with_coordinates))
countries_with_coordinates.to_csv('african_countries_with_coords.csv')