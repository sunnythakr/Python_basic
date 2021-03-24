class student:

    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print("hello my name is ",self.name)
        print(" my roll no is", self.rollno)
        print("Total marks is ", self.marks)

s = student("johnson",33,435)
s.display()

  
