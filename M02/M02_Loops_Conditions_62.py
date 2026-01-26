# M02_Loops_Conditions_62.py
# Jennifer Bowers 1/26/2026
# Assignment 6.2
# This will test a true/false of small or green again different veggy/fruit

import os
os.system("cls")

small = False
print("Small is ", small)

green = True
print("Green is ", green)

if small: # Tests if the item is small
    if green: # Tests if the small item is green
        print("It is a pea!")
        print()
    else: # Output if not green
        print("It is a cherry!")
        print()
else: # Continues this section if the item is not small
    if green: # Tests if the large item is green
        print("It is a watermellon!")
        print()
    else: # Output if not green
        print("It is a pumpkin!")
        print()