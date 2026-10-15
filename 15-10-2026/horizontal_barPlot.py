
import matplotlib.pyplot as plt

names = ['Amit', 'Sneha', 'Rahul', 'Priya', 'Neha']
marks = [80, 90, 75, 85, 95]

plt.barh(names, marks)
plt.title("Horizontal Bar Plot")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.show()
