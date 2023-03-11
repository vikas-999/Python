#wap to check the given number is prime or not
num = int(input("enter a number :"))
tables = []
count = 0
for i in range(1,101,1):
    for j in range(1,101,1):
        a = i * j
        tables.append(a)
for k in tables:
    if k == num:
        count+=1
if count == 2:
    print("its a prime")
else:
    print("not a prime")
  
