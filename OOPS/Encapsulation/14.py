# SchoolSystem in Python, which models a school's
#  student and teacher management system:
class Person:
    def __init__(self, name, age):
        self._name = name  # Encapsulated attribute
        self._age = age  # Encapsulated attribute

    def display_info(self):
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self._student_id = student_id  # Encapsulated attribute
        self._grades = {}  # Encapsulated attribute for grades

    def add_grade(self, subject, grade):
        self._grades[subject] = grade

    def display_grades(self):
        print("Grades:")
        for subject, grade in self._grades.items():
            print(f"{subject}: {grade}")


class Teacher(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self._employee_id = employee_id  # Encapsulated attribute
        self._subjects_taught = []  # Encapsulated attribute for subjects taught

    def add_subject_taught(self, subject):
        self._subjects_taught.append(subject)
        print(f"Added {subject} to subjects taught")

    def display_subjects_taught(self):
        print("Subjects Taught:")
        for subject in self._subjects_taught:
            print(subject)


class SchoolSystem:
    def __init__(self):
        self._students = {}  # Encapsulated attribute for students
        self._teachers = {}  # Encapsulated attribute for teachers

    def enroll_student(self, student):
        self._students[student._student_id] = student
        print(f"Enrolled student: {student._name}")

    def hire_teacher(self, teacher):
        self._teachers[teacher._employee_id] = teacher
        print(f"Hired teacher: {teacher._name}")

    def get_student(self, student_id):
        return self._students.get(student_id)

    def get_teacher(self, employee_id):
        return self._teachers.get(employee_id)

    def display_students(self):
        print("Students:")
        for student_id, student in self._students.items():
            print(f"Student ID: {student_id} - Name: {student._name}")

    def display_teachers(self):
        print("Teachers:")
        for employee_id, teacher in self._teachers.items():
            print(f"Employee ID: {employee_id} - Name: {teacher._name}")


# Creating instances of the Student, Teacher, and SchoolSystem classes
student1 = Student("Alice Johnson", 16, "S123")
student2 = Student("Bob Smith", 15, "S456")

teacher1 = Teacher("Mr. Anderson", 40, "T789")
teacher2 = Teacher("Ms. Davis", 35, "T101")

school = SchoolSystem()

# Using encapsulated methods to interact with the objects
school.enroll_student(student1)
school.enroll_student(student2)

school.hire_teacher(teacher1)
school.hire_teacher(teacher2)

student1.add_grade("Math", 90)
student1.add_grade("Science", 85)

teacher1.add_subject_taught("Math")
teacher1.add_subject_taught("Physics")

school.display_students()
school.display_teachers()

student1.display_info()
student1.display_grades()

teacher1.display_info()
teacher1.display_subjects_taught()
