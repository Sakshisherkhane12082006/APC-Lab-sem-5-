project1 = {"Amit", "Riya", "Sakshi", "Rahul"}
project2 = {"Sakshi", "Rahul", "Neha", "Priya"}

print("Employees in both projects:", project1.intersection(project2))

print("Employees only in Project 1:", project1.difference(project2))
print("Employees only in Project 2:", project2.difference(project1))

print("Total unique employees:", project1.union(project2))