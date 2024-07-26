# Auction Program
from diagram import logo

print(logo)
continue_bid = True
name_bid = {}

# while continue_bid == True:
#     name = input("What is your name? : ")
#     bid = int(input("What is your bid? : $"))
#     name_bid[name] = bid

#     bidders_available = input("Are there any other bidders? Type 'yes' or 'no'")
#     if bidders_available ==  "no":
#         continue_bid = False

# name_list = list(name_bid.keys())
# bid_list = list(name_bid.values())

# index1 = bid_list.index(max(bid_list))
# print(f"The winner is {name_list[index1]} with a bid of ${bid_list[index1]}")

def find_highest_bidder(bid_dict):
    highest_bid = 0
    winner = ""
    for bidder in bid_dict:
        bid_amount = bid_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while continue_bid == True:
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $"))
    name_bid[name] = bid

    bidders_available = input("Are there any other bidders? Type 'yes' or 'no'")
    if bidders_available ==  "no":
        continue_bid = False

find_highest_bidder(name_bid)


