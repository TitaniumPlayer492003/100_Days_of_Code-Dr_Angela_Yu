# # Scope

# # enemies = 1

# # def increase_enemies():
# #   enemies = 2
# #   print(f"enemies inside function: {enemies}")

# # increase_enemies()
# # print(f"enemies outside function: {enemies}")

# PLAYER_STRENGTH = 10  # This var has global scope

# def drink_potion():
#     """tis a docstring"""
#     player_strength = 20  # This var has local scope
#     print(player_strength)


# # drink_potion()
# print(PLAYER_STRENGTH)

# # There is no Block Scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    if game_level<5:
        new_enemy = enemies[0]

create_enemy()
print(new_enemy) # What we learn is that if we create a variable within a function, then that varible is availaible only within that function, [remeber Scope]
