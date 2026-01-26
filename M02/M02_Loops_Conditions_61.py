# Jennifer Bowers
# M02 Programming Assignment Loops and Conditionals
# 6.1
# 1/26/2026

import os
os.system("cls")

def game(secret, guess): # Testing the guess
    '''
    Docstring for game
    Function to test the guessed number against the secret to win
    
    :param secret: The number the guess is trying to match
    :param guess: The user's guess
    '''
    while guess != secret: # Loops so long as the guess doesn't match the secret.
        if guess > secret: # If the guess is too high
            print(f"{guess} is too high!\n")
            guess = getNum()

        elif guess < secret: # If the guess is too low
            print(f"{guess} is too low!\n")
            guess = getNum()

        else: # In case of an error
            print("Something went wrong...\n")
            break
            
    else: # If the guess is a match
        print(f"---- {guess} is just right!---- \n")

def getNum():
    '''
    Docstring fro getNum
    Gathers the user's input and checks that it is both an integer and in range
    Then returns the value
    '''
    while True:
        user_input = input("Enter a number between 1 and 10: ")

        try:
            user_input = int(user_input)

            if 1 <= user_input <= 10:
                return user_input
            else:
                print(f"{user_input} isn't a valid number or between 1 - 10.\n")

        except ValueError:
            print(f"{user_input} is not an integer.\n")

print("Lets pick the secret number!")
secret = getNum()

print("\nNow we start guessing!")
guess = getNum()

game(secret, guess)  