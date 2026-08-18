attendance = {
    "Monday": {"Amit", "Riya", "Sakshi"},
    "Tuesday": {"Amit", "Riya", "Sakshi", "Rahul"},
    "Wednesday": {"Amit", "Riya"},
    "Thursday": {"Amit", "Riya", "Sakshi"},
    "Friday": {"Amit", "Riya", "Sakshi"}
}

# Students attending all classes
all_students = set.intersection(*attendance.values())

print("Students attended all classes:", all_students)

# Total unique students
unique_students = set.union(*attendance.values())

print("Total unique students:", len(unique_students))

# Students attending only one class
count = {}

for students in attendance.values():
    for student in students:
        count[student] = count.get(student, 0) + 1

only_one = {student for student in count if count[student] == 1}

print("Students attended only one class:", only_one)