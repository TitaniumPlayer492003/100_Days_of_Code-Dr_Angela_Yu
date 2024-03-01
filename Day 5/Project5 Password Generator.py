#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

import random
letters = int(input('How many letter would you like in your password? '))
symbols = int(input('How many symbols would you like in your password? '))
numbers = int(input('How many numbers would you like in your password? '))

letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = []

for i in range(0,letters):
    rand_letter = random.randint(0,51)
    password_list.append(letters_list[rand_letter])

for i in range(0,symbols):
    rand_symbol = random.randint(0,8)
    password_list.append(symbols_list[rand_symbol])

for i in range(0, numbers):
    rand_number = random.randint(0,9)
    password_list.append(rand_number)

# Eazy solution (not jumblling the password):
for alphanumeric_and_symbols in password_list:
    print(alphanumeric_and_symbols,end='')

print('\n',end='')

# Hard solution (jumbling the password):
jumbled_password_list = []

temp_password_list = list(password_list) # NOTE: the use of 'list' keyword

for character in temp_password_list:
    random_char_password_list = random.randint(0,len(password_list)-1)
    jumbled_password_list.append(password_list[random_char_password_list])
    password_list.pop(random_char_password_list) #CORRECTION_MADE: Earlier I was using .remove(character)

for char in jumbled_password_list:
    print(char,end='')
    