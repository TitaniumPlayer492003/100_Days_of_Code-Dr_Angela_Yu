#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end

city = input("What city did you grow up in? \n")
pet_name = input("What is a name for a pet? \n")

band_name = f"Your band name is {city} {pet_name}"

print(band_name)