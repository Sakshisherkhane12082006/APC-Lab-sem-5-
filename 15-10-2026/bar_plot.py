
import matplotlib.pyplot as plt

names = ['Amit', 'Sneha', 'Rahul', 'Priya', 'Neha']
marks = [80, 90, 75, 85, 95]

plt.bar(names, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
