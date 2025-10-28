# This is a class called Student
class Student:
    # 👉 Class attribute: shared by all instances
    college_name = "ABC College"

    # Constructor method: called when a new object is created
    def __init__(self, name, roll):
        # 👉 Instance attributes: unique to each object
        self.name = name
        self.roll = roll

    # Method to display student details
    def display_info(self):
        print("Name:", self.name)           # instance attribute
        print("Roll Number:", self.roll)    # instance attribute
        print("College:", Student.college_name)  # class attribute


# Creating objects of Student
student1 = Student("Kishan", 101)
student2 = Student("Rahul", 102)

# Changing the class attribute (this affects all objects)
Student.college_name = "XYZ University"

# Displaying information
student1.display_info()
print("---")
student2.display_info()
