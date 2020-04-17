import json

with open('student.json', 'r') as f:
    data = json.load(f)
    
print(data)
print(type(data))
print(data)
print(data["name"])
for key, val in data.items():
    print(key, ":", val)

