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


name = input('Please input the name of the constructor you would like to know about: ')


if name not in const['name'].values: 
    print('Sorry the input is invalid')
    constId = None
    
else:
    constId = const.loc[(const.name == name),['constructorId']]
    
     
    get_lower = int(input('Please insert the year of races you would like from: '))  # lower limit of range
    get_upper = int(input('Please insert the year of races you would like upto: '))  # upper limit of range
    
    year_races = pd.DataFrame()
    #race_count = []
    # this is an enpty dataframe
    
    total_range = list(range(get_lower, get_upper+1))
    for i in total_range:
        year_races = pd.concat([year_races, races.loc[(races.year == i),['raceId']]])
    
    # Extract the raceIds from the filtered races DataFrame
    raceIds = year_races['raceId']
    
    # Filter constructor results based on the raceIds
    all_results = const_results[const_results['raceId'].isin(raceIds)][['raceId','constructorId','points']]
    main_results = all_results[all_results['constructorId'].isin(constId)]
    
    print(constId) # prints constructor id
    
    print(all_results) # prints all results
    
    print(main_results) # prints results of the particular constructor id
    
    '''
    if constId is not None:
        # Now filter directly on the column
        main_results = all_results[all_results['constructorId'] == constId]
        print(main_results)
    else:
        print("Constructor ID not found. No results to display.")
    '''  
    

    