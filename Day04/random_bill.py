import random

diners_name = ["Pankaj", "Mayank", "Himanshu", "Vipul", "Pradeep", "Vinay"]

print(random.choice(diners_name))

#2

index = random.randint(0,len(diners_name))

print(diners_name[index])