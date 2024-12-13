class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DOB: {self.dob}"


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.name}"


class School:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}

    def input_number_of_students(self):
        return int(input("Enter the number of students in the class: "))

    def input_number_of_courses(self):
        return int(input("Enter the number of courses: "))

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_course(self, course):
        self.courses[course.course_id] = course

    def input_student_info(self):
        number_of_students = self.input_number_of_students()
        for _ in range(number_of_students):
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            student = Student(student_id, student_name, dob)
            self.add_student(student)

    def input_course_info(self):
        number_of_courses = self.input_number_of_courses()
        for _ in range(number_of_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            course = Course(course_id, course_name)
            self.add_course(course)

    def input_marks(self):
        number_of_marking_courses = int(input("Enter the number of courses you want to input marks: "))
        for _ in range(number_of_marking_courses):
            marking_course_id = input("Enter the course ID that you want to input marks: ")
            if marking_course_id in self.courses:
                number_of_marks = int(input("Enter the number of students you want to input marks: "))
                for _ in range(number_of_marks):
                    student_id = input("Enter student ID: ")
                    student_mark = float(input("Enter student mark: "))
                    if student_id not in self.marks:
                        self.marks[student_id] = {}
                    self.marks[student_id][marking_course_id] = student_mark
            else:
                print("Course not found")

    def list_courses(self):
        print("Course list:")
        for course in self.courses.values():
            print(course)

    def list_students(self):
        print("Student list:")
        for student in self.students.values():
            print(student)

    def list_marks(self):
        listing_course_id = input("Enter the course ID that you want to list marks: ")
        if listing_course_id not in self.courses:
            print("Course not found")
        else:
            print(f"Mark list for {listing_course_id}:")
            for student_id, student_marks in self.marks.items():
                if listing_course_id in student_marks:
                    print(f"Student ID: {student_id}, Mark: {student_marks[listing_course_id]}")


if __name__ == "__main__":
    school = School()
    school.input_student_info()
    school.input_course_info()
    school.input_marks()
    school.list_courses()
    school.list_students()
    school.list_marks()