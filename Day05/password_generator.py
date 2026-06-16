import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter_input = int(input("How many letters you want in password? "))
number_input = int(input("How many numbers you want in password? "))
symbol_input = int(input("How many symbols you want in password? "))

password = []

for l in range(letter_input):
    l = random.choice(letters)
    password.append(l)

for n in range(number_input):
    n = random.choice(numbers)
    password.append(n)

for s in range(symbol_input):
    s = random.choice(symbols)
    password.append(s)

random.shuffle(password)
print("".join(password))