def register():
    print("\n--- Register ---")
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")

    print("Registration successful!\n")


def login():
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "r") as file:
        users = file.readlines()

    for user in users:
        saved_user, saved_pass = user.strip().split(",")
        if username == saved_user and password == saved_pass:
            print("Login successful! Welcome", username)
            return True

    print("Invalid username or password.\n")
    return False


def protected_page():
    print("\n--- Protected Page ---")
    print("This is a secured page. Only logged-in users can see this.\n")


while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        if login():
            protected_page()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")