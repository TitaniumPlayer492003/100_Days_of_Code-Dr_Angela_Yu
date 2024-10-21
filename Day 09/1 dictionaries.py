# dictionary example
dict1 = {'bug':"An error in a program.", 'process':"Program in execution."} 

# accessing a value in a dictionary
print(dict1['bug'])

# adding a new entry in a dictionary, same for updating an entry
dict1["loop"] = "The action of doing something over and over again"
print(dict1)

# looping in a dictionary
for key in dict1:
    print(key)
    print(dict1[key])