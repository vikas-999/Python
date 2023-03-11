#serialization in python
# we use json.dumps(data)
#and json.dump(data,file)
# we use above two methods for the serialization
import json
import os
a = '''
    username : balavikasss999@gmail.com
    password : Kingsvip123#
    address  : 607 6th ave s
    city     : st. cloud
    state    : minnesota
    '''
obj = json.dumps(a)
print(obj)
print(os.getcwd())
os.chdir(r"C:\Users\13203\Documents\json_file")
print(os.getcwd())

with open("sample.json","w") as file:
    json.dump(obj,file)
    print("data is added sucessfully to the file")


#deserialization
py_obj = json.loads(obj)
print(py_obj)

with open("sample.json") as file:
    b = json.load(file)
    print(b)

