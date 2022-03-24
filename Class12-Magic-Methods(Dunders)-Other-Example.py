class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + 'gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):  # repr: we will use this method to create a message to the python programmer that could be
        # copy exactly as it is in the display and past inside python code to create the same object that appears.
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):  # str: this post a message for the user. If the compiler doesn't find this massage it will look
        # for the message that appears in the __repr__ method
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))
# print(emp_1.__repr__())
# print(emp_1.__str__())
# print(1 + 2) could be written like: print(int.__add__(1, 2))
# print(emp_1 + emp_2)
# print(len('test')) could be written like: print('test'.__len__())
print(len(emp_1))

