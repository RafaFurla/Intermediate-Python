class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue-test({})".format(self._hiddenlist)


queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
# --------------------------------------------------------------
print(' # ' * 40)
# classes can have their own attributes that belong to that class and not the instances.
# Look the example bellow.


class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


print(Student.count, "students")
mark = Student('Mark')
print(Student.count, "students")
ann = Student('Ann')
print(Student.count, "students")
# --------------------------------------------------------------
print(' # ' * 40)


class Spam:
    __egg = 7

    def print_egg(self):
        print(self.__egg)


s = Spam()
s.print_egg()  # this line is a form of access the private method __egg.
print(s._Spam__egg)  # this line is a form of access the private method __egg (name of object._name of classPrivate method)
print(s.__egg)  # this last line will finish in error. It’s because you can’t access the __egg method just put s.__egg.
