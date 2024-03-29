from os import system, name 
import time

MAX_STUDENT_UNITS = 21

# =============================== CLASSES ===============================

# a Course object that contains attributes such as course code, units, class limit,
# current student quantity, list of enrolled students, and pre requisites of the course
class Course():
    course_code = ""
    units = ""

    class_limit = ""
    student_quantity = ""
    student_list = []

    pre_requisites = []

    # initialize Course object with parameters: course code, class limit, units,
    # pre requisites, current quantity of students, and list of students
    def __init__(self, course_code, class_limit, units, pre_requisites, student_quantity, student_list):
        self.course_code = course_code
        self.class_limit = class_limit
        self.units = units
        self.pre_requisites = pre_requisites
        self.student_quantity = student_quantity
        self.student_list = student_list

    # add student in student list
    def addStudent(self, student):
        self.student_quantity = int(self.student_quantity) + 1
        self.student_list.append(student.getIdNo())

    # remove student in student list 
    def removeStudent(self, student):
        self.student_quantity = int(self.student_quantity) - 1
        self.student_list.remove(student.getIdNo())
    
    # returns course code
    def getCourseCode(self):
        return self.course_code

    # returns course units
    def getUnits(self):
        return int(self.units)

    # returns list of pre requisities
    def getPreReqs(self):
        return self.pre_requisites

    # returns class limit
    def getClassLimit(self):
        return int(self.class_limit)

    # returns current quantity of students enrolled
    def getStudentQuantity(self):
        return int(self.student_quantity)

    # returns list of enrolled students
    def getStudentList(self):
        return self.student_list

    # prints course information
    def printCourse(self):
        if self.course_code != "course code":
            print("--------------------------------------------------")
            print("Course Code:\t" + self.course_code)
            print("Units:\t\t" + self.units)
            print("Capacity:\t" + self.student_quantity + "/" + self.class_limit)
            print("Pre reqs:\t| ", end="")
            for pre_req in self.pre_requisites:
                print(pre_req + " | ", end="")
            print("\n--------------------------------------------------")


