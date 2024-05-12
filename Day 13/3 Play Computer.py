############DEBUGGING#####################

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

# Evaluate the above lines of code acting as a computer, see if there are any bugs

# Solution:
# 1994 is an axception as it is in neither intervals[(1980,1994) & (1994, infinity)]
# To fix this we can simply add an = sign at either of the conditions. One NOT BOTH
