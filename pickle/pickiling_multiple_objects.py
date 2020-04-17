import pickle
from stdnt import *

f= open('stdnt.pickle', 'wb')
try:
    while True:
        stdno = int(input('Enter Student number: '))
        stdname = input('Enter Student name: ')
        sub = input('Enter Subject: ')
        
        std = Student(stdno, stdname, sub)
        
        pickle.dump(std, f)
        
        option = input('Serialize one more object[Yes | No ] : ')
        
        if option.lower() == 'no':
            break
finally:
    f.close()

print('Multiple object serialized')


