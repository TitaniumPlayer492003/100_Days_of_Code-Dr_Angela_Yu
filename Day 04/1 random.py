# python uses Mersenne Twister, a pseudorandom number generator
# Use wikipedia for more info (also, KhanAcademy)

import random

# produces random integer
int_num = random.randint(1,10)
print(int_num)

# produces random float in the interval [0,1) : includes 0, exclude 1
float_num = random.random()
print(float_num)
# we can just multiply float_num with int_num to get one in a particular range OR -> 
# Do this
random_number = random.uniform(0, 5)
print(random_number)

upto_two_decimal_places = "{:.2f}".format(random_number)
print(upto_two_decimal_places)