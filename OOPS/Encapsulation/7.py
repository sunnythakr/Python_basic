class Student:
    def __init__(self, student_id, name, age):
        self._student_id = student_id  # Encapsulated attribute
        self._name = name  
        self._age = age  
        self._grades = {}  # Encapsulated attribute for storing grades

    def add_grade(self, subject, grade):
        if subject not in self._grades:
            self._grades[subject] = []
        self._grades[subject].append(grade)

    def get_average_grade(self, subject):
        if subject in self._grades:
            grades = self._grades[subject]
            if grades:
                return sum(grades) / len(grades)
            else:
                return "No grades available for this subject"
        else:
            return "Subject not found"

    def display_student_info(self):
        print(f"Student ID: {self._student_id}")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print("Grades:")
        for subject, grades in self._grades.items():
            print(f"{subject}: {grades}")


# Creating instances of the Student class
student1 = Student("001", "Alice", 18)
student2 = Student("002", "Bob", 19)

# Using encapsulated methods to interact with the objects
student1.add_grade("Math", 90)
student1.add_grade("Math", 85)
student1.add_grade("Science", 75)
student1.display_student_info()
print("Average Math grade:", student1.get_average_grade("Math"))

student2.add_grade("History", 80)
student2.add_grade("English", 95)
student2.display_student_info()
print("Average Science grade:", student2.get_average_grade("Science"))
