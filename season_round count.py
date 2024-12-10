# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:10:37 2024

@author: pareshdokka
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests


races = pd.read_csv(r'C:\\Documents\\PYTHON COURSE\\Python F1\\f1db_csv\\races.csv')


def get_races():

    # input the upper and lower ranges for the time period 
    get_lower = int(input('Please insert the year of races you would like from: ')) # lower limit of range
    get_upper = int(input('Please insert the year of races you would like upto: ')) # upper limit of range
    
    year_races = pd.DataFrame()
    # this is an enpty dataframe
    
    total_range = list(range(get_lower, get_upper+1))
    for i in total_range:
        year_races = pd.concat([year_races, races.loc[(races.year == i),['raceId', 'year', 'round','name']]])
        # concatinates all the data from year year into one dataframe          
    
    race_count = year_races.groupby('year').size()
    # .groupby('x'): groups the dataframe with similar properties for 'X'. 
    #.size(): Tells you the count of the groups 
    # These are pandas libraries.
    
    print(race_count)
    
get_races()


#print('The number of rounds that have taken place this year are {}'.format(race_count))
