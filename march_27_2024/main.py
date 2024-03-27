from students import Student
from teachers import Teacher

def print_student_list(student):
    if len(student) >= 1: # if there is none then don't show
        print("\n\t ** STUDENTS ** \n")
        for i in student:
            print(i)
    else:
        print("\n No student records found \n")

def print_teacher_list(teacher):
    if len(teacher) >= 1: # if there is none then don't show
        print("\n\t ** TEACHERS ** \n")
        for i in teacher:
            print(i)
    else:
        print("\n No teacher records found \n")



def add_student(students):
    id = f"S{len(students) + 1:03d}"
    first_name = input("\n Enter student's first name: ")
    last_name = input("\n Enter student's last name: ")
    grade = input("\n Enter student's grade: ")
    students.append(Student(id, first_name, last_name, grade))
    print("\n\t*\tStudent added successfully.\t*\n\n")
    print_student_list(students)

def add_teacher(teachers):
    id = f"T{len(teachers) + 1:03d}"
    first_name = input("\n Enter teacher's first name: ")
    last_name = input("\n Enter teacher's last name: ")
    field = input("\n Enter teacher's field: ")
    teachers.append(Teacher(id, first_name, last_name, field))
    print("\n\t*\tTeacher added successfully.\t*\n\n")
    print_teacher_list(teachers)

def remove_student(students, id):
    for student in students:
        if student.id == id:
            students.remove(student)
            print("\n\t*\tStudent removed successfully.\t*\n")
            print_student_list(students)
            return
    print("\n\t*\tStudent not found.\t*\n")

def remove_teacher(teachers, id):
    for teacher in teachers:
        if teacher.id == id:
            teachers.remove(teacher)
            print("\n\t*\tTeacher removed successfully.\t*\n")
            print_teacher_list(teachers)
            return
    print("\n\t*\tTeacher not found.\t*\n")

def update_student(students, id):
    for student in students:
        if student.id == id:
            first_name = input("\n Enter new first name: ")
            last_name = input("\n Enter new last name: ")
            grade = input("\n Enter new grade: ")
            student.update(first_name, last_name, grade)
            print("\n\t*\tStudent updated successfully.\t*\n")
            print_student_list(students)
            return
    print("\n\t*\tStudent not found.\t*\n")

def update_teacher(teachers, id):
    for teacher in teachers:
        if teacher.id == id:
            first_name = input("\n Enter new first name: ")
            last_name = input("\n Enter new last name: ")
            field = input("\n Enter new field: ")
            teacher.update(first_name, last_name, field)
            print("\n\t*\tTeacher updated successfully.\t*\n")
            print_teacher_list(teachers)
            return
    print("\n\t*\tTeacher not found.\t*\n")

def main():
    students = []
    teachers = []

    while True:
        try: 
            category = input("\n Which list do you want to work on? (s)students or (t)teachers: ")
            if category == 's':
                while True:
                    print_student_list(students)
                    action = input("\n What do you want to do? (a)Add, (r)Remove, (u)Update: ")
                    if action == 'a':
                        add_student(students)
                    elif action == 'r':
                        student_id = input("\n Enter student ID to remove: ")
                        remove_student(students, student_id)
                    elif action == 'u':
                        student_id = input("\n Enter student ID to update: ")
                        update_student(students, student_id)
                    else:
                        print("\n Invalid input. Please enter 'a', 'r', or 'u'.")

                    continue_option = input("\n Do you want to do anything else on the same list? (y/n): ")
                    if continue_option.lower() != 'y':
                        break
                
            elif category == 't':
                while True:
                    print_teacher_list(teachers)
                    action = input("\n What do you want to do? (a)Add, (r)Remove, (u)Update: ")
                    if action == 'a':
                        add_teacher(teachers)
                    elif action == 'r':
                        teacher_id = input("\n Enter teacher ID to remove: ")
                        remove_teacher(teachers, teacher_id)
                    elif action == 'u':
                        teacher_id = input("\n Enter teacher ID to update: ")
                        update_teacher(teachers, teacher_id)
                    else:
                        print("\n Invalid input. Please enter 'a', 'r', or 'u'.")

                    continue_option = input("\n Do you want to do anything else on the same list? (y/n): ")
                    if continue_option.lower() != 'y':
                        break
                
            else:
                print("\n Invalid input. Please enter 's' or 't'.")
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
