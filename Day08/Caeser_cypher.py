

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']








# def encode(original_text, shift_amount):
#     cypher_text = ""
#     for letter in original_text:
#         if letter not in alphabet:
#             cypher_text = cypher_text + letter
#         else:
#             shifted_amount = alphabet.index(letter) + shift_amount
#             shifted_amount = shifted_amount % len(alphabet)
#             cypher_text = cypher_text + alphabet[shifted_amount]
#     print(cypher_text)


# def decode(original_text, shift_amount):
#     output_message = ""
#     for letter in original_text:
#         if letter not in alphabet:
#             output_message = output_message + letter
#         else:
#             shifted_amount = alphabet.index(letter) - shift_amount
#             shifted_amount = shifted_amount % len(alphabet)
#             output_message = output_message + alphabet[shifted_amount]
#     print(output_message)

def caesar(original_text, shift_amount, encrypt_or_decrypt):
    output_message = ""
    if encrypt_or_decrypt == "decrypt":
        shift_amount = shift_amount * -1

    for letter in original_text:
        if letter not in alphabet:
            output_message = output_message + letter
        else:
            shifted_amount = alphabet.index(letter) + shift_amount
            shifted_amount = shifted_amount % len(alphabet)
            output_message  = output_message + alphabet[shifted_amount]
    
    print(output_message)


should_continue = True

while should_continue:
    direction = input("pleae type encrypt to 'encode' and decrypt to 'decode'").lower()
    message = input("Enter a message: ").lower()
    shift = int(input("how many words needs to be shifted? "))
    caesar(original_text=message, shift_amount=shift, encrypt_or_decrypt=direction)
    
    play_again = input("type yes to continue or not to exit:\n").lower()
    if play_again == "no":
        should_continue = False
        print("Thank you")