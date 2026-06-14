print("Welcome to python pizza deliveries!")
size = input("What size of pizza do you want? enter \"S\" for Small \"M\" Medium and \"L\" for Large: ").lower()
pepperoni = input("Do you want pepperoni on your pizz? Y/N: ").lower()
extra_cheese = input("Do you want extra cheese? Y/N: ").lower()


bill = 0

if size == "s":
    bill += 15
    
elif size == "m":
    bill += 20
    
elif size == "l":
    bill += 25
    

if pepperoni == "y":
    if size =="s":
        bill += 2
    else:
        bill += 3

if extra_cheese =="y":
    bill += 1

print(f"your total bill for {size} size pizza is {bill}")