# States of america in the list they joined the union
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia",              "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0]) # first state
print(states_of_america[1]) # Second state
print(states_of_america[-1]) # last state

# Changing the name of an element from the list
states_of_america[1] = "Pencilvania"
print(states_of_america)

# Adding an element to the end of the list
states_of_america.append('Mexico')
print(states_of_america)

# Adding multiple elements
states_of_america.extend(['Canada','Greenland'])
print(states_of_america)