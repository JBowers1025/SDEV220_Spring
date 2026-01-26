# M02_Loops_Conditions_73.py
# Jennifer Bowers 1/26/2026
# Assignment 7.3
# This goes through a cycle of adding 1 to a number until it meets the guess_me value

guess_me = 5

for number in range(10): # Loops through 0 to 10 or until found the guess_me
    if number < guess_me: # Continues to cycle through each number, printing "too low", until the number matches the guess_me
        print("Too low")
    elif number > guess_me: # Prints "Oops" and breaks out of the loop if the number is greater than guess_me
        print("Oops")
        break       
    else:
        print("Found it!") # Prints "Found it!" and breaks the loop when the number matches the guess_me
        break
