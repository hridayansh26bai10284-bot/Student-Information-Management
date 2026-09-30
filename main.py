# Program to manage student information using Dictionary and Set

# 1. Create a dictionary containing student names, roll numbers and marks
students = {
    "Rahul": {"roll": 101, "marks": 85},
    "Priya": {"roll": 102, "marks": 90},
    "Amit": {"roll": 103, "marks": 78},
    "Neha": {"roll": 104, "marks": 90}
}

# 2. Display all keys, values and key-value pairs
print("Keys:", students.keys())
print("Values:", students.values())
print("Key-Value Pairs:", students.items())

# 3. Add a new student
students["Karan"] = {"roll": 105, "marks": 92}
print("\nAfter adding Karan:")
print(students)

# 4. Update marks of an existing student
students["Amit"]["marks"] = 88
print("\nAfter updating Amit's marks:")
print(students)

# 5. Delete a student
del students["Neha"]
print("\nAfter deleting Neha:")
print(students)

# 6. Check whether a particular student name exists
name = "Rahul"

if name in students:
    print("\n", name, "exists in the dictionary.")
else:
    print("\n", name, "does not exist in the dictionary.")

# 7. Find maximum and minimum marks
marks = [student["marks"] for student in students.values()]

print("\nMaximum marks:", max(marks))
print("Minimum marks:", min(marks))

# 8. Create a set containing all unique marks
unique_marks = set(marks)
print("\nUnique marks set:", unique_marks)

# 9. Add and remove an element from the set
unique_marks.add(95)
print("After adding 95:", unique_marks)

unique_marks.remove(95)
print("After removing 95:", unique_marks)

# 10. Create a second set and perform set operations
second_set = {88, 92, 100}

print("\nFirst Set:", unique_marks)
print("Second Set:", second_set)

print("Union:", unique_marks.union(second_set))
print("Intersection:", unique_marks.intersection(second_set))
print("Difference:", unique_marks.difference(second_set))
print("Symmetric Difference:",
      unique_marks.symmetric_difference(second_set))

# 11. Check subset and disjoint
print("\nIs first set a subset of second set?",
      unique_marks.issubset(second_set))

print("Are both sets disjoint?",
      unique_marks.isdisjoint(second_set))

# 12. Create a list with duplicate marks and remove duplicates
duplicate_marks = [85, 88, 92, 85, 88, 85]

print("\nList with duplicate marks:", duplicate_marks)

no_duplicates = set(duplicate_marks)
print("After removing duplicates:", no_duplicates)

# 13. Count frequency of each mark using a dictionary
frequency = {}

for mark in duplicate_marks:
    if mark in frequency:
        frequency[mark] += 1
    else:
        frequency[mark] = 1

print("\nFrequency of each mark:", frequency)

# 14. Display final dictionary and unique marks set
print("\nFinal Student Dictionary:")
print(students)

print("Final Unique Marks Set:")
print(unique_marks)