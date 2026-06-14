print("Welcome to Python RollerCoaster!")
height = int((input("Please enter your height in cm: ")))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("Please enter your age: "))
    if age <12 :
        bill = 5
        print("Child under 12 tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth Tickes are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photos = input("Do you want a phot taken? Y/N: ").lower()
    if wants_photos == "y":
        bill += 3

    print(f"your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride")