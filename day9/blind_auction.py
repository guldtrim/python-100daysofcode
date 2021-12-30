import os
from art import logo
print(logo)

bids = {}
highest_bid = 0
winner = {}
looper = True

def auctioneer(a, b):
    bids[a] = b

while looper:
    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    auctioneer(a = name, b = bid)
    additional = input("Are there other users that want to bid?")
    if additional == "yes":
        os.system("cls")
    else:
        looper = False
for i in bids:
    if bids[i] > highest_bid:
        winner.clear()
        highest_bid = bids[i]
        winner[name] = i
        winner[bid] = bids[i]

print(f"The winner is {winner[name]} with a bid of: {winner[bid]}")