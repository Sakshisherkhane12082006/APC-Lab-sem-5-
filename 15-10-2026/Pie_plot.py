
import matplotlib.pyplot as plt

subjects = ['Python', 'Java', 'C++', 'HTML']
marks = [30, 25, 20, 25]

plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Subject-wise Marks")
plt.show()
