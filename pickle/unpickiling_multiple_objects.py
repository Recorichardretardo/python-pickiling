import pickle


f= open('stdnt.pickle', 'rb')
try:
    while True:
        try:
            stdnts = pickle.load(f)
            stdnts.display()
        except EOFError:
            break

finally:
    f.close()

print('unpickiling is done')
 