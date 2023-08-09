# NOTE: BREAKING ENCAPSULATION IS BAD.

class Test(object):
    def set_val(self, val):
        self.value = val

    def get_val(self):
        print(self.value)


t1 = Test()
t2 = Test()

t1.set_val(10)
t2.set_val(1000)
t1.value = 100  # <== Overriding `set_value` directly
# <== ie..  Breaking encapsulation

t1.get_val()
t2.get_val()