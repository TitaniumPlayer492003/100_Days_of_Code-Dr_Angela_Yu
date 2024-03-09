alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(input_text = text ,shift_by = shift):
    for letter in input_text:
        index_letter = alphabet.index(letter)
        encrypted_letter_index = index_letter + shift_by
        while encrypted_letter_index >= 26:
            encrypted_letter_index = encrypted_letter_index - 26
        print(alphabet[encrypted_letter_index],end='')
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

def decrypt (input_text = text, shift_by = shift):
    for letter in input_text:
        encrypted_letter_index = alphabet.index(letter)
        index_letter = encrypted_letter_index - shift_by
        while index_letter < 0:
            index_letter = index_letter + 26
        print(alphabet[index_letter],end ='')

if direction == 'encode':
    encrypt(text,shift)
else:
    decrypt(text, shift)