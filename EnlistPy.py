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

    def __init__(self, course_code, class_limit, units, time_start, time_end, pre_requisites):
        self.course_code = course_code
        self.class_limit = class_limit
        self.units = units
        self.time_start = time_start
        self.time_end = time_end
        self.pre_requisites = pre_requisites
        self.student_quantity = 0

    def addStudent(self, student):
        if self.student_quantity == class_limit:
            print("Cannot enroll in course, capacity is full!")
        else:
            self.student_quantity += 1
            self.current_students.append(student)
            print("Successfully enrolled in course!")

    def removeStudent(self, student):
        self.student_quantity =- 1
        self.current_students.remove(student)
        print("Successfully removed from class")
    
    def getCourseCode(self):
        return self.course_code

    def displayCourseInfo(self):
        print(self.course_code)
        print("Units: " + self.units)
        print(self.time_start + " - " + self.time_end)
        print(self.student_quantity + " / " + self.class_limit)
        print("Pre-requisites:")
        for course in self.pre_requisites:
            print(course.getCourseCode)



class User():
    first_name = ""
    last_name = ""
    id_no = ""
    
    def __init__(self, first_name, last_name, id_no):
        self.first_name = first_name
        self.last_name = last_name
        self.id_no = id_no

class Student(User):
    degree = ""
    current_units = ""
    max_units = 21
    current_courses = []
    courses_taken = []

    def __init__(self,first_name, last_name, id_no, degree, courses_taken, current_courses):
        super(Student, self).__init__(first_name, last_name, id_no)
        self.courses_taken = courses_taken
        self.degree = degree
        self.current_courses = current_courses
        # self.current_units = 0

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





class Admin(User):

    def __init__(self, first_name, last_name, id_no, password):
        super(Admin, self).__init__(first_name, last_name, id_no, password)

    # def createCourse(self):
    
    # def removeCourse(self, course):



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
    f = open("users.txt","r")
    f1 = f.readlines()
    id_num_found = False
    correct_password = False

    while id_num_found == False:
        print("ID Number: ", end ="")
        id_no = input()

        for line in f1:
            lines = line.rsplit(", ")

            if id_no == lines[0]:
                id_num_found = True
                break

        if id_num_found == False:
            print("Invalid ID number! Please try again")

    f.close()

    while correct_password == False:
        print("Password: ", end ="")
        password = input()

        if password != lines[1]:
            print("Invalid password! Please try again")
        else:
            correct_password = True
            print("Successfully logged in!")


def sign_up():
    print("Enter First Name: ", end="")
    first_name = input()
    print("Enter Last Name: ", end="")
    last_name = input()

    f = open("users.txt","r")
    f1 = f.readlines()
    valid_id_no = False

    while valid_id_no == False:
        valid_id_no = True
        print("Enter ID Number: ", end ="")
        id_no = input()

        for line in f1:
            lines = line.rsplit(", ")
            if id_no == lines[0]:
                print("ID Number already in use!")
                valid_id_no = False
                break
    f.close()

    print("Enter Password: ", end="")
    password = input()

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

        prev_courses = []
        courseInput = ""

        print("Input the course codes of courses that you've previously taken:")
        print("(enter 'None' if no more inputs)")
        while courseInput != "None":
            courseInput = input()
            if courseInput != "None":
                prev_courses.append(courseInput)

        # id_no, first name, last name, degree, courses taken, current units, current courses
        f = open("students.txt","a+")

        f.write("\n" + id_no + ", " + first_name + ", " + last_name + ", " + degree + ", ")
        for course in prev_courses:
            f.write(course + " ")
        f.write(", 0, ")

        f.close()

    else:
        f = open("admins.txt","a+")

        f.write("\n" + id_no + ", " + first_name + ", " + last_name)
    
        f.close()
    
    # add user data to user
    f = open("users.txt","a+")
    f.write("\n" + id_no + ", " + password + ", ")
    if user_type == "1":
        f.write("student")
    else:
        f.write("admin")
    f.close()

    
def main():
    action = start_menu()

    if action == 1:
        log_in()

    else:
        sign_up()
    

main()

