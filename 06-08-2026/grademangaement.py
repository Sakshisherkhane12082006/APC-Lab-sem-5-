students = ["Sakshi", "Shreya"]
grades = [90, 95]

# Add
students.append("Rahul")
grades.append(85)

# Update
i = students.index("Sakshi")
grades[i] = 98

# Remove
i = students.index("Shreya")
students.pop(i)
grades.pop(i)

# Display
print("Students:", students)
print("Grades:", grades)
print("Average Grade:", sum(grades)/len(grades))
print("Highest Grade:", max(grades))
print("Lowest Grade:", min(grades))