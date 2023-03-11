import json
data = {"username":"vikas","password":1234}
json_obj = json.dumps(data)
print(json_obj)
print(type(json_obj))

import os
os.chdir(r"C:\Users\13203\Documents\json")
with open("sample.json","w") as file:
    json.dump(data,file)
    print("data dumped sucessfully")
