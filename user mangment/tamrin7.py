from tamrin7_module import *

while True:
   option = show_menu()

   match option:
        case "1":
            user_data()
        case "2":
            login_check()
        case "3":
            show_user()
        case "0":
            break
        case _:
            print("Error : Invalid option")