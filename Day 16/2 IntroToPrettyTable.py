from turtle import Turtle, Screen

from prettytable import PrettyTable

table = PrettyTable()
# print(table)

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = 'l'

print(table)