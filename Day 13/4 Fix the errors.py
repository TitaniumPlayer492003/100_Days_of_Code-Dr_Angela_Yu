############DEBUGGING#####################

# Fix the Errors
age = input("How old are you?")
if age > 18:
    print("You can drive at age {age}.")

# See if there is error in the forementioned code

# Solution:
# 'age' variable is of String type, we have to explicitly convert it into an int
# AND in line 6, we want {age} to display THE age, not just print {age}.
#   We have to make the print String into an f-string
