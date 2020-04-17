from pyaml import yaml

STUDENT = {'name':'Mark','age':22,'spec':'math','fee':1000.0, 'isPass':True, 'backlogs': None}

yaml_string = yaml.dump(STUDENT)

print(yaml_string)

with open("student.yaml", "w") as f:
    yaml.dump(STUDENT, f)

print("yaml file created")
  
