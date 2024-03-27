from students import Student
from teachers import Teacher

def add_student(students):
    id = f"S{len(students) + 1:03d}"
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    grade = input("Enter student's grade: ")
    students.append(Student(id, first_name, last_name, grade))
    print("Student added successfully.")

def add_teacher(teachers):
    id = f"T{len(teachers) + 1:03d}"
    first_name = input("Enter teacher's first name: ")
    last_name = input("Enter teacher's last name: ")
    field = input("Enter teacher's field: ")
    teachers.append(Teacher(id, first_name, last_name, field))
    print("Teacher added successfully.")

def remove_student(students, id):
    for student in students:
        if student.id == id:
            students.remove(student)
            print("Student removed successfully.")
            return
    print("Student not found.")

def remove_teacher(teachers, id):
    for teacher in teachers:
        if teacher.id == id:
            teachers.remove(teacher)
            print("Teacher removed successfully.")
            return
    print("Teacher not found.")

def update_student(students, id):
    for student in students:
        if student.id == id:
            first_name = input("Enter new first name: ")
            last_name = input("Enter new last name: ")
            grade = input("Enter new grade: ")
            student.update(first_name, last_name, grade)
            print("Student updated successfully.")
            return
    print("Student not found.")

def update_teacher(teachers, id):
    for teacher in teachers:
        if teacher.id == id:
            first_name = input("Enter new first name: ")
            last_name = input("Enter new last name: ")
            field = input("Enter new field: ")
            teacher.update(first_name, last_name, field)
            print("Teacher updated successfully.")
            return
    print("Teacher not found.")

def main():
    students = []
    teachers = []
