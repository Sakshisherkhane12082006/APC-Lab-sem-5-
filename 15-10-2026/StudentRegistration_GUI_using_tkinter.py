import tkinter as tk
from tkinter import messagebox

def register():
    name = entry_name.get()
    roll = entry_roll.get()
    course = entry_course.get()

    if name == "" or roll == "" or course == "":
        messagebox.showwarning("Warning", "Please fill all fields")
    else:
        messagebox.showinfo(
            "Registration Successful",
            f"Name: {name}\nRoll No: {roll}\nCourse: {course}"
        )

root = tk.Tk()
root.title("Student Registration")
root.geometry("350x300")

tk.Label(root, text="Student Registration Form",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Student Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Roll Number").pack()
entry_roll = tk.Entry(root)
entry_roll.pack()

tk.Label(root, text="Course").pack()
entry_course = tk.Entry(root)
entry_course.pack()

tk.Button(root, text="Register", command=register).pack(pady=15)

root.mainloop()