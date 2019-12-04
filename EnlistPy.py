
MAX_STUDENT_UNITS = 21

# Classes

class Course():
    course_code = ""
    units = ""

    class_limit = ""
    student_quantity = ""
    current_students = []

    pre_requisites = []

    def __init__(self, course_code, class_limit, units, pre_requisites, student_quantity, current_students):
        self.course_code = course_code
        self.class_limit = class_limit
        self.units = units
        self.pre_requisites = pre_requisites
        self.student_quantity = student_quantity
        self.current_students = current_students

    def addStudent(self, student):
        self.student_quantity = int(self.student_quantity) + 1
        self.current_students.append(student)

    def removeStudent(self, student):
        self.student_quantity =- 1
        self.current_students.remove(student)
        print("Successfully removed from class")
    
    def getCourseCode(self):
        return self.course_code

    def getStudentQuantity(self):
        return int(self.student_quantity)

    def getClassLimit(self):
        return int(self.class_limit)

    def getCurrentStudents(self):
        return self.student_quantity

    def getPreReqs(self):
        return self.pre_requisites

    def getUnits(self):
        return int(self.units)


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
        return self.first_name
    
    def getIdNo(self):
        return self.id_no


class Student(User):
    degree = ""
    current_units = ""
    current_courses = []
    courses_taken = []

    def __init__(self, id_no, first_name, last_name, degree, courses_taken, current_units, current_courses):
        super(Student, self).__init__(id_no, first_name, last_name)
        self.degree = degree
        self.courses_taken = courses_taken
        self.current_units = int(current_units)
        self.current_courses = current_courses

    def takeCourse(self, course):
        self.current_courses.append(course)
        self.current_units = int(self.current_units) + int(course.getUnits())
        course.addStudent(self)


    # def dropCourse(self, course):

    def getPrevCoursesTaken(self):
        return self.courses_taken

    def getCurrentUnits(self):
        return int(self.current_units)


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

    if lines[2] == "student":
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

        user = Student(id_no, first_name, last_name, degree, prev_courses_taken, current_units, current_courses)
    
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
    user = ""

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

        # id_no, first name, last name, degree, courses taken, current units, current courses
        user = Student(id_no, first_name, last_name, degree, prev_courses, "0", [])

    else:
        f = open("admins.txt","a+")

        f.write("\n" + id_no + ", " + first_name + ", " + last_name)
    
        f.close()

        user = Admin(id_no, first_name, last_name)
    
    # add user data to user
    f = open("users.txt","a+")
    f.write("\n" + id_no + ", " + password + ", ")
    if user_type == "1":
        f.write("student")
    else:
        f.write("admin")
    f.close()

    return user

def getCourseDataFromFile():
    f = open("courses.txt","r")

    f1 = f.readlines()
    courses = []

    for line in f1:
        data = line.rsplit(", ")

        course_code = data[0]
        units = data[1]
        # time_start = data[2]
        # time_end = data[3]
        pre_reqs = data[2].rsplit()
        class_limit = data[3]
        current_quantity = data[4]
        student_list = data[5].rsplit()
        
        courses.append(Course(course_code, class_limit, units, pre_reqs, current_quantity, student_list))   
        
    f.close()

    return courses

def isStudentInCourse(student, course):
    id_no = student.getIdNo()
    student_list = course.getCurrentStudents()

    studentIsInList = False
    for student_no in student_list:
        if id_no == student_no:
            studentIsInList = True
    
    return studentIsInList
        
def canStudentEnrollInCourse(student, course):
    if course.getStudentQuantity == course.getClassLimit:
        print("Course is full!")
        return False

    elif isStudentInCourse(student, course):
        print("You are already enrolled here!")
        return False

    elif student.getCurrentUnits() + course.getUnits() > MAX_STUDENT_UNITS:
        print("Cannot add more units to user!")
        return False

    else:
        prev_courses = student.getPrevCoursesTaken()
        pre_reqs = course.getPreReqs()

        canEnroll = False
        num = 0
        numPreReq = len(pre_reqs)

        for course in prev_courses:
            for pre_req in pre_reqs:
                if course == pre_req:
                    num += 1
        
        if num == numPreReq:
            return True
        else:
            print("Not enough pre-requisites!")
            return False


# def updateCourseInFile():


# def updateStudentInFile():


def main():
    run = True
    user = ""

    courses_data = getCourseDataFromFile()

    while run == True:
        action = start_menu()

        if action == "1" or action == "2":
            if action == "1":
                user = log_in()
            else:
                user = sign_up()
            
            print("\nHello, " + user.getFirstName() + ".\nWhat would you like to do?")

            if type(user) is Student:
                print("1 - Add Course")
                print("2 - Drop Course")
                print("3 - View Student Information")
                action = input("Enter Input: ")

                if action == "1":
                    course_to_add = input("Enter Course Code: ")

                    course_found = False
                    for course in courses_data:
                        if course.getCourseCode() == course_to_add:
                            course_found = True
                            break
                    
                    if course_found == False:
                        print("Course not found!")

                    else:
                        if canStudentEnrollInCourse(user, course) == True:
                            user.takeCourse(course)
                            print("Successfully enrolled in " + course.getCourseCode())
                            #end of action
    

                elif action == "2":
                    course_to_drop = input("Enter Course Code: ")

                elif action == "3":
                    user.display_info()

                else:
                    print("Invalid input!")

            elif type(user) is Admin:
                print("1 - Create Course")
                print("2 - Remove Course")
                # print("3 - View All Courses")
                action = input("Enter Input: ")

                # if action == "1":

                # elif action == "2":

                # elif action == "3":

                # else:

        else:
            run = False
    
    
main()