# Scope

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

PLAYER_STRENGTH = 10  # This var has global scope

def drink_potion():
    """tis a docstring"""
    player_strength = 20  # This var has local scope
    print(player_strength)


# drink_potion()
print(PLAYER_STRENGTH)
