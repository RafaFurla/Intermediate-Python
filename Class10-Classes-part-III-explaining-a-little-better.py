class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = str(first + '.' + last + '@company.com').lower()  # see that we don't need to input all the
        # attributes. Some of them could be created using algorithms like we did here.

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.fullname)  # if you call a method and don't put the parenthesis after that, python will undestand
# that you want to print the method and not the return value of the method.
print(emp_1.fullname())
print(Employee.fullname(emp_1))  # you can also call the fullname method using directly the class. But in this case
# you have to input the self attribute directly. Diffently of the print above, if you use this print here the attribute
# "self" will not pass automatically. This is a little obvious because class can create a lot of instances (objects)
# not just the emp_1. Then you have to mention what instance you are talking about.
print(emp_1.email)  # if you call an attribute you don't need to put the parenthesis after that.
print(emp_2.email)
