import pandas as pd
import numpy as np
from datetime import datetime
import gradio as gr
from matplotlib import pyplot as plt
import seaborn as sns


"""
PLANNED LAYOUT:
1. Set-up
2. Subfunctions
3. Main analysis function (and gradio version)
4. Main menu
"""





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
                #dominance_analysis()
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

