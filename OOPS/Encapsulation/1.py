class Test(object):
    def set_val(self, val):
        self.value = val

    def get_val(self):
        return self.value


t1 = Test()
t2 = Test()
t1.set_val(10)
t2.set_val(22)

print(t1.get_val())
print(t2.get_val())
