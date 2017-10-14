def create_student(student_id, name, grade):
    return {"student_id": student_id, "name": name, "grade": grade}


def get_student_id(student):
    return student["student_id"]


def get_student_name(student):
    return student["name"]


def get_student_grade(student):
    return student["grade"]


def set_student_id(student, student_id):
    student["student_id"] = student_id


def set_student_name(student, student_name):
    student["name"] = student_name


def set_student_grade(student, student_grade):
    student["grade"] = student_grade


def add_student(students, student):
    students.append(student)

def delete_student(students, student_id):
    l = [s for s in students if get_student_id(s) != student_id]
####### UI SECTION ########

def ui_add_student(students):
    student_id = input("student_id: ")
    name = input("name: ")
    grade = int(input("grade: "))

    student = create_student(student_id, name, grade)
    add_student(students, student)

def print_students(students):
    for student in students:
        print("ID = {0}, NAME = {1}, GRADE = {2}", get_student_id(student), get_student_name(student), get_student_grade(student))

def print_menu():
    print("1. Add student\n\
2. Print students\n\
x. Exit ")

def run_menu():
    options = {1: ui_add_student, 2: print_students}
    students = []
    while True:
        print_menu()
        op = input("Choose an option: ")

        if op == 'x':
            break

        op = int(op)
        options[op](students)

if __name__ == '__main__':
    run_menu()