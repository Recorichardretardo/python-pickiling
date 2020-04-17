
import jsonpickle

class Student:
    def __init__(self,stdno, stdname, subject):
        self.stdno = stdno
        self.stdname = stdname
        self.subject = subject

    def display(self):
        print('STDNO:{}, STDNSME:{}, SUBJECT:{}'.format(self.stdno, self.stdname, self.subject))

stdnt = Student(1, 'Rolf', 'history')


json_string = jsonpickle.encode(stdnt)

print(json_string)

std = jsonpickle.decode(json_string)

print(type(std))
print(std)
std.display()