from art import logo
print(logo)
# TODO-1: Ask the user for
def save_bidder():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

# TODO-2: Save data into dictionary {name: price}
    return {name: bid}
more_bidders = 'yes'
dict_of_bids = {}
while more_bidders == "yes":
# TODO-3: Whether if new bids need to be added
    dict_of_bids.update(save_bidder())
    more_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if more_bidders == "yes":
        print("\n" * 20)
# TODO-4: Compare bids in dictionary
for name in dict_of_bids:
    if dict_of_bids[name] == max(dict_of_bids.values()):
        winner = name

print(f"The winner is {winner} with a bid of ${dict_of_bids[winner]}")