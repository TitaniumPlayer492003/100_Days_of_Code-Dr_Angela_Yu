# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print('Hi :3')
    print('How do you do?')
    print("Isn't the weather nice today?")

# greet()

def greetWithName(name):
    print(f'Hi {name} :3')
    print(f'How do you do {name}?')

# greetWithName("Avijeet")

username = input() # Here, username is the parameter, and input() the argument
greetWithName(username)
