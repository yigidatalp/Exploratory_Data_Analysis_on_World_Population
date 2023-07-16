# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:55:00 2023

@author: Yigitalp
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read the dataset
df = pd.read_csv('world_population.csv')

# check the dataset
df.info()

# descriptive statistics of the dataset
descriptive_statistics = df.describe()

# sum of null values in the dataset
sum_of_nulls = df.isnull().sum()

# number of unique values in the dataset
num_of_uniques = df.nunique()

# dataset sorted by 2022 population in descending order (first 10 rows)
sorted_by_2022population = df.sort_values(
    by='2022 Population', ascending=False).head(10)

# dataset sorted by world population percentage in descending order (first 10 rows)
sorted_by_world_population_percentage = df.sort_values(
    by='World Population Percentage', ascending=False).head(10)

# correlation calculation
correlation = df.corr()

# correlation heatmap
plt.subplots(figsize=(10, 5))
sns.heatmap(correlation, annot=True)

# descriptive statistics of the dataset grouped by continent
df_groupedby_continent = df.groupby('Continent').describe()

# grouped by continent dataset sorted by 2022 population mean
continent_sorted_by_2022population = df_groupedby_continent.sort_values(
    by=('2022 Population', 'mean'), ascending=False)

# dataset where continent is Oceania
df_continent_ocenia = df[df['Continent'].str.contains('Oceania')]

#%%
# plot by mean population of continents per year
df_columns_in_reverse_order = df[df.columns[::-1]]
df_only_continent_populations = df_columns_in_reverse_order[
    df_columns_in_reverse_order.columns[4:13]]
df_groupedby_continent_populations_mean_transpose = df_only_continent_populations.groupby(
    'Continent').mean().transpose()
df_groupedby_continent_populations_mean_transpose.plot()

#%%
# detecting outliers with boxplots
df.boxplot(figsize=(20, 10))

# dataset only with numeric or object or float values
df_numeric = df.select_dtypes(include='number')
df_object = df.select_dtypes(include='object')
df_float = df.select_dtypes(include='float')
