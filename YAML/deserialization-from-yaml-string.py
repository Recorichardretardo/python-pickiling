from pyaml import yaml

STUDENT = {'name':'Mark','age':22,'spec':'math','fee':1000.0, 'isPass':True, 'backlogs': None}

yaml_string = yaml.dump(STUDENT)

print(yaml_string)



new_dect = yaml.safe_load(yaml_string)

print(type(new_dect))

print(new_dect)

for key , val in new_dect.items():
    print(key, '....', val)
  
