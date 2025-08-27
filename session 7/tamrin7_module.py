import re

user_list = []

def show_menu():
    print("-" * 50)
    print("1)Add user")
    print("2)Login check")
    print("3)Show user")
    print("0)Exit")
    option = input("Enter your choice: ")
    print("-" * 50)
    return option

def username_validator(username):
    if re.match(r"^[a-zA-Z][a-zA-Z0-9._]{8,20}$", username):
        return True
    else:
        return False

def nickname_validator(nickname):
    if re.match(r"^[a-zA-Z][a-zA-Z0-9._]{3,30}$", nickname):
        return True
    else:
        return False

def user_check(username):
    if username in user_list:
        return True
    else:
        return False

def user_data():
    username = input("Enter username: ")
    nickname = input("Enter nickname: ")
    password = input("Enter password: ")

    status = input("User is active? (y/n): ")
    if status == "y":
        print("true")
    else:
        print("false")

    if username_validator(username) and nickname_validator(nickname)and user_check(username):
        user = {"username": username,
            "password": password,
            "nickname": nickname,
            "status": status}
        user_list.append(user)
        print("Info : user added successfully")
        return user
    else:
        print("Error : invalid username or password")
        return None

def login_check():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in user_list:
        if user_list[username]["password"] == password:
            print("Info : login ok")
        elif user_list[username]["status"] == "n" :
            print("Info : User is not active")
        else:
            print("Error : Invalid password")
    else:
        print("Error : invalid username")

def show_user():
    for user in user_list:
        print(f"{user['username']} "
              f"{user['password'],print('*******')} "
              f"{user['status']}")