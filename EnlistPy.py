# Classes

# Methods

def start_menu():
    print("\n=========================")
    print("Welcome to DLSU EnlistPy!")
    print("=========================\n")

    print("1 - LOG IN")
    print("2 - SIGN UP")

    print("Input: ", end =" ")
    action = input()

    while action != "1" and action != "2":
        print("Invalid input!")
        print("Input: ", end =" ")
        action = input()

    return action

def log_in():
    print("ID Number: ", end ="")
    username = input()

    print("Password: ", end ="")
    password = input()

    # check text files for valid username and
    # corresponding password

def sign_up():
    print("Enter First Name: ", end="")
    first_name = input()

    print("Enter Last Name: ", end="")
    last_name = input()

    print("Enter ID Number: ", end="")
    id_no = input()

    print("Enter Password: ", end="")
    password = input()

    # check if id number is not in database

    print("Type of user:")
    print("1 - Student")
    print("2 - Admin")
    print("Input: ", end =" ")
    user_type = input()

    while user_type != "1" and user_type != "2":
        print("Invalid input!")
        print("Input: ", end =" ")
        user_type = input()
    
    if user_type == "1":
        print("Enter degree: ", end="")
        degree = input()

        # instantiate new student class

    else:

        # instantiate new admin class

    
def start_program():


# Main

# action = start_menu()

# print(action)

start_program()