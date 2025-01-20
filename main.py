import os
import pandas as pd
import numpy as np
from datetime import datetime
import gradio as gr
from matplotlib import pyplot as plt
import seaborn as sns


"""
PLANNED LAYOUT:
1. Set-up
    - data directory filepaths
    - Global data that needs tp ne shared across terminal and web UI versions
2. Subfunctions
3. Main analysis function (and gradio version)
4. Main menu & run script
"""

### SET-UP

# Get directory path to use for dataset file paths
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data")

# Load data
races = pd.read_csv(os.path.join(data_dir, "races.csv"))
const = pd.read_csv(os.path.join(data_dir, "constructors.csv"))
const_results = pd.read_csv(os.path.join(data_dir, "constructor_results.csv"))
const_standings = pd.read_csv(os.path.join(data_dir, "constructor_standings.csv"))

#TO-DO: Point system declarations here?





### Sub functions

def input_validation(name, start_year, end_year):
    is_valid = False

    # Check if the name given is in the constructors
        
    # .str: converts value into string
    # .contains: checks if given value is in the datalist
    # .any(): returns true even if there is a single true match

    if const['name'].str.lower().str.contains(name.lower()).any():
        if (start_year < 1950) or (end_year > 2024) or (start_year > end_year):
            # Three checks, and all have to be true to be valid
            
            print('Invalid range, Please make sure to give a valid range')
        else:
            is_valid = True

    else:
        print('No match found')

    return is_valid       


def team_query(constId, start_year, end_year):
    # Componenents: get constructor results, map year/round to time var for plotting
    

    # CONSTRUCTOR RESULTS
    # Filter races by year (we'll also use this later to calc the total rounds and time mapping)
    filtered_races = races.loc[(races['year'] >= start_year) & (races['year'] <= end_year), 
                               ['raceId', 'year', 'round']]
    print("\n", filtered_races.head())

    # const_results doesn't hold year and round data, so first we merge it with filtered races
    merged_results = const_results.merge(races[['raceId', 'year', 'round',]], on = 'raceId', how = 'left')

    # then we filter for the desired constructor
    filtered_results = merged_results[(merged_results['constructorId'] == constId)]
    # remove unwanted 'status' column
    filtered_results = filtered_results.drop(columns = ['status'])
    print('\n', filtered_results.head())
    
    

    # TIME-MAPPING
    # year_fraction is an intuitive way of distributing rounds across years on a plot graph
    # We calculate this by doing the year + (the round number - 1, divided by the number of rounds)



    pass



### Analysis function
def dominance_analysis():
     
    # Get input name, year range, and validate data
    is_valid = False
    while is_valid != True:
        name = input("Please enter constructor name: ")
        start_year = int(input("Please enter starting year for analysis range: "))
        end_year = int(input("Please enter ending year of analysis range: "))

        is_valid = input_validation(name, start_year, end_year)
    


    # Get constructorId
    constId = const.loc[const["name"] == name, "constructorId"].values[0]
    #We just want the value, not a dataframe object.
    #constId = constId.values[0][0]
    print("{0} has constructor ID: {1}".format(name, constId))



    # Query data
    temp_dataframe = team_query(constId, start_year, end_year)




    print("This is a placeholder line for a breakpoint")






    #Points calculation


    #Season Round and Time mapping


    #Visualisation


    pass




### MAIN MENU

def main():
    menu_choice = ""

    while menu_choice != "0":
            #Spacer for ease of reading
            print("")
            print("")
            print("")
            print("########## ", "Current Time: ", datetime.now().strftime("%H:%M:%S"))
            print("")
            
            #Menu choices
            print("Main Menu:")
            print("0: Exit")
            print("1: Dominance Analysis")
            print("2: Launch Gradio web UI")
             
            menu_choice = input("Please select option number: ")
            
            if menu_choice == "0":
                 pass
            elif menu_choice == "1":
                dominance_analysis()
                pass
            elif menu_choice =="2":
                #instantiate gradio here
                pass
            else:
                print("Invalid choice, please try again.")





### RUN SCRIPT
if __name__ == "__main__":
    #main()
    # Or directly launch analysis/gradio UI here
    dominance_analysis()

