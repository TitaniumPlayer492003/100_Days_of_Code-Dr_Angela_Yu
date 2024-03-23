import os
from art import logo

people_and_their_bids = {}

more_people = 'yes'
while more_people == 'yes':
    print(logo)
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    people_and_their_bids[name] = bid    
    more_people = input("Are there more people? ")
    os.system('cls')

bids = []
highest_bid = 0
for person in people_and_their_bids:
    if people_and_their_bids[person] > highest_bid:
        highest_bid = people_and_their_bids[person]
        winner = person
    elif people_and_their_bids[person] == highest_bid:
        winner = winner + ", " +person

print(logo)
print(f"{winner} won with a bid of ${highest_bid}!")
