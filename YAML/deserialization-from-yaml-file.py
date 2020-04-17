from pyaml import yaml


with open("student.yaml", "r") as f:
    yaml_string = yaml.safe_load(f)

print(yaml_string)
  
