import menu

is_on = True
money_in_machine = 0

available_water = int(menu.resources["water"])
available_milk = int(menu.resources["milk"])
available_coffee = int(menu.resources["coffee"])


def switch_off():
    """
    Sets the 'is_on' boolean to false. This causes the code to exit.
    """
    global is_on
    is_on = False


def generate_report():
    """
    Prints the report of the coffee machine's remaining contents. It prints available water, milk, coffee, and money.
    """
    print("Water:", available_water)
    print("Milk:", available_milk)
    print("Coffee:", available_coffee)
    print(f"Money: ${money_in_machine:.2f}")


def are_resources_enough():
    """
    Check if there are enough resources to make the item that the user has opted for.
    """
    item = menu.options[user_choice]["ingredients"]
    global available_water, available_milk, available_coffee
    remaining_water = available_water - item["water"]
    if "milk" in item:
        remaining_milk = available_milk - item["milk"]
    else:
        remaining_milk = 0
    remaining_coffee = available_coffee - item["coffee"]

    if remaining_water < 0:
        print("Sorry, there isn't enough water.")
    if remaining_milk < 0:
        print("Sorry, there isn't enough milk.")
    if remaining_coffee < 0:
        print("Sorry, there isn't enough coffee.")

    return remaining_water >= 0 and remaining_milk >= 0 and remaining_coffee >= 0


def charge_money():
    """
    Charges the user money in quarters, dimes, nickels, and pennies.
    """
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    amount_paid = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return amount_paid


def make_purchase():
    """
    Initiates the purchase of the user_input item.
    """
    global user_choice
    required_water = menu.options[user_choice]["ingredients"]["water"]
    if "milk" in menu.options[user_choice]["ingredients"]:
        required_milk = menu.options[user_choice]["ingredients"]["milk"]
    else:
        required_milk = 0
    required_coffee = menu.options[user_choice]["ingredients"]["coffee"]
    required_money = menu.options[user_choice]["cost"]
    print(f"{user_choice.upper()} costs ${required_money:.2f}")
    change = charge_money() - required_money

    if change < 0:
        print("Not enough money! Money refunded. Please Pay again.")
        make_purchase()
    else:
        update_machine_status(required_water, required_milk, required_coffee, required_money)
        print(f"Your change is ${change:.2f}")


def update_machine_status(current_item_water_req, current_item_milk_req, current_item_coffee_req, current_item_cost):
    """
    Updates the Coffee Machine's data, like remaining water, milk, coffee, and earned money.
    """
    global available_water, available_milk, available_coffee, money_in_machine
    available_water -= current_item_water_req
    available_milk -= current_item_milk_req
    available_coffee -= current_item_coffee_req
    money_in_machine += current_item_cost


valid_responses = ["off", "report", "espresso", "latte", "cappuccino"]

while is_on:
    user_choice = input("What would you like? An espresso, latte or cappuccino?\n").lower()
    while user_choice not in valid_responses:
        # user_choice = input("What would you like? An espresso, latte or cappuccino?\n").lower()
        user_choice = input("Invalid input! Please try again.\n").lower()
    if user_choice == "off":
        switch_off()
    elif user_choice == "report":
        generate_report()
    elif user_choice in valid_responses and are_resources_enough():
        make_purchase()
        print(f"Here is your {user_choice.upper()}! Have a nice day!")
