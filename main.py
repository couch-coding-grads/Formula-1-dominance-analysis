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





### Sub functions

def input_validation(name, start_year, end_year):
    is_valid = False

    # Make sure name is capitalised first letter only
    # Check if team constructor name is correct, if years are in range and right way around

    #For now, just pass true
    is_valid = True
     
    return is_valid


def team_query():
    
    pass



### Analysis function
def dominance_analysis():
     
    # Get input name, year range, and validate data
    is_valid = False
    while is_valid != True:
        name = input("Please enter constructor name: ")
        start_year = input("Please enter starting year for analysis range: ")
        end_year = input("Please enter ending year of analysis range: ")

        is_valid = input_validation(name, start_year, end_year)
    


    # Get constructorID
    constId = const.loc[(const.name == name), ["constructorId"]]
    #We just want the value, not a dataframe object
    constId = constId.values[0][0]
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
    main()
    # Or directly launch analysis/gradio UI here
    dominance_analysis()

