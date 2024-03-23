# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# NOTE: You should convert the bmi to a whole number and print out a whole number in order to pass 
# all the tests. See examples below.

# Example Input 1
# 1.75
# 80
# means: weight = 80 and height = 1.75

# Example Output 1
# 26
# Since: 80 ÷ (1.75 x 1.75) = 26.122448979591837

# Example Input 2
# 1.58
# 57
# Example Output 1
# 22

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

BMI = int(float(weight)/(float(height)**2))
print(BMI)