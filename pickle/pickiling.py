import pickle


class Student:
    def __init__(self,stdno, stdname, subject):
        self.stdno = stdno
        self.stdname = stdname
        self.subject = subject

    def display(self):
        print('STDNO:{}, STDNSME:{}, SUBJECT:{}'.format(self.stdno, self.stdname, self.subject))


stdnt = Student(1, 'Rolf', 'history')

# pickiling:

with open('stdnt.pickle', 'wb') as f:
    pickle.dump(stdnt, f)


# 'wb' means 'write binary' and is used for the file handle: 
# open('stdnt.pickle', 'wb') which writes the pickeled data into a file.

print("object pickiling is done.")