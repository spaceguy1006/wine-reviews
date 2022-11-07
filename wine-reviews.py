# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:17:08 2022

@author: shrey
"""
""" This project explores the reviews of several wines """

import pandas as pd

# Creating my own data frame of favourite fruits of different aged people

fav_fruits = pd.DataFrame({'Strawberries':[2, 9, 5, 4],
                         'Grapes': [3, 4, 7, 1], 
                         'Watermelon': [7, 5, 2, 8], 
                         'Banana': [0, 1, 0, 3], 
                         'Mango': [1, 10, 2, 5]}, 
                         index = ['0 - 10', '11 - 20', '21 - 30', '31 - 40'])

fav_fruits.index.name = 'Age Ranges'

print(fav_fruits)

#%%

""" analysing a bigger dataset obtained from the internet """

wine_data = pd.read_csv(r'C:\Users\shrey\OneDrive\Desktop\coding trials\wine_reviews.csv', index_col = 0)

# The index_col = 0 accounts for the index numbering already existing within the dataframe

print(wine_data.head(7))

# Obtaining a list of all columns

list_of_col = list(wine_data.columns)

print(list_of_col)

# This is a list of all the different wine tasters who have given reviews.

print(wine_data['taster_name'].describe())

print(wine_data['taster_name'].unique())

""" There are 19 different wine tasters and Roger Voss has given the most reviews (25514). """

# Getting the taster name, price and points of the first 10 wines

print(wine_data.loc[:9, ['title', 'taster_name', 'price', 'points']])

""" All these wines seem to have the same points. """

# Getting the first 5 wines that come from Mexico 

print(wine_data.loc[wine_data.country == 'Mexico'].head())

# Finding out the list of wines, from France, that Roger Voss has reviewed

RV_france = wine_data.loc[(wine_data.country == 'France') &  (wine_data.taster_name == 'Roger Voss')].count()

print(RV_france)

"""" Roger Voss has reviewed 18602 wines from France! """

# Removing wines which have null price values

null_prices = wine_data.loc[wine_data.price.isnull()]
wine_data2 = wine_data.drop( labels = null_prices.index, axis = 0)

print(wine_data2)

""" wine_data2 is now a dataframe where all the wines have a definite price. """ 


# Finding the cheapest and most expensive wines of each point rating

price_ranges = wine_data.groupby('points').price.agg(['min', 'max'])

print(price_ranges)

# Finding the country which has the greatest price range.

price_ranges = wine_data2.groupby('country').price.agg(['min', 'max'])
range = abs(wine_data.groupby('country').price.min() - wine_data.groupby('country').price.max())
max_range = max(list(range))

print(max_range)

"""France has the greatest price range with a range of 3295. """

# If we're only interested in wines from France, a new dataframe can be created.

french_wine = wine_data2.loc[wine_data2.country == 'France']
french_wine = french_wine.drop('country', axis = 1)
french_wine = french_wine.reset_index(drop = True)

print(french_wine)







































