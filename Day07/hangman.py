import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
    '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

words = ["apple", "frog", "zebra", "lion", "america"]

chosen_word = random.choice(words)

lives = 6
guessed_letters = []
game_over = False

print("_" * len(chosen_word))

while not game_over:

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'")
        continue

    guessed_letters.append(guess)

    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in the word.")
        print(f"Lives left: {lives}")

    display = ""

    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    print(display)
    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You win!")

    elif lives == 0:
        game_over = True
        print(f"You lose! The word was '{chosen_word}'")