balance = 100000000

exit = False

while not exit:

    user_input = int(input("press 1 for Balance\npress 2 for Deposit\npress 3 for Withdraw \npress 4 for Exit: \n"))

    if user_input == 1:
        print(f"you have {balance}.rs in your account")

    elif user_input == 2:
        dep_amount = int(input("please enter amount you wish to deposit: \n"))
        balance = dep_amount + balance
        print(f"you have deposited {dep_amount} and your total balance is {balance}")
    elif user_input == 3:
        withdraw_amount = int(input("Please enter how much you would like to withdraw? \n"))
        if withdraw_amount > balance:
            print("withdraw amount is higher than your actual bank balance")
        else:
            balance -= withdraw_amount
            print(f"Pleae collect your money, you have withdrawed {withdraw_amount} rs\nyour remaining balance is {balance}")
    elif user_input == 4:
        exit = True
    else:
        print("Invalid choice. Please select 1-4.")
            