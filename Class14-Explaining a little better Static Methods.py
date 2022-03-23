class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = str(first + '.' + last + '@company.com').lower()  # see that we don't need to input all the
        # attributes. Some of them could be created using algorithms like we did here.
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod  # this class method will change the value of the raise_amt.
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod  # this class method will took a string and transform into a new instance of the class. In this case
    # it will create a new employee.
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod  # function that take a date and return whether or not that was a workday. This function has a logical connection with
# our emplyee class but it doesn't actyally depends on any specific instance or class variable. So instead we will
# create this function as a static method.
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
