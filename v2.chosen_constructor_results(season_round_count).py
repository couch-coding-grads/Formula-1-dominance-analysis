# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:02:02 2024

@author: pareshdokka
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests


races = pd.read_csv(r'C:\\Documents\\PYTHON COURSE\\Python F1\\f1db_csv\\races.csv')
const = pd.read_csv(r'C:\\Documents\\PYTHON COURSE\\Python F1\\f1db_csv\\constructors.csv')
const_results = pd.read_csv(r'C:\\Documents\\PYTHON COURSE\\Python F1\\f1db_csv\\constructor_results.csv')
const_standings = pd.read_csv(r'C:\\Documents\\PYTHON COURSE\\Python F1\\f1db_csv\\constructor_standings.csv')

#input constructors name
name = input('Please input the name of the constructor you would like to know about: ') 

#Checks if input for constructor name is valid
while True:
    if name not in const['name'].values: 
        constId = None
        print('Sorry the input is invalid')
        name = input('Please input the name of the constructor you would like to know about: ') 
        
    else:
        # goes through const dataframe to match the name given with its 'constructor_id'
        constId = const.loc[(const.name == name), ['constructorId']]
        # turns the single-celled dataframe with const_id into an integer
        constId_value = constId.values[0][0]
    
        get_lower = int(input('Please insert the year of races you would like from: '))  # lower limit of range
        get_upper = int(input('Please insert the year of races you would like upto: '))
    
        #Checks if input for time range is valid   
        while True:
            if get_lower>get_upper:
                print('Invalid range, Please make sure to give a valid range')
            
                # input the upper and lower ranges for the time period 
                get_lower = int(input('Please insert the year of races you would like from: '))  # lower limit of range
                get_upper = int(input('Please insert the year of races you would like upto: '))  # upper limit of range
            else:
            
                # this is an empty dataframe
                year_races = pd.DataFrame()
    
    
                total_range = list(range(get_lower, get_upper+1))
                for i in total_range:
                    year_races = pd.concat([year_races, races.loc[(races.year == i),['year','raceId']]])
                    # concatinates all the data from year year into one dataframe
    
                race_count = pd.DataFrame(year_races)      
                race_count['year_fraction'] = races['year']+races['round']/races.groupby('year')['round'].transform('max')
    
                raceIds = year_races['raceId']
    
                # all_results: all the results of all the constructors from all the races during the given time range
                all_results = const_results[const_results['raceId'].isin(raceIds)][['raceId','constructorId','points']]
    
                # main_results: results of given constructor from all the races furing the given time range
                main_results = all_results[all_results['constructorId']== constId_value]
                
                final_result = pd.merge(race_count, main_results, on='raceId')
    
                #print(all_results) # prints all results
                #print(race_count)
                #print(main_results) # prints results of the particular constructor id
                print(final_result)
                #exit loop
                break
        break
    
    