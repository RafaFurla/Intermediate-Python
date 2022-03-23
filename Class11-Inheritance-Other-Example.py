class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = str(first + '.' + last + '@company.com').lower()

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):  # even if i didn't defined the class with any method the compilator will seach for the
    # __init__ here in the subclass. If the compilator didn't find anything it will look in the superclass.
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # Other form to write this line of code is: Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

'''print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

print(help(Developer))
print(dev_1.email)
print(dev_2.prog_lang)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)'''

print(isinstance(mgr_1, Employee))  # is mgr_1 instance of Employee class? This is what isinstance method respond.
print(isinstance(mgr_1, Developer))
print(isinstance(Developer, Employee))
print(isinstance(Manager, Developer))
