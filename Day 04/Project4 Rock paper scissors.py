rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random


user_choice = input("Rock, paper or scissors? ").lower()

list = [rock,paper,scissors]
index = random.randint(0,2)
computer_choice = list[index]


if user_choice == "rock" or user_choice == "r":
    print(rock)
    print("Computer chose: ",computer_choice)
    if computer_choice == rock:
        print('Draw')
    elif computer_choice == paper:
        print('You lose! Paper covers rock!')
    else:
        print("You win! Rock crushes scissors!")
elif user_choice == 'paper' or user_choice == 'p':
    print(paper)
    print("Computer chose: ",computer_choice)
    if computer_choice == rock:
        print('You win! Paper covers rock!')
    elif computer_choice == paper:
        print('Draw')
    else:
        print("You lose! Scissor cuts paper!")
elif user_choice == 'scissors' or user_choice == 's':
    print(scissors)
    print("Computer chose: ",computer_choice)
    if computer_choice == rock:
        print('You lose! Rock crushes scissors')
    elif computer_choice == paper:
        print('You win! Scissor cuts paper!')
    else:
        print("Draw")
else:
    print('Invalid input. Is there a typo?')
