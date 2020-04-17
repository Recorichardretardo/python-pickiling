import json

STUDENT = {'name':'Mark','age':22,'spec':'math','fee':1000.0, 'isPass':True, 'backlogs': None}

# Serialize python Dict object to Json string

json_string = json.dumps(STUDENT)

print(json_string)


  
