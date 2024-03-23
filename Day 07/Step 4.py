#Step 4
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = [
    "dog", "cat", "horse", "rabbit", "duck", "chicken", "cow", "pig","lion", "elephant", "giraffe", "zebra", "monkey", "bear", "tiger", "sheep", "goat", "deer", "mouse", "hamster", "guinea pig", "goldfish", "turtle", "frog", "bird", "butterfly", "fish", "snake", "lizard", "koala","penguin", "panda", "kangaroo", "seal", "hippo", "bat", "racoon", "otter", "wolf", "fox", "owl", "squirrel", "shark", "whale", "dolphin", "seagull", "pelican"]

chosen_word = random.choice(word_list)

lives = 6

print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.append('_')
print(display)

while ('_' in display != 0 and lives > 0):
    guess = 'hehe'
    while len(guess)>1:
        guess = input("Guess a letter: ").lower()
        if len(guess)>1:
            print('You can only guess one letter.')
    if guess not in chosen_word:
        lives -= 1
    
    print(stages[lives])
    
    # if lives == 0:
    #     print('YOU LOSE!')
    #     print(f"Then answer was: {chosen_word}")
    #     break
    
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter
    
    print(display)

if lives > 0:
    print('YOU WIN!')
elif lives == 0:
    print('YOU LOSE!')
    print(f'The answer was: {chosen_word}')