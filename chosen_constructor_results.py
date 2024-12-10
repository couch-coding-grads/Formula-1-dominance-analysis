# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:14:46 2024

@author: pareshdokka
"""
import pandas as pd

races = pd.read_csv(r'C:\\Documents\\PYTHON COURSE\\Python F1\\f1db_csv\\races.csv')
const = pd.read_csv(r'C:\\Documents\\PYTHON COURSE\\Python F1\\f1db_csv\\constructors.csv')
const_results = pd.read_csv(r'C:\\Documents\\PYTHON COURSE\\Python F1\\f1db_csv\\constructor_results.csv')
const_standings = pd.read_csv(r'C:\\Documents\\PYTHON COURSE\\Python F1\\f1db_csv\\constructor_standings.csv')


#input constructors name
name = input('Please input the name of the constructor you would like to know about: ') 


if name not in const['name'].values: 
    print('Sorry the input is invalid')
    constId = None
    
else:
    # goes through const dataframe to match the name given with its 'constructor_id'
    constId = const.loc[(const.name == name), ['constructorId']]
    # turns the single-celled dataframe with const_id into an integer
    constId_value = constId.values[0][0]
    
  
   # input the upper and lower ranges for the time period 
    get_lower = int(input('Please insert the year of races you would like from: '))  # lower limit of range
    get_upper = int(input('Please insert the year of races you would like upto: '))  # upper limit of range
    
    # this is an empty dataframe
    year_races = pd.DataFrame()
    
    total_range = list(range(get_lower, get_upper+1))
    for i in total_range:
        year_races = pd.concat([year_races, races.loc[(races.year == i),['raceId']]])
        # concatinates all the data from year year into one dataframe
    
    raceIds = year_races['raceId']
    
    # all_results: all the results of all the constructors from all the races during the given time range
    all_results = const_results[const_results['raceId'].isin(raceIds)][['raceId','constructorId','points']]
    
    # main_results: results of given constructor from all the races furing the given time range
    main_results = all_results[all_results['constructorId']== constId_value]
 
    print(main_results) # prints results of the particular constructor id
    #print(all_results) # prints all results
