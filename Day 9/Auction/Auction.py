from replit import clear
from art import logo


def newBidder(name, price):
    bidder1[name] = price


def checkHighest():
    max_bid = 0
    max_bid_by = ""
    for name in bidder1:
        amount = bidder1[name]
        if amount > max_bid:
            max_bid = amount
            max_bid_by = name
    print(f"Max bid by {max_bid_by} with amount of ₹{max_bid}")


def starter():
    print(logo)


bidder1 = {}

cont = True
while cont == True:
    starter()
    name = input("Enter Your Name:\t")
    price = int(input("Enter Your price amount:\t₹"))
    newBidder(name, price)
    print(bidder1)
    prompt = input("Do you want to continue? 'y' or 'n'")
    if prompt == "n":
        checkHighest()
        cont = False
    elif prompt == "y":
        clear()
