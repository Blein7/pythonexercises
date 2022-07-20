# HINT: You can call clear() to clear the output in the console
biddings = {}
other_bidders = False
while not other_bidders:
    name = input("Enter your name:")
    bid = int(input("Enter your bid: $"))
    biddings[name] = bid
    num_bidders = input("Is there another bidder? 'yes' or 'no')")
    if num_bidders == 'yes':
        other_bidders = False
    else:
        other_bidders = True
new_val = max(biddings.values())
keys = [k for k, v in biddings.items() if v == new_val]
print(new_val)
print(keys)
#


bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()

