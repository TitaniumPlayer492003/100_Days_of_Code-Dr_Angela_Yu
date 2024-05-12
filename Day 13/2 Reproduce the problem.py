############DEBUGGING#####################

# Reproduce the Bug
from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# Make it so that every time the code is run it generates an error

# # Solution:
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(6, 6)
# print(dice_imgs[dice_num])
