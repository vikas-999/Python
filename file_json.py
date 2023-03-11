#deserialization
import json
data = {"username":"vikas","password":1234}
json_obj = json.dumps(data)
print(json_obj)
print(type(json_obj))

python_obj = json.loads(json_obj)
print(python_obj)
print(type(python_obj))
      
import os
os.chdir(r"C:\Users\13203\Documents\json_file")
with open("sample.json") as file:
    data = json.load(file)
    print(data)
    print(type(data))
