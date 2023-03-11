'''
#while loop
#just using while loop
a = [22,11,34,23,46,35,58,69,70]
i = 0
while i < len(a):
    if a[i]%2 == 0:
        print(a[i],"is even")
    else:
        print(a[i],"is odd")
    i = i + 1

# wap to print odd numbers from 1 to 20
a = 1
b = 20
while a < b:
    if not a%2 == 0:
        print(a,"is odd")
    a = a+1

#wap to print numbers from 0 to 9
a= 0
b= 10
while a < b:
    print(a)
    a =a+1

# wap to print even numbers from 0 to 20 in single line
a = 0
b = 21
l =[]
while a < b:
    if a%2 == 0:
        print(a,end=',')
    a = a+1

# -10 to -1
a = -10
b = -1
while a < b:
    print(a)
    a = a + 1

# 20 to 0
a = 20
b = 0
while a > b:
    print(a)
    a = a-1
    '''
