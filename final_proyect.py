import tkinter as tk

def verify(data):
    if data == "":
        data == "Error"
    return data

def convert(value):
    if value.isdecimal():
        value = int(value)
    else:
        value = "Error"
    return value

def view():
    if students == {}:
        print("You have not entered any student.")
    else:
        print("Student List:")
        for name in students:
            courses = students[name]
            print(name + " - " + str(courses) + " courses")

def add():
    student_name = box_name.get()
    student_name = verify(student_name) 
    courses = box_courses.get()
    courses = convert(courses)
    if student_name == "Error":
        print("Error.")
    elif courses == "Error":
        print("Error. Enter a number.")
    else:
        students[student_name] = courses
        print("The student has been successfully registered")

def view_student():
    name = box_name.get()
    if name in students:
        print( name + " has " + str(students[name]) +" courses")
    else:
        print("That student does not have any courses.")

students = {}

window = tk.Tk()
window.config(width=400, height=300)
window.title("Final Proyect")

button_list = tk.Button(text="View student list", command=view)
button_list.place(x=10, y=10)

label_name = tk.Label(text="Student name:")
label_name.place(x=10, y=60)

box_name = tk.Entry()
box_name.place(x=110, y=60, width=150, height=20)

label_courses = tk.Label(text="Courses:")
label_courses.place(x=10, y=100)

box_courses = tk.Entry()
box_courses.place(x=110, y=100, width=50, height=20)

button_add = tk.Button(text="Add student", command=add)
button_add.place(x=10, y=150)

button_courses = tk.Button(text="View number of courses", command=view_student)
button_courses.place(x=115, y=150)

window.mainloop()