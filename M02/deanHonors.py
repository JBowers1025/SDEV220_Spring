# M02 Lab Case Study: if... else and while
# Jennifer Bowers 1/26/2026
# M02CaseStudyBowers.py
# This program determines if a student is part of the dean's list and honor roll.

import os
os.system("cls") # Clears the ouput (terminal) screen

print("\nThis will determine if the student has made it onto the Dean's list and/or Honor Roll.\n")

def deanHonor(name):
    '''
    Tests the GPA of the student against the requirements to be on the dean's list and honor roll.
    '''

    firstName = (input("Please enter the student's first name: ")).capitalize()
    
    gpa = input("Please enter the student's GPA: ")

    try:  # Tests if the GPA value is a float number
        float(gpa)
        gpa = float(gpa)

        if 0 <= gpa <= 4:  # Tests to make sure the GPA is a valid value

            if 3.5 <= gpa:  # Tests if on the Dean's list
                print(f"\n{firstName} {lastName} is on the Dean's list and the Honor Roll!\n")

            elif 3.25 <= gpa < 3.5:  # Tests if on the Honor Roll
                print(f"\n{firstName} {lastName} is on the Honor Roll!\n")

            else:  # (gpa < 3.25) Returns a statement that the student wasn't on either list
                print(f"\nSorry, {firstName} {lastName} isn't on either list.\n")

        else:  # Returns that the GPA was not in the correct number range.
            print(f"\nThe gpa value of {gpa} is not value between 0.0 and 4.0.\n")

    except ValueError:  # Returns that the GPA was not a float
        print(f"\nThe gpa value of {gpa} is not a valid number.\n")

# Beginning input to start the program
lastName = (input("Please enter the student's last name or ZZZ to quit: ")).capitalize()

# Repeating block of code. If the value is ZZZ the program will quit.
while lastName.upper() != "ZZZ":
   deanHonor(lastName)

   # Repeats the program
   lastName = (input("\nPlease enter the next student's last name: ")).capitalize()

# Program's closing message   
print("\n--------\nThanks for using this program. Have a great day!\n--------\n") 