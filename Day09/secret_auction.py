

participants = {}
continue_bidding = True
while continue_bidding:

    name = input("What is your name?\n")
    bid_amount = int(input("What is your bid? \n$"))
    participants[name] = bid_amount
    other_bidders = input("Are there any other bidders? type yes or no\n").lower()

    if other_bidders == "no":
        continue_bidding = False
    elif other_bidders == "yes":
        print("\n" * 100)
        continue_bidding = True
    else:
        print("wrong input")
        other_bidders = input("Are there any other bidders? type yes or no\n").lower()

highest_bid = max(participants, key = participants.get)
        
print(f"The winner is {highest_bid} with highest bid of ${participants[highest_bid]}")
# looked up google to get highest bid number




