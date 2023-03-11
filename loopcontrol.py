'''
#wap to print the first "n" elements from the given list
a = ["facebook","netflix","amazon","apple","google"]
n = int(input("enter the range : "))
for i in a:
    for j in range(len(i)):
        if j<n:
            print(i[j],end="")
        else:
            break


#continue
b = [2,3,5,4,9,6,7,10,12,33,45,2,1,7]
for i in b:
    if i>10:
        continue
    print(i)
    

#pass
c = [1,2,3,4,5,6]
for i in c:
    pass
print(i)
'''
#palindrome using for loop
s = input("enter a string : ")
r = []
for i in s[::-1]:
    r.append(i)
if r == list(s):
    print("palindrome")
else:
    print("not a palindrome")

     
 
