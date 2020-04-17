import json

with open('student.json', 'r') as f:
    data = json.load(f)
    
print(data)
for key, val in data.items():
    print(key, ":", val)

