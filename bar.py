#Bar Graph

import matplotlib.pyplot as plt
courses = ["Python", "Java", "CSS", "SQL", "Java Script"]
students = [50, 90, 45, 34, 78]

plt.bar(courses,students)
plt.xlabel("Courses")
plt.ylabel("Students Enrolled")
plt.title("Students per Course")

plt.show()