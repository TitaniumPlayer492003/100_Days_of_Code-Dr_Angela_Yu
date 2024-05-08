# # # Scope

# # # enemies = 1

# # # def change_enemies():
# # #   enemies = 2
# # #   print(f"enemies inside function: {enemies}")

# # # change_enemies()
# # # print(f"enemies outside function: {enemies}")

# # PLAYER_STRENGTH = 10  # This var has global scope

# # def drink_potion():
# #     """tis a docstring"""
# #     player_strength = 20  # This var has local scope
# #     print(player_strength)


# # # drink_potion()
# # print(PLAYER_STRENGTH)

# # # There is no Block Scope

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]

# def create_enemy():
#     if game_level<5:
#         new_enemy = enemies[0]

# create_enemy()
# print(new_enemy) # What we learn is that if we create a variable within a function, then that varible is availaible only within that function, [remeber Scope]

# Modifying a Global Scope
enemies = 1

def change_enemies():
    enemies = 0 # If you think about it, we are not changing the enemies variable
    # In fact we are creating a new variable with the same name that has local scope
    # To understand this you can change 'enemies' to be  of a numerical value and inside the function write enemies +=1
    print("Enemies inside function:",enemies)

change_enemies()
print("Enemies outside function:",enemies)


# The correct way to do what's intended on line 41, note teh use ogf 'global' keyword:
def increase_enemies():
    global enemies # Comment this line out to see what error you will be recieving
    enemies +=1
    print("Enemies inside the new function:", enemies)

increase_enemies()

# This however neat it looks, is bad practice. Avoid modifying a global variable inside a function as much as you can.
