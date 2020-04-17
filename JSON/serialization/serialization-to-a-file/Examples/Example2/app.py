import json

STUDENT = {'name':'Mark','age':22,'spec':'math','fee':1000.0, 'isPass':True, 'backlogs': None}

with open('student.json', 'w') as f:
    json.dump(STUDENT , f, indent=4)

print("file is seralized/created.")


  
