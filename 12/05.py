# Pickling and Unpickling

import pickle


class employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr


def display(self):
    print(self.eno, "\t", self.ename, "\t", self.esal, "\t", self.eaddr)


with open("emp.dat", "wb") as f:
    e = employee(11, "sunny", 33444, "BrodaCosta")
    pickle.dump(e, f)
    print("pickling of employee Object completed")


with open ("emp.dat",'rb') as f :
    obj = pickle.load(f)
    print("printing employee information after unpicjling ")
    obj.display()