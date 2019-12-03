# Classes

class Course():
    course_code = ""
    units = ""

    class_limit = ""
    student_quantity = ""
    current_students = []

    time_start = ""
    time_end = ""

    pre_requisites = []

    def __init__(self, course_code, class_limit, units, pre_requisites):
        self.course_code = course_code
        self.class_limit = class_limit
        self.units = units
        self.pre_requisites = pre_requisites
        self.current_students = 0
    
    def getCourseCode(self):
        return self.course_code

    def 


class User():
    first_name = ""
    last_name = ""
    id_no = ""
    password = ""
    
    def __init__(self, first_name, last_name, id_no, password):
        self.first_name = first_name
        self.last_name = last_name
        self.id_no = id_no
        self.password = password


class Student(User):
    degree = ""
    current_units = ""
    max_units = 21
    current_courses = []
    courses_taken = []

    def __init__(self, degree, courses_taken):
        self.degree = degree
        self.current_units = 0

    # def takeCourse(self, course):


    # def dropCourse(self, course):


    def display_info(self):
        print("Full Name: " + self.first_name + " " + self.last_name)
        print("ID Number: " + self.id_no)
        print("Degree: " + self.degree)
        print("Units currently taking: " + self.current_units)
        print()
        print("Current Courses:")
        for course in current_courses:
            print(course.getCourseCode())





# class Admin(User):

#     def __init__(self):


#     def createCourse(self):
    
#     def removeCourse(self, course):



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

        courses = []
        courseInput = ""

        print("Input the course codes of courses that you've previously taken:")
        print("(enter 'None' if no more inputs)")
        while courseInput != "None":
            courseInput = input()
            if courseInput != "None":
                courses.append(courseInput)

        # instantiate new student class

    # else:

        # instantiate new admin class

    
# def start_program():


# Main

# action = start_menu()

# print(action)

# start_program()