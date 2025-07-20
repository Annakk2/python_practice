last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# This script creates and manages a student's gradebook using Python lists.
# It demonstrates list creation, two-dimensional lists, element modification,
# and combining multiple lists to simulate managing course grades over semesters.

# Your code below: 

subjects = ["physics", "calculus", "poetry", "history"]

print()

grades = [98, 97, 85, 88]

print()

gradebook = [
  ["physics", 98],
  ["calculus", 97],
  ["poetry", 85],
  ["history", 88]
]
print(gradebook)

print()

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

gradebook[-1][-1] = 98

gradebook[2].remove(85)

gradebook[2].append("pass")

print()

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)