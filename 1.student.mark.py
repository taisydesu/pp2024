course_dict = {}
student_dict = {}
mark_dict = {}

def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def student_info(number_of_students): 
    for _ in range(number_of_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        student_dict[student_id] = (student_name, dob)
    
def input_number_of_courses():
    return int(input("Enter the number of courses: "))
    
def course_info(number_of_courses):
    for _ in range(number_of_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course_dict[course_id] = course_name
    
def course_mark_input():
    number_of_marking_courses = int(input("Enter the number of courses you want to input marks: "))
    for _ in range(number_of_marking_courses):
        marking_course_id = input("Enter the course ID that you want to input marks: ")
        if marking_course_id in course_dict:
            number_of_marks = int(input("Enter the number of students you want to input marks: "))
            for _ in range(number_of_marks):
                student_id = input("Enter student ID: ")
                student_mark = float(input("Enter student mark: "))
                if student_id not in mark_dict:
                    mark_dict[student_id] = {}
                mark_dict[student_id][marking_course_id] = student_mark
        else:
            print("Course not found")
        
def course_list():
    print(f"Course list: {course_dict}")
    
def student_list():
    print(f"Student list: {student_dict}")

def mark_list():
    listing_course_id = input("Enter the course ID that you want to list marks: ")
    if listing_course_id not in course_dict:
        print("Course not found")
    else:
        print(f"Mark list for {listing_course_id}")
        for student_id, student_marks in mark_dict.items():
            if listing_course_id in student_marks:
                print(f"Student ID: {student_id}, Mark: {student_marks[listing_course_id]}")

number_of_students = input_number_of_students()
student_info(number_of_students)
number_of_courses = input_number_of_courses()
course_info(number_of_courses)
course_mark_input()

course_list()
student_list()
mark_list()