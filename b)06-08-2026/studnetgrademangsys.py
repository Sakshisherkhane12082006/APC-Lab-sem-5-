names = []
grades = []

def add_student(name, grade):
    names.append(name)
    grades.append(grade)

def update_grade(name, grade):
    if name in names:
        index = names.index(name)
        grades[index] = grade
    else:
        print("Student not found")

def remove_student(name):
    if name in names:
        index = names.index(name)
        names.pop(index)
        grades.pop(index)
    else:
        print("Student not found")

def average_grade():
    return sum(grades) / len(grades)

def display_extreme():
    print("Highest Grade:", max(grades))
    print("Lowest Grade:", min(grades))

add_student("Sakshi", 85)
add_student("Riya", 90)
add_student("Amit", 75)

update_grade("Amit", 80)
remove_student("Riya")

print("Students:", names)
print("Grades:", grades)
print("Average Grade:", average_grade())
display_extreme()