import os

students = []

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):  # ✅ Capitalized class name
    def __init__(self, name, age, student_id, marks):
        super().__init__(name, age)
        self.student_id = student_id
        self.marks = marks
        self.__grade = self.calculate_grade()  # ✅ Correct method name

    def calculate_grade(self):  # ✅ Correct method name
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 75:
            return "A"
        elif self.marks >= 60:
            return "B"
        else:
            return "C"

    def get_details(self):
        return {
            "name": self.name,
            "age": self.age,
            "student_id": self.student_id,
            "marks": self.marks,
            "grade": self.__grade
        }

def add_student():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        student_id = int(input("Enter your student ID: "))
        marks = int(input("Enter your marks: "))
        new_student = Student(name, age, student_id, marks)  # ✅ Corrected
        students.append(new_student)
        print("✅ Student added successfully\n")
    except ValueError:
        print("❌ Invalid input. Please try again\n")

def view_student():
    if not students:
        print("❌ No student found.\n")
        return
    print("📋 Student Details:")
    for s in students:
        details = s.get_details()
        for key, value in details.items():
            print(f"{key}: {value}")
        print("-" * 30)  # ✅ Correct indentation

def save_to_file(filename="student.txt"):
    with open(filename, "w") as file:
        for s in students:
            data = s.get_details()
            file.write(str(data) + "\n")
    print(f"✅ Saved all student details to {filename}\n")

def load_from_file(filename="student.txt"):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("❌ File not found\n")

def main():
    while True:
        print("""
        🧑‍🎓 Student Management System 🧾
        1. Add Student
        2. View All Students
        3. Save to File
        4. Load from File
        5. Exit
        """)
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_student()
            elif choice == 2:
                view_student()
            elif choice == 3:
                save_to_file()
            elif choice == 4:
                load_from_file()
            elif choice == 5:
                print("👋 Exiting program. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please select 1–5.\n")
        except ValueError:
            print("❌ Please enter a valid number.\n")

if __name__ == "__main__":
    main()
