#Guess the number game where a random number is generated and the user must guess it

import random

thenumber = random.randrange (1,100)

print ("Guess a number between 1 and 100.")

while True:
    
    myGuess = int(input())

    if myGuess == thenumber:
        print("You guessed the number!")
        break
    elif myGuess - thenumber <= 5 and myGuess - thenumber >= 0:
        print("Too high, but very close!")
    elif myGuess - thenumber >= -5 and myGuess - thenumber <= 0:
        print("Too low, but very close!")

    elif myGuess >= 1 and myGuess <= 100:
        if myGuess < thenumber:
            print("Too low. Keep guessing!")
        elif myGuess > thenumber:
            print("Too high. Keep guessing!")

    elif myGuess < 1 or myGuess > 100:
        print("Number out of range. What do you take me for!? Try again.")
