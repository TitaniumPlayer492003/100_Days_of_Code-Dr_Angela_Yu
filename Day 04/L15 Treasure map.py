'''This is a difficult challenge. 💪

You are going to write a program that will mark a spot on a map with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
Now it looks a bit more like the coordinates of a real map:

Your job is to write a program that allows you to mark a square on the map using a letter-number system.

First, your program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
Example Input 1
B3
Example Output 1
Hiding your treasure! X marks the spot.
['⬜️', '️⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', 'X', '⬜️️']

Example Input 2
B1
Example Output 2
Hiding your treasure! X marks the spot.
['⬜️', 'X', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', '⬜️️', '⬜️️']
Hints
See if this List method helps you: https://www.w3schools.com/python/ref_list_index.asp

Remember that nested Lists in Python are accessed from outside to inside. e.g. In the List below:

list = [['A', 'B, 'C'], 'E', 'F', 'G']
E is list[1] C is list[0][2]

Check your formatting. This is correctly formatted:
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
vs.

Incorrectly formatted (missing a space before 'X and extra space after the X and extra space before the comma):
#
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️','X ' , '⬜️']'''

# Start here:

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

"""map = [[A1,B1,C1],
        [A2,B2,C2],
        [A3,B3,C3]]"""
        
column = position[0] 
row = int(position[1])

if column == 'A':
    if row == 1:
        line1[0] = 'X'
    elif row == 2:
        line2[0] = 'X'
    elif row ==3:
        line3[0] = 'X'
elif column == 'B':
    if row == 1:
        line1[1] = 'X'
    elif row == 2:
        line2[1] = 'X'
    elif row ==3:
        line3[1] = 'X'
elif column == 'C':
    if row == 1:
        line1[2] = 'X'
    elif row == 2:
        line2[2] = 'X'
    elif row ==3:
        line3[2] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

## I wrote the code above. The solution however is a little more difficult to understand but a lot, lot shorter
# Start here:

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter = position[0]
abc = ['A','B','C']
letter_as_number = int(abc.index(letter)) # Get? What's happening here?
number = int(position[1])-1

map[number][letter_as_number] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")