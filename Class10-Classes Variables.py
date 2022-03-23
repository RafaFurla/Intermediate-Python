class Employee:
    num_of_emps = 0
    raise_amount = 1.04

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
        self.pay = int(self.pay * Employee.raise_amount)
    ''' self.pay = int(self.pay * self.raise_amount) there are two ways of calling "raise_amount". One of them is to 
    call from the Employee class and other is to call from one specificaly instance. The first is for use the 
    raise_amount value defined in Employee class. The last is for use the raise_amount value defined in the especific 
    instance, if it has one. If not found, the compilator will use the value defined in Employee class.'''


print(f"The total number of employes in the company now is: {Employee.num_of_emps}")
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
print(f"The total number of employes in the company now is: {Employee.num_of_emps}")

print(Employee.raise_amount)
print(emp_1.raise_amount)  # the compiler will look for the attribute (raise_amount) inside the instance. If not found
# it will look inside the class.
print(emp_2.raise_amount)

print(' # ' * 20)

Employee.raise_amount = 1.05  # it's easier to change the value of raise_amount if we define it inside the class. If we
# had defined it inside a method the only way to change would be inside the method manually.
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(' # ' * 20)

print(emp_1.__dict__)
emp_1.raise_amount = 1.06  # we can change the value of raise_amount just for one especifically instance. Even if this
# attribute is not defined for the instance. What happening here is that this command will create the attribute
# automatically. This will show in the emp_1.__dict__ command bellow.
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_1.__dict__)

print(' # ' * 20)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_2.pay)
