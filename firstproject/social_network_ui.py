# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Login")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. View my details")
    print("2. Edit my details")
    print("3. Add a friend")
    print("4. View all my friends")
    print("5. View all my blocked friends")
    print("6. View all my messages")
    print("7. Send a message")
    print("8. Block a friend")
    print("9. <- Go back ")
    return input("Please Choose a number: ")