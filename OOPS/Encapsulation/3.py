# Here we look at another example, where we have three methods
# set_val(), get_val(), and increment_val().


class MyInteger(object):
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val

    def get_val(self):
        print(self.val)

    def increment_val(self):
        self.val = self.val + 1
        print(self.val)


a = MyInteger()
a.set_val(10)
a.get_val()
a.increment_val()
print("\n")

# Trying to break encapsulation in a new instance with an int
c = MyInteger()
c.val = 15
c.get_val()
c.increment_val()
print("\n")

# Trying to break encapsulation in a new instance with a str
b = MyInteger()
b.val = "MyString"  # <== Breaking encapsulation, works fine
b.get_val()  # <== Prints the val set by breaking encap
# b.increment_val()  # This will fail, since str + int wont work
print("\n")