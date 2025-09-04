students = {"Alice": 85,"Bob": 90,"Charlie": 78,"David": 92,"Eva": 88}
name = input("Enter student's name: ")
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found")