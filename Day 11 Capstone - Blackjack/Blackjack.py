############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import art
import os
import random

# First let's make a dictionary, with cards as keys and their values as value, we will keep an ace = 11
card_dict = {
    "A": 11,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}


# Making a function to add a random card
def addCard(entity_cards):
    """
    Adds a card to an entity. Doesn't return anything. Just updates the current cards of given entity.
    """
    random_card = random.choice(list(card_dict.keys()))
    entity_cards.append(random_card)


# Making a function to calculate score
def calcScore(entity_cards):
    """
    Calculates the score of a given entity. Returns the score of the same entity.
    """
    entity_score = 0
    for card in entity_cards:
        entity_score += card_dict[card]
    return entity_score


# Converting a list to a string
def conv(entity_cards):
    """
    Converts a list(of cards) into a string seperated with ' '.
    """
    entity_cards_string = ""
    for card in entity_cards:
        entity_cards_string += str(card) + " "
    return entity_cards_string


play = "y"  # flag variable, indicates whether a game is in play
while play == "y":
    os.system("cls")
    # Initializing two lists which will contain user's and dealer's(computer's) cards respectively
    user_cards = []
    dealer_cards = []

    # Give one card to dealer(this card is revealed), then one card to user, then one card to dealer again(this card isn't), then finally one card to user again
    for i in range(2):
        addCard(dealer_cards)
        addCard(user_cards)

    # Finding user's current score
    user_score = calcScore(user_cards)

    hit_hold = (
        "hit"  # flag variable, indicates whether an ongoing game is finished or not
    )

    while hit_hold == "hit" and user_score < 21:
        os.system("cls")
        print(art.logo)
        print(f"Dealer's first card: {dealer_cards[0]}")
        print(f"Your cards: {conv(user_cards)}, current score: {user_score}")

        # Ask user to hit or hold
        hit_hold = input("Hit or hold? ")
        if hit_hold == "hit":
            addCard(user_cards)  # adding a card
            user_score = calcScore(user_cards)  # re-calculating user_score

        # Assigning desirable value to 'A' : 11 or 1
        if user_score > 21 and "A" in user_cards:
            user_score -= 10

    # Finding dealer's current score and making it draw one card if its score < 17 (only one card, only one time)
    dealer_score = calcScore(dealer_cards)
    if dealer_score < 17:
        addCard(dealer_cards)
        dealer_score = calcScore(dealer_cards)  # re-calculating dealer's score

    os.system("cls")
    print(art.logo)
    print(f"Dealer's cards: {conv(dealer_cards)}, Dealer's score: {dealer_score}")
    print(f"Your cards: {conv(user_cards)}, Your score: {user_score}")

    if user_score == 21:  # BLACKJACK
        os.system("cls")
        print(art.logo)
        print(f"Your cards: {conv(user_cards)}, Your score: {user_score}")
        print("BLACKJACK! THAT'S HOW IT'S DONE! 💥")
    elif user_score > 21:  # BUST
        os.system("cls")
        print(art.logo)
        print(f"Your cards: {conv(user_cards)}, Your score: {user_score}")
        print("BUST! HA! YOU'RE A MESS! 😠")
    elif dealer_score > 21:  # DEALER BUST
        print("Dealer BUST! AMATEUR HOUR! YOU'RE PATHETIC! 💥")
    elif user_score > dealer_score:  # WIN
        print("YOU WIN! NO SURPRISE THERE, CHAMP! 🏆")
    elif user_score == dealer_score:  # DRAW
        print("Draw... A TIE? HOW DISAPPOINTING. 😑")
    else:  # LOSS
        print("YOU LOST! BETTER LUCK NEXT TIME, LOSER! 😒")

    # Ask if user wants to play again
    play = input("Type 'y' to play again: ")
    if play == "y":
        os.system("cls")
