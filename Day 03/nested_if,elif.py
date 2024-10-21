name = input('Enter your name: ')
height = float(input("Enter your height: "))

def canRide(n,h):
    if h >= 120:
        age = int(input("Enter your age: "))
        if age >= 18:
            return "You can ride the roller coaster, your ticket is $12"
        elif 12>=age>18 :
            return "You can ride the roller coaster, your ticket is $7"
        else:
            return "You can ride this roller coaster, your ticket is $5"
    else:
        return f"Sorry {n}, you cannot ride the roller coaster."

print(canRide(name,height))
