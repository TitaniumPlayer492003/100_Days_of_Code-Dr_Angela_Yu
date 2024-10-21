import os
import art
import random

numToGuess = random.randint(1,100)

os.system('cls')
print(art.logo)
# print(f"psst, the answer is {numToGuess}.")
print("I am thinking of a nmber between 1 and 100.")

gameMode = None
while gameMode != 'easy' and gameMode !='hard':
    gameMode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if gameMode == 'easy' : remainingTries = 10
elif gameMode == 'hard' : remainingTries = 5

userGuess = None
while remainingTries > 0:
    userGuess = int(input(f"You have {remainingTries} tries remaining. Make a guess: "))
    if userGuess == numToGuess:
        print(f"YES! {numToGuess} is the correct answer!") 
        break
    elif userGuess > numToGuess: print("Too High")
    else: print("Too Low")
    remainingTries -= 1

if remainingTries == 0: print("You Lose! You are out of guesses ☹")