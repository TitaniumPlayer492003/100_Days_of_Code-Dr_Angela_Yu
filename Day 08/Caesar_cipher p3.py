alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(action, input_text, shift_by):
    cipher_text = ''
    if action == 'decode':
        shift_by *= -1
    for letter in input_text:
        index_of_letter = alphabet.index(letter)
        index_of_changed_letter = index_of_letter + shift_by
        while index_of_changed_letter >25:
            index_of_changed_letter -= 26
        while index_of_changed_letter <0:
            index_of_changed_letter += 26
        
        cipher_text += alphabet[index_of_changed_letter]
    print(f"The {action}d word is: {cipher_text}")
# ChatGPT Optimized:
# def caesar(action, input_text, shift_by):
#     cipher_text = ''
#     shift_by %= 26  # Ensure shift is within the range [0, 25]
#     if action == 'decode':
#         shift_by = -shift_by  # Negative shift for decoding
#     for letter in input_text:
#         if 'a' <= letter <= 'z':
#             shifted_char = chr(((ord(letter) - ord('a') + shift_by) % 26) + ord('a'))
#         else:
#             shifted_char = letter  # Keep non-alphabetic characters unchanged
#         cipher_text += shifted_char
#     print(f"The {action}d word is: {cipher_text}")

caesar(direction, text, shift)