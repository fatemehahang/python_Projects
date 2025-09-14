from farayandha.orders import *

print("Order App")
print("Version 1.0")
print("MFT")
print("-" * 50)

while True:
    option = show_menu()

    match option:
        case "1":
            get_orders()
        case "2":
            show_result()
        case "3":
            break
        case _:
            print("Invalid option")

    print("-" * 50)