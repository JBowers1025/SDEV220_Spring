# M02_Loops_Conditions_72.py
# Jennifer Bowers 1/26/2026
# Assignment 7.2
# This program will guess the secret number by incrementing up by one until the number matches the secret number

import os
os.system("cls")

guess_me = 7
number = 1

while number != guess_me: # This will continue looping as long as the number doesn't equal the guess_me
    if number > guess_me: # If the number is larger than the guess_me, it prints out "oops"
        print("oops")
        number += 1 # The number increments by 1 for every time the loop reiterates
        break
    else: # If the number is lower than the guess_me, it prints "Too Low"
        print("Too low")
        number += 1 # The number increments by 1 for every time the loop reiterates
else: # Breaks out of the loop and prints "Found it" when the number matches the guess_me
    print("Found it!")