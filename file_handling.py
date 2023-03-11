'''
###file handling###
import os
#to get current working directory
c_path = os.getcwd()
print(c_path)

# to change the current working directory
path = r"C:\Users\13203\Desktop\spiderpy"
os.chdir(path)
print(c_path)

#to create new directory
os.mkdir("crawl")

#to delete the directory
os.rmdir("crawl")

#opening a file without content manager and performing read,append commands
f = open("new.txt","r")
print(f.read())

f = open("new.txt","a")
f.write("class is done good night")
f.close()

#opening a file with content manager
with open("new.txt","r") as f:
    print(f.read())
    print("-" * 50)
with open("new.txt","a") as f:
    print(f.write("class will be continued tommorow"))
    print("-" * 50)
with open("new.txt","r") as f:
    print(f.read())
    print("-"*50)
with open("new.txt","w") as f:
    print("if we use the write command everything will be erased")

'''
