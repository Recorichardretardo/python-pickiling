import json

json_string = '{"name":"Mark","age":22,"spec":"math","fee":1000.0, "isPass":true, "backlogs": null}'


student = json.loads(json_string)

print(type(student))
print(student)
print(student["name"])

for key, val in student.items():
    print(key, ":", val) 