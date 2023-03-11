import os

c_path = os.getcwd()
print(c_path)

path = r"C:\Users\13203\Documents\hadling_file"
os.chdir(path)
c_path = os.getcwd()
print(c_path)

with open("access-log.txt") as file:
    for i in file:
        ip=i.split()
        print(ip[0])
