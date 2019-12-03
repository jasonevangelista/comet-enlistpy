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
    
    def __init__(self, id_no, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id_no = id_no

    def getFirstName(self):
        return first_name

class Student(User):
    degree = ""
    current_units = ""
    max_units = 21
    current_courses = []
    courses_taken = []

    def __init__(self, id_no, first_name, last_name, degree, courses_taken, current_units, current_courses):
        super(Student, self).__init__(id_no, first_name, last_name)
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

    def __init__(self, id_no, first_name, last_name):
        super(Admin, self).__init__(id_no, first_name, last_name)

    # def createCourse(self):
    
    # def removeCourse(self, course):



# Methods

def start_menu():
    print("\n=========================")
    print("Welcome to DLSU EnlistPy!")
    print("=========================\n")

    print("1 - LOG IN")
    print("2 - SIGN UP")
    print("3 - EXIT PROGRAM")

    print("Input: ", end =" ")
    action = input()

    while action != "1" and action != "2" and action != "3":
        print("Invalid input!")
        print("Input: ", end =" ")
        action = input()

    return action

def log_in():
    user = ""
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

    if lines[3] == "student":
        f = open("students.txt","r")
        f1 = f.readlines()
        for line in f1:
            data = line.rsplit(", ")
            if data[0] == id_no:
                break
        f.close()

        first_name = data[1]
        last_name = data[2]
        degree = data[3]
        prev_courses_taken = data[4].split()
        current_units = data[5]
        current_courses = data[6].split()

        user = Student(id_no, first_name, last_name, degree, courses_taken, current_units, current_courses)
    
    else:
        f = open("admins.txt","r")
        f1 = f.readlines()
        for line in f1:
            data = line.rsplit(", ")
            if data[0] == id_no:
                break
        f.close()

        first_name = data[1]
        last_name = data[2]

        user = Admin(id_no, first_name, last_name)
    
    return user
    
    
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
    run = True
    user = ""

    while run == True:
        action = start_menu()

        if action == "1" or action == "2":
            if action == "1":
                user = log_in()
            else:
                user = sign_up()
            
            print("Hello, " + user.getFirstName() + ".\nWhat would you like to do?")

            if user is student:
                print("1 - Add Course")
                print("2 - Drop Course")
                print("3 - View Student Information")
            else:
                print("1 - View All Courses")
                print("2 - Create Course")
                print("3 - Remove Course")
        
        else:
            run = False
    
    
main()

