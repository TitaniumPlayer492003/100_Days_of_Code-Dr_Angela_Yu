import os
from art import logo

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b


opr_dict = {"+": addition, "-": subtraction, "*": multiplication, "/": division}

go_again = "n"
while go_again is not None:

    while go_again != "y" and go_again != "n" and go_again != "exit":
        go_again = input("Say what now? ")

    if go_again == "y":
        f_num = result
    elif go_again == "n":
        os.system("cls")
        print(logo)
        f_num = float(input("What's the first number?: "))
    else:
        break

    print("+ \n- \n* \n/")
    opr = input("Pick an operation: ")
    while opr not in opr_dict:
        opr = input("Pick a valid operation: ")

    n_num = float(input("What's the next number?: "))

    result = opr_dict[opr](f_num, n_num)
    if result == int(result):
        result = int(result)
    print(f"{f_num} {opr} {n_num} = {result}")

    go_again = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation. Type 'exit' to exit: "
    )