# a User object that contains a first name, last name, and id number
class User():
    first_name = ""
    last_name = ""
    id_no = ""
    
    # initialize a User object with parameters: id number, first name, and
    # last name
    def __init__(self, id_no, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id_no = id_no

    # returns first name
    def getFirstName(self):
        return self.first_name
    
    # returns last name
    def getLastName(self):
        return self.last_name
    
    # returns id number
    def getIdNo(self):
        return self.id_no


# a Student object that inherits the User class and contains attributes such as
# a degree, current total units, current courses taking up, and previous
# courses taken
class Student(User):
    degree = ""
    current_units = ""
    current_courses = []
    courses_taken = []

    # initialize a Student object with parameters: id number, first name, last name,
    # degree, previous courses taken, current units, and current courses taking up
    def __init__(self, id_no, first_name, last_name, degree, courses_taken, current_units, current_courses):
        super(Student, self).__init__(id_no, first_name, last_name)
        self.degree = degree
        self.courses_taken = courses_taken
        self.current_units = int(current_units)
        self.current_courses = current_courses

    # adds a course to current courses of student if possible
    def takeCourse(self, course):
        if canStudentEnrollInCourse(self, course):
            old_course_line = lineFormatCourse(course)
            old_student_line = lineFormatStudent(self)

            self.current_courses.append(course.getCourseCode())
            self.current_units = int(self.current_units) + int(course.getUnits())

            course.addStudent(self)

            new_course_line = lineFormatCourse(course)
            new_student_line = lineFormatStudent(self)

            print("Successfully enrolled in " + course.getCourseCode())

            updateDataInFile("courses.txt", old_course_line, new_course_line)
            updateDataInFile("students.txt", old_student_line, new_student_line)
            time.sleep(2)

    # drops a course from current courses of student if possible
    def dropCourse(self, course):
        if isStudentInCourse(self, course) == True:
            old_course_line = lineFormatCourse(course)
            old_student_line = lineFormatStudent(self)

            self.current_courses.remove(course.getCourseCode())
            self.current_units = int(self.current_units) - int(course.getUnits())
            course.removeStudent(self)

            new_course_line = lineFormatCourse(course)
            new_student_line = lineFormatStudent(self)

            print("Successfully dropped in " + course.getCourseCode())

            updateDataInFile("courses.txt", old_course_line, new_course_line)
            updateDataInFile("students.txt", old_student_line, new_student_line)
            time.sleep(2)
        else:
            print("You are not currently enrolled in this course!")
            time.sleep(2)

    # returns the student's degree
    def getDegree(self):
        return self.degree

    # returns the previous courses taken
    def getPrevCoursesTaken(self):
        return self.courses_taken

    # returns the current units
    def getCurrentUnits(self):
        return int(self.current_units)

    # returns the current courses being taken
    def getCurrentCourses(self):
        return self.current_courses

    # displays student information
    def display_info(self):
        clear()
        print("Full Name: " + self.first_name + " " + self.last_name)
        print("ID Number: " + self.id_no)
        print("Degree: " + self.degree)
        print("Units currently taking: " + str(self.current_units))
        print()
        print("Current Courses:")
        for course in self.current_courses:
            print(course)
        print()
        input("Press Enter to return to menu ")


# an Admin object that inherits the User class
class Admin(User):

    # initialize Admin object with parameters: id number, first name, and last name
    def __init__(self, id_no, first_name, last_name):
        super(Admin, self).__init__(id_no, first_name, last_name)

    # creates a new course if course has not yet been created
    def createCourse(self, courses_data):
        new_course = ""

        course_code = input("Course Code: ")

        course_found = False
        for course in courses_data:
            if course.getCourseCode() == course_code:
                course_found = True
                break
        
        if course_found:
            print("Cannot add anymore! Course already in list!")
            time.sleep(2)

        else:
            units = input("Units: ")

            pre_reqs = []
            print("Pre-Requisites for Course:")
            print("(enter 'None' if no more inputs)")
            courseInput = ""
            while courseInput != "None":
                courseInput = input()
                if courseInput != "None":
                    pre_reqs.append(courseInput)

            class_limit = input("Class Limit: ")
            student_quantity = "0"
            student_list = []

            new_course = Course(course_code, class_limit, units, pre_reqs, student_quantity, student_list)

            f = open("courses.txt","a+")
            f.write("\n" + lineFormatCourse(new_course))
            f.close()

            print("Course successfully added!")
            time.sleep(2)

    # removes course from data set if it exists
    def removeCourse(self, courses_data):

        course_to_remove = ""

        course_code = input("Course Code: ")

        course_found = False
        for course in courses_data:
            if course.getCourseCode() == course_code:
                course_found = True
                break
        
        if course_found:
            # delete from students the specified course
            students = getStudentsFromCourse(course)

            for student in students:
                student.dropCourse(course)

            # delete course from data
            line_to_remove = lineFormatCourse(course)

            f = open("courses.txt", "r")
            lines = f.readlines()
            f.close()

            f = open("courses.txt", "w")
            for line in lines:
                if line.strip("\n") != line_to_remove:
                    f.write(line)
            f.close()

            f = open("courses.txt", "r")
            new_lines = f.readlines()
            f.close()

            f = open("courses.txt", "w")
            for line in new_lines:
                if line == new_lines[-1]:
                    f.write(new_lines[-1].strip("\n"))
                else:
                    f.write(line)
            f.close()

            print("Course successfully removed!")
            time.sleep(2)

        else:
            print("Course not found!")
            time.sleep(2)


# =============================== METHODS ===============================

# displays start menu and gets input for specific action
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


# displays log in menu and gets id number and password input
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

    if lines[2].strip('\n') == "student":
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


# displays sign up menu for registering new accounts for student and admin
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

        f = open("students.txt","a+")

        f.write("\n" + id_no + ", " + first_name + ", " + last_name + ", " + degree + ", ")
        for course in prev_courses:
            f.write(course + " ")
        f.write(", 0, ")

        f.close()

        user = Student(id_no, first_name, last_name, degree, prev_courses, "0", [])

    else:
        f = open("admins.txt","a+")
        f.write("\n" + id_no + ", " + first_name + ", " + last_name)
        f.close()

        user = Admin(id_no, first_name, last_name)
    
    f = open("users.txt","a+")
    f.write("\n" + id_no + ", " + password + ", ")
    if user_type == "1":
        f.write("student")
    else:
        f.write("admin")
    f.close()

    return user


# gets course data from text file "courses.txt" and places it in a Course object list
def getCourseDataFromFile():
    f = open("courses.txt","r")
    f1 = f.readlines()
    courses = []

    for line in f1:
        data = line.rsplit(", ")
        course_code = data[0]
        units = data[1]
        pre_reqs = data[2].rsplit()
        class_limit = data[3]
        current_quantity = data[4]
        student_list = data[5].rsplit()
        
        courses.append(Course(course_code, class_limit, units, pre_reqs, current_quantity, student_list))   
        
    f.close()

    return courses


# gets student data from text file "students.txt" that are enrolled in a 
# specified course and places them in a Student object list
def getStudentsFromCourse(course):
    student_list = course.getStudentList()
    students = []

    f = open("students.txt", "r")
    lines = f.readlines()
    for line in lines:
        data = line.rsplit(", ")

        for s_id_no in student_list:
            if s_id_no == data[0]:
                id_no = data[0]
                first_name = data[1]
                last_name = data[2]
                degree = data[3]
                prev_courses = data[4].rsplit()
                current_units = data[5]
                current_courses = data[6].rsplit()

                students.append(Student(id_no, first_name, last_name, degree, prev_courses, current_units, current_courses))
    f.close()

    return students


# checks if a specified student is currently enrolled in a specified course
def isStudentInCourse(student, course):
    id_no = student.getIdNo()
    student_list = course.getStudentList()

    studentIsInList = False
    for student_no in student_list:
        if id_no == student_no:
            studentIsInList = True
    
    return studentIsInList


# checks if a specified student can currently enroll in a specified course
def canStudentEnrollInCourse(student, course):
    if course.getStudentQuantity() == course.getClassLimit():
        print("Course is full!")
        time.sleep(2)
        return False

    elif isStudentInCourse(student, course):
        print("You are already enrolled here!")
        time.sleep(2)
        return False

    elif student.getCurrentUnits() + course.getUnits() > MAX_STUDENT_UNITS:
        print("Cannot add more units to user!")
        time.sleep(2)
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
            time.sleep(2)
            return False


# updates a specific line of text in text file
def updateDataInFile(filename, old_line, new_line):
    s = open(filename).read()
    s = s.replace(old_line, new_line)
    f = open(filename, 'w')
    f.write(s)
    f.close()


# converts course data into a string to save in text file
def lineFormatCourse(course):
    line = course.getCourseCode() + ", " + str(course.getUnits()) + ", "

    for pre_req in course.getPreReqs():
        line += pre_req + " "
    
    line += ", " + str(course.getClassLimit()) + ", " + str(course.getStudentQuantity()) + ", "

    for student_id in course.getStudentList():
        line += student_id + " "

    return line


# converts student data into a string to save in text file
def lineFormatStudent(student):
    # id_no, first name, last name, degree, prev courses taken, current units, current courses
    line = student.getIdNo() + ", " + student.getFirstName() + ", " + student.getLastName() + ", " + student.getDegree() + ", "

    for prev_course in student.getPrevCoursesTaken():
        line += prev_course + " "
    
    line += ", " + str(student.getCurrentUnits()) + ", "

    for curr_course in student.getCurrentCourses():
        line += curr_course + " "
    
    return line


# clears the screen
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


# =============================== MAIN METHOD ===============================

def main():
    run = True
    user = ""

    while run == True:
        courses_data = getCourseDataFromFile()
        action = start_menu()

        clear()

        if action == "1" or action == "2":
            if action == "1":
                user = log_in()
            else:
                user = sign_up()
            
            clear()
            
            print("\nHello, " + user.getFirstName() + ".\nWhat would you like to do?\n")

            if type(user) is Student:
                while action != "4":
                    print("1 - Add Course")
                    print("2 - Drop Course")
                    print("3 - View Student Information")
                    print("4 - Log Out")
                    action = input("Enter Input: ")
                    clear()

                    if action == "1" or action == "2":
                        for course_to_display in courses_data:
                            course_to_display.printCourse()

                        course_input = input("Enter Course Code: ")

                        course_found = False
                        for course in courses_data:
                            if course.getCourseCode() == course_input:
                                course_found = True
                                break
                        
                        if course_found == False:
                            print("Course not found!")
                        
                        else:
                            if action == "1":
                                user.takeCourse(course)

                            elif action == "2":
                                user.dropCourse(course)

                    elif action == "3":
                        user.display_info()
                        input("Press Enter to Continue\n")

                    elif action == "4":
                        continue
                    else:
                        print("Invalid input!\n")

                    clear()    

            elif type(user) is Admin:
                while action != "4":
                    print("1 - Create Course")
                    print("2 - Remove Course")
                    print("3 - View All Courses")
                    print("4 - Log Out")
                    action = input("Enter Input: ")
                    clear()

                    if action == "1":
                        user.createCourse(courses_data)

                    elif action == "2":
                        for course_to_display in courses_data:
                            course_to_display.printCourse()

                        user.removeCourse(courses_data)

                    elif action == "3":
                        for course_to_display in courses_data:
                            course_to_display.printCourse()
                        input("Press Enter to return to menu ")

                    elif action == "4":
                        continue
                    else:
                        print("Invalid input!\n")

                    clear()
        else:
            run = False
            print("Program closing...")
            time.sleep(1)
    
main()