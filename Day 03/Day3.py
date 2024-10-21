def isGreater(h):
    if h >= 120:
        return "can ride the roller coster."
    else:
        return "cannot ride the roller coster."
    
name = input("Enter name: ")
height = int(input("Enter height: "))
print(name,isGreater(height))