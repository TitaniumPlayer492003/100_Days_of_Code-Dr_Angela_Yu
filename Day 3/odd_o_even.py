# Check whether a number is odd or even.

# Example 1 Input
# 43
# Example 1 Output
# This is an odd number.
# Example 2 Input
# 94
# Example 2 Output
# This is an even number.

# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
def odd_o_even(num):
    if num % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
print(odd_o_even(number))