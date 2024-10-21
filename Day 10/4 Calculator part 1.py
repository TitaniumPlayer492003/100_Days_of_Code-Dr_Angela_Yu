import os
from art import logo

print(logo)

def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a,b):
    return a / b


go_again = 'n'
while go_again == 'y' or go_again == 'n':
    
    if go_again == 'n':
        f_num = int(input("What's the first number?: "))
    
    print("+ \n- \n* \n/")
    opr = input("Pick an operation: ")
    
    n_num = int(input("What's the next number?: "))
    
    if opr == '+':
        result = addition(f_num,n_num)
        print(result)
    elif opr == '-':
        result = subtraction(f_num,n_num)
        print(result)
    elif opr == '*':
        result = multiplication(f_num,n_num)
        print(result)
    elif opr == '/':
        result = division(f_num,n_num)
        print(result)
    go_again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if go_again == 'y':
        f_num = result
    elif go_again == 'n':
        os.system('cls')
        print(logo)
