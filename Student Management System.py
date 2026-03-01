class Student:
    all_students = []
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def update_marks(self, new_marks):
        self.marks = new_marks
        print(f"Marks for {self.name} updated to {self.marks}.")

    def show_details(self):
        print("\nStudent Details: ")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Marks: {self.marks}")


    @classmethod
    def find_student_by_roll(cls, roll):
        for student in cls.all_students:
            if student.roll_no == roll:
                return student
            return None

    @classmethod
    def add_student(cls):
        name = input("Enter student's name: ")
        roll_no = input("Enter student's roll no.: ")
        marks = int(input("Enter student's marks: "))
        student = cls(name, roll_no, marks)
        cls.all_students.append(student)
        print(f"Student - '{name}' added successfully!")

    @classmethod
    def update_student_marks(cls):
        roll = input("Enter student's roll no. to update marks: ")
        student = cls.find_student_by_roll(roll)
        if student:
            new_marks = int(input("Enter new marks: "))
            student.update_marks(new_marks)
            print(f"Marks for {student.name} updated successfully!")
        else:
            print("Student not found!")

    @classmethod
    def show_all_students(cls):
        if not cls.all_students:
            print("No students found.")
            return
        for student in cls.all_students:
            student.show_details()


def menu():
    while True:
        print("\n=========Student Management System============")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Show all Students")
        print("4. Exit")

        choice = int(input("Enter your option (1-4): "))
        if choice == 1:
            Student.add_student()
        elif choice == 2:
            Student.update_student_marks()
        elif choice == 3:
            Student.show_all_students()
        elif choice == 4:
            print("Exiting the system...")
            exit()
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    menu()

