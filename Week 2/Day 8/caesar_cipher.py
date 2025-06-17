starting_word = input("What would you like to cipher? ")
shift_amount = int(input("How much would you like the letters to shift? "))

ciphered_word_builder = ""
for letter in starting_word:
    order_of_letter_plus_shift = ord(letter) + shift_amount
    in_range = True
    while in_range:
        if order_of_letter_plus_shift < 97:
            order_of_letter_plus_shift += 26
        elif order_of_letter_plus_shift > 122:
            order_of_letter_plus_shift -= 26
        else:
            in_range = False
    ciphered_word_builder = ciphered_word_builder + chr(order_of_letter_plus_shift)

print(f"Your cipher is: {ciphered_word_builder}")