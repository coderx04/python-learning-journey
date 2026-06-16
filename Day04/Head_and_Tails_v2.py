import random
win = False
while not win:
      
    user_input = int(input("Choose 0 for Heads or 1 for Tails?: "))
    choice = random.randint(0,1)

    if choice == 0:
        print(f"Heads {choice}")
    else:
        print(f"Tails {choice}")
    if choice == user_input:
            print("you won!")
            win = True
    else:
        print("you lose!")