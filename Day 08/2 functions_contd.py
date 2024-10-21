username = 'Avijeet'#input("Enter name: ")
loc = 'LPU' #input("Enter location: ")

def greetWithPos(name,location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")

greetWithPos(username,loc)
# These ^ (above) are called positional arguments, because they depend on the position

# Below are Keyword Arguments, because they depend on keywords
def greetWithKey(name = username,location=loc):
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")

greetWithKey(loc,username)
