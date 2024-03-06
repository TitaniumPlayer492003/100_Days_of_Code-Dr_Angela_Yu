# FINAL hangman

import random
import os
from utility_files import logo as lg
from utility_files import stages
import utility_files

chosen_word = random.choice(utility_files.word_list) # Choosing a word randomly
lives = 6 # Setting the max amount of lives

print(lg) # printing the logo
print(f'Pssst, the solution is {chosen_word}.') #Solution, used while debugging

display = [] #Initializing a list that will contain _ equal to the number of letters
for letter in chosen_word: #adding _ to the list
    display.append('_')
print(f"{' '.join(display)}") # Printing display in form of just blanks instead of a list

incorrect_guesses = [] # Initializing a list that will keep a record of all the wrong inputs

# Main Logic
while ('_' in display != 0 and lives > 0): #looping while there are _s left and lives > 0
    
    # Taking Input
    guess = 'hehe' #Initializing 'guess', setting it to a length > 1
    while len(guess)>1: # Taking input; making sure only letter is input-ted
        guess = input("Guess a letter: ").lower() # Converting input into lower_case
        if len(guess)>1:
            print('You can only guess one letter.')
        else: # Clearing the screen after every user_guess, improving UX
            os.system('cls')
    
    # If guess is correct
    if guess in chosen_word:
        if guess in display:
            print(f"You've already guessed {guess}")
        for index, letter in enumerate(chosen_word):# replacing _ with guessed letter in display; telling the user the guess is correct
            if letter == guess:
                display[index] = letter
                print('Correct guess!')
    
    # If guess is incorrect
    else:
        # If a wrong guess repeats; no lives are lost, and the user is notified.
        if guess in incorrect_guesses:
            print(f"You've already guessed {guess}. No life will be deducted.")
        
        # In case of an incorrect guess, reducing a life, and adding incorrect guess to the list of incorrect guesses
        else: 
            lives -= 1
            incorrect_guesses.append(guess)
            print(f"'{guess}' is not in the word.")
            print(stages[lives]) #NOTE: Lives(in ascii art) are only displayed if a life is lost in that attempt
    
    print(f"{' '.join(display)}") # Printing display in form of just blanks instead of a list

# Once we exit the loop:
# Check Win
if lives > 0:
    print('YOU WIN!')

# Else, Loss; tell user the correct answer
else:
    print('YOU LOSE!')
    print(f'The answer was: {chosen_word}')