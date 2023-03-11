#armstrong number
num = int(input("enter a number :"))
char = str(num)
arm = 0
for i in char:
    arm = arm + int(i)*int(i)*int(i)
print(arm)    
if num == arm:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
