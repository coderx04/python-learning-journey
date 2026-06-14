
print("Welcome the tip calculator!")

total_bill = float(input("Enter total bill amount: "))
tip_percentage = float(input("How much tip % you would like to give?: "))
total_guests = int(input("How many people like to split the bill?: "))

tip_amount = (total_bill/100) * tip_percentage
grand_total = tip_amount + total_bill
per_person = grand_total / total_guests

print(f"\nYour Grand total amount is {grand_total:.2f} rs.\n Per person needs to pay {round(per_person, 2)} rs.\n Thank You, Please visit again!  ")