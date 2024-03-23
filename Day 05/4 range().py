# simple example using range() in a for loop
total = 0
for i in range(1,11): # add all numbers from [1,10]
    print(i)

# all for loops by default have a default 'step' of 1, to change a step:

for i in range (1, 11, 2):
    print(i)

# when we initialize a variable like 'total' in this case total=0, it is called an accumulator

total = 0
for number in range(1,101):
    total += number
print(total)

# Google about mathematician Carl Gauss (when he was 10)