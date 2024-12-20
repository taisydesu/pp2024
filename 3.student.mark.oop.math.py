import math
import numpy
import curses

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

    def input_number_of_students(self, stdscr):
        stdscr.addstr("Enter the number of students in the class: ")
        stdscr.refresh()
        return int(stdscr.getstr().decode())

    def input_number_of_courses(self, stdscr):
        stdscr.addstr("Enter the number of courses: ")
        stdscr.refresh()
        return int(stdscr.getstr().decode())

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_course(self, course):
        self.courses[course.course_id] = course

    def input_student_info(self, stdscr):
        number_of_students = self.input_number_of_students(stdscr)
        for _ in range(number_of_students):
            stdscr.addstr("Enter student ID: ")
            student_id = stdscr.getstr().decode()
            stdscr.addstr("Enter student name: ")
            student_name = stdscr.getstr().decode()
            stdscr.addstr("Enter student date of birth: ")
            dob = stdscr.getstr().decode()
            student = Student(student_id, student_name, dob)
            self.add_student(student)

    def input_course_info(self, stdscr):
        number_of_courses = self.input_number_of_courses(stdscr)
        for _ in range(number_of_courses):
            stdscr.addstr("Enter course ID: ")
            course_id = stdscr.getstr().decode()
            stdscr.addstr("Enter course name: ")
            course_name = stdscr.getstr().decode()
            course = Course(course_id, course_name)
            self.add_course(course)

    def input_marks(self, stdscr):
        stdscr.addstr("Enter the number of courses you want to input marks: ")
        number_of_marking_courses = int(stdscr.getstr().decode())
        for _ in range(number_of_marking_courses):
            stdscr.addstr("Enter the course ID that you want to input marks: ")
            marking_course_id = stdscr.getstr().decode()
            if marking_course_id in self.courses:
                stdscr.addstr("Enter the number of students you want to input marks: ")
                number_of_marks = int(stdscr.getstr().decode())
                for _ in range(number_of_marks):
                    stdscr.addstr("Enter student ID: ")
                    student_id = stdscr.getstr().decode()
                    stdscr.addstr("Enter student mark: ")
                    student_mark = float(stdscr.getstr().decode())
                    rounded_mark = math.floor(student_mark * 10) / 10.0
                    if student_id not in self.marks:
                        self.marks[student_id] = {}
                    self.marks[student_id][marking_course_id] = rounded_mark
            else:
                stdscr.addstr("Course not found\n")

    def calculate_gpa(self, student_id):
        if student_id not in self.marks:
            return None
        total_credits = 0
        total_weighted_marks = 0
        for course_id, mark in self.marks[student_id].items():
            credits = float(input(f"Enter credits for course {course_id}: "))
            total_credits += credits
            total_weighted_marks += mark * credits
        if total_credits == 0:
            return 0
        gpa = total_weighted_marks / total_credits
        return gpa

    def sort_students_by_gpa(self):
        gpa_list = []
        for student_id in self.students:
            gpa = self.calculate_gpa(student_id)
            if gpa is not None:
                gpa_list.append((student_id, gpa))
        gpa_list.sort(key=lambda x: x[1], reverse=True)
        sorted_students = [self.students[student_id] for student_id, _ in gpa_list]
        return sorted_students

    def list_courses(self, stdscr):
        stdscr.addstr("Course list:\n")
        for course in self.courses.values():
            stdscr.addstr(f"{course}\n")

    def list_students(self, stdscr):
        stdscr.addstr("Student list:\n")
        for student in self.students.values():
            stdscr.addstr(f"{student}\n")

    def list_marks(self, stdscr):
        stdscr.addstr("Enter the course ID that you want to list marks: ")
        listing_course_id = stdscr.getstr().decode()
        if listing_course_id not in self.courses:
            stdscr.addstr("Course not found\n")
        else:
            stdscr.addstr(f"Mark list for {listing_course_id}:\n")
            for student_id, student_marks in self.marks.items():
                if listing_course_id in student_marks:
                    stdscr.addstr(f"Student ID: {student_id}, Mark: {student_marks[listing_course_id]}\n")

def main(stdscr):
    school = School()
    school.input_student_info(stdscr)
    school.input_course_info(stdscr)
    school.input_marks(stdscr)
    school.list_courses(stdscr)
    school.list_students(stdscr)
    school.list_marks(stdscr)
    sorted_students = school.sort_students_by_gpa()
    stdscr.addstr("Students sorted by GPA:\n")
    for student in sorted_students:
        stdscr.addstr(f"{student}\n")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)