import random
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
image = [rock, paper, scissors]
user_input = int(input("Choose 0 for rock, 1 for Paper and 2 for scissors: "))

if user_input <0 or user_input >2:
    print("Wrong Input")
else:

    computer_choice = random.randint(0,2)

    print("You Choose")
    print(image[user_input])

    print("computer Chosse")
    print(image[computer_choice])

    if user_input ==  computer_choice:
        print("Its's a Draw")
    elif (user_input == 0 and computer_choice == 2) or (user_input == 2 and computer_choice == 1) or (user_input == 1 and computer_choice == 0):
        print("you win!")
    else:
        print("you lose")