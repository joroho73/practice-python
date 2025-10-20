'''
Guessing Game One   

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right

'''

import random as r

# generate random number
rand = r.randint(1,9)

# enter an integer
guess = None
while guess is None: # validate as number
    try:
        guess = int(input("Enter a number between 1 and 9 (inclusive)."))
        
        if rand == guess:
            print("Well done, you win!!\n" + str(rand) + " is the same as " + str(guess))
        elif rand < guess:
            print("You guessed too high.")
        else:
            print("You guessed too low.")

        print(f"You guessed: {guess}, random number: {rand}")
        
    except ValueError:
        print("Not a number, please try again.")
        




