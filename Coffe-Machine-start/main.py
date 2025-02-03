from menu import MENU,resources

profit=0
flag=True

def coffee_choose(value):
    """Returns True when order can be made ,False if ingredients insufficient."""
    is_ok = True
    for i in value:
        if value[i]>=resources[i]:
            print(f"Sorry there is not enough {i}.")
            is_ok = False
    return is_ok

def coins():
    """Return the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters(0.25)?: "))*0.25
    total += int(input("How many dimes(0.1)?: "))*0.1
    total += int(input("How many nickels(0.05)?: "))*0.05
    total += int(input("How many pennies(0.01)?: "))*0.01
    return total

def success_transaction(money,drink_cost):
    """Return True when the payment is accepted,or False if money is insufficient."""
    if money>=drink_cost:
        change=round(money-drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def make_coffee(drink_name,value):
    """Deduct the required ingredients from the resources."""
    for i in value:
        resources[i]-=value[i]
    print(f"Here is your {drink_name}☕")
while flag:
    choice=input("What would you like? (espresso/latte/cappuccino):")
    if choice=='report':
        print(f"Water {resources["water"]}ml.")
        print(f"Milk {resources["milk"]}ml.")
        print(f"Coffee {resources["coffee"]}gr.")
        print(f"Money: ${profit}.")
    elif choice=="off":
        flag=False
    else:
        coffee=MENU[choice]
        if coffee_choose(coffee["ingredients"]):
            payment=coins()
            if success_transaction(payment,coffee["cost"]):
                make_coffee(choice,coffee["ingredients"])
    
        



