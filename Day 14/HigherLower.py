import os
import random
import art
import game_data

OPTION_A = None
OPTION_B = None

score = 0

gameOver = False

OPTION_A = random.choice(game_data.data)


def correctAnswer(a, b):
    if a["follower_count"] > b["follower_count"]:
        return "A"
    else:
        return "B"


def Guess():
    g = input("Who has more followers? Write 'A' or 'B': ").upper()
    while g != "A" and g != "B":
        g = input("Had a stroke while writing that? Try again: ").upper()
    return g


while gameOver == False:
    OPTION_B = random.choice(game_data.data)

    while OPTION_B == OPTION_A:
        OPTION_B = random.choice(game_data.data)

    os.system("cls")

    print(art.logo)
    print("Score:", score)
    print()
    print(
        "A:", OPTION_A["name"] + ",", OPTION_A["description"] + ",", OPTION_A["country"]
    )
    print(art.vs)
    print(
        "B:", OPTION_B["name"] + ",", OPTION_B["description"] + ",", OPTION_B["country"]
    )
    print()

    if Guess() == correctAnswer(OPTION_A, OPTION_B):
        score += 1
        OPTION_A = OPTION_B
    else:
        gameOver = True
        print()
        print("Incorrect! You lose.")
        print(
            "A:",
            OPTION_A["name"] + ",",
            OPTION_A["follower_count"],
            "million followers",
        )
        print(
            "B:",
            OPTION_B["name"] + ",",
            OPTION_B["follower_count"],
            "million followers",
        )
