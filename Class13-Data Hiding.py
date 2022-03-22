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
