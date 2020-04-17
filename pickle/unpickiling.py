import pickle

class Student:
    def __init__(self,stdno, stdname, subject):
        self.stdno = stdno
        self.stdname = stdname
        self.subject = subject

    def display(self):
        print('STDNO:{}, STDNSME:{}, SUBJECT:{}'.format(self.stdno, self.stdname, self.subject))

# unpickiling:

with open('stdnt.pickle', 'rb') as f:
    stdntObj = pickle.load(f)

# 'rb' read binary:

print('unpickiling is done')
print(stdntObj)
stdntObj.display()