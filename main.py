accounts = []

def register():
    print("---- REGISTER ----")
    username = input("Username: ")
    while any(account["username"] == username for account in accounts):
        print('This username is already in use.')
        username = input("\nUsername: ")
    password = input("Password: ")
    accounts.append({"username":username, "password":password})
    print("Profile successfully registered.")

def login():
    print("---- LOGIN ----")
    username = input("Username: ")
    if not any(user["username"] == username for user in accounts):
        print('This username is not registered.')
        return
    else:
        password = input("Password: ")
        password_correct = None
        for account in accounts:
            if account["username"] == username:
                password_correct = account["password"]
                break
        if password_correct == password:
            print("Logged in successfully!!!")
        else:
            print("Incorrect password")
                
while True:
    print("\n---------------------")
    option = input("1 - Login" \
    "\n2 - Register" \
    "\n3 - Exit" \
    "\n    chose one: ")
    print("---------------------")
    if option == "1":
        login()
    elif option == "2":
        register()
    elif option == "3" or option == "":
        break
    else:
        print("Invalid option")
