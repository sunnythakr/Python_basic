# __init__() is a constructor method which helps to
# set initial values while instatiating a class.

# __init__() will get called with the attributes set in __init__(),
# when a class is instantiated.

class myConstructor(object):
    def __init__(self):
        print("Calling the __init__() constructor!\n")
        self.val = 0

    def increment(self):
        self.val = self.val + 1
        print(self.val)


con = myConstructor()
con.increment()  # will print 1
con.increment()  # will print 2