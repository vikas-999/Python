import os
print(os.getcwd())
os.chdir(r"C:\Users\13203\Documents\hadling_file")
print(os.getcwd())

with open("data.txt") as file:
    c=0
    for i in file:
        a = i.split()
        if a[0] =='Adidas':
            c+=1
    print(c)

with open("access-log.txt") as file:
    d ={}
    for i in file:
        a = i.split()
        if a != []:
            if a[0] not in d:
                d[a[0]] = 1
            else:
                d[a[0]] +=1
    print(d)

from collections import Counter
with open("access-log.txt") as file:
    l =[]
    for i in file:
        a = i.split()
        if a != []:
            l.append(a[0])
    print(Counter(l))

from itertools import islice
with open("access-log.txt") as file:
    r = islice(file,4)
    for i in list(r):
        print(i)

from collections import deque
with open("example.txt") as file:
    r = deque(file,4)
    print(r)


