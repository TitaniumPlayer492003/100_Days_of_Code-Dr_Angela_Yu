#Step 3
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for letter in chosen_word:
    display.append('_')
print(display)

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while '_' in display != 0:
    guess = 'hehe'
    while len(guess)>1:
        guess = input("Guess a letter: ").lower()
        if len(guess)>1:
            print('You can only guess one letter.')

    #Check guessed letter
    "My method doesn't work. GPT's does."
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter
    
    print(display)
print('YOU WIN!')