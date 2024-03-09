"""
annonate
"""

from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

run_again = 'yes'
while run_again != 'no':
    if run_again == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n")) 

        def caesar(action, input_text, shift_by):
            cipher_text = ''
            if action == 'decode':
                shift_by *= -1
            for letter in input_text:
                if letter in alphabet:
                    index_of_letter = alphabet.index(letter)
                    index_of_changed_letter = index_of_letter + shift_by
                    while index_of_changed_letter >25: index_of_changed_letter -= 26
                    while index_of_changed_letter <0: index_of_changed_letter += 26
                    # instead of writing the above two while loops, we can just index_of_changed_letter %=26
                    cipher_text += alphabet[index_of_changed_letter]
                else:
                    cipher_text += letter
            print(f"The {action}d word is: {cipher_text}")
        caesar(direction,text,shift)
        run_again = input("Type 'yes' if you want to go again. Otherwise type 'no' \n").lower()
    else:
        while run_again != 'yes' and run_again != 'no':
            run_again = input("Say what now? \n")
if run_again=='no': print('Goodbye')