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
    username_check = input("Enter username: ")
    password_check = input("Enter password: ")
    for user in user_list:
        if user["username"] == username_check:
            print("Info : login ok")
            if user["password"] == password_check :
                if user["status"] == "y":
                    print("Info : login ok")
                else:
                    print("Info : user locked")
            else:
                print("Error : Invalid password")

def show_user():
    for user in user_list:
        print(f"Username :{user['username']:10} "
              f"Nickname :{user['nickname']:10} "
              f"Password :{'*' * len(user['password']):10,} "
              f"Status :{bool(user['status'])}")