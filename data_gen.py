import pandas as pd
'''
Main goal is to generate a filter list that can filter out african countries
'''
countries = pd.read_csv('countries.csv')
continent = pd.read_csv('continent.csv')
africa = continent[continent['Continent']=='Africa']
african_countries = africa['Country']