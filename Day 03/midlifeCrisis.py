# Same code as the roller coaster but, if age is between 45 and 55, then the ride is free
# $3 if somebody wants photos
# Use AND or OR operators

name = input('Enter your name: ')
height = float(input("Enter your height: "))
bill = 0

if height >= 120:
    age = int(input("Enter your age: "))
    if age>=45 and age<=55:
        bill += 0
        print ("CONGRATULATIONS!! You get a free ride!")
    elif age >= 18:
        bill += 12
        print ("You can ride the roller coaster, your ticket is $12")
    elif 12>=age :
        bill += 7
        print ("You can ride the roller coaster, your ticket is $7")
    else:
        bill += 5
        print ("You can ride this roller coaster, your ticket is $5")
    want_photo = input('Do you want photos for an extra $3? Y/N ')
    if want_photo == 'Y':
        bill+=3
else:
    print (f"Sorry {name}, you cannot ride the roller coaster.")
    
print(f"Your total is ${bill}.")