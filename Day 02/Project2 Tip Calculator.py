#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("What was your bill? $"))
tip = float(input("What percentage tip would you like to give? "))
persons = int(input("How many people are splitting this bill? "))

total = bill + (bill*tip/100)
per_person = total/persons
# per_person = round(total/persons,2)
# print(f"Each person should pay: ${per_person}")
print("${:.2f}".format(per_person))
