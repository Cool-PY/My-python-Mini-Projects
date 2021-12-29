# All functions

def add():
    user_name = input("Enter the name of the user: ")
    user_passwd = input("Enter the password of the user: ")
    f = open("Passwds.txt", "a")
    f.write("\nUser: ")
    f.write(user_name)
    f.write(" | ")
    f.write("Password: ")
    f.write(user_passwd)
    f.write("\n")
    f.close()
    print("Your new user name and password has been saved")
    return "Your new user name and password has been saved"

def see():
    see_file = open("Passwds.txt")
    print(see_file.read())
    see_file.close()

while True:
    print('\nYou have 3 choices\n(1) Add a user with password.\n(2) See all the users.\n(3) Quit')
    Choice1 = input("Enter: ")

    if Choice1 == "1" or Choice1 == "add":
        print("OK! Now")
        add()

    elif Choice1 == "2" or Choice1 == "see":
        print("OK!")
        see()

    elif Choice1 == "3" or Choice1 == "quit":
        print("OK!")
        quit()
