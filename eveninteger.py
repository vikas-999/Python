#wap to check the first number is even or odd
#n = int(input("enter a number : "))
#print(n)
n = int(input("enter a number: "))
s = str(n)
l = int(s[0])
if l%2 == 0:
    print("the first element in a given number is EVEN number")
else:
    print("the first element in a given number is ODD number")
