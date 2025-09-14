from persiantools.digits import to_word
from re import match

order_list = []

def show_menu():
    print("1)Add order")
    print("2)Show orders")
    print("3)Exit")
    option = input("Enter your choice: ")
    print("-" * 50)
    return option

def name_validator(name):
    if match(r"^[a-zA-Z\s\d]{3,30}$", name):
        return True
    else:
        return False

def number_validator(number):
    return number > 0

def get_orders():
    name = input("Enter your name: ")
    price = input("Enter your price: ")
    quantity = int(input("Enter your quantity: "))

    if name_validator(name) and name_validator(price) and name_validator(quantity):
        product = {"product": name,
                   "price": price,
                   "quantity": quantity,
                   "total": price * quantity
        }
        order_list.append(product)
        print("Product added to order")
        return product
    else:
        print("Invalid Data!!!")

def get_total():
    total = 0
    for order in order_list:
        total = total + order["total"]
    return total

def show_result():
    for order in order_list:
        print(
            f"{order["product"]:12} {order["price"]:>5} * {order["quantity"]:>3} ==> {order["price"] * order["quantity"]:>8}")
    print("-" * 50)
    print(f"Total: {get_total():>24} $")
    print(to_word(get_total()))

__all__ = ["show_menu", "get_orders", "show_result"]