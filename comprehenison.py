'''
#compreshension
l =[1,2,3,4,5,6]
l1 = []
for i in l:
    if i%2 == 0:
        l1.append(i**2)
    else:
        l1.append(i*i*i)
print(l1)
#list comprehension
l2 = [i**2 if i%2 == 0 else i*i*i for i in l]
print(l2)

# vowels
a = ["laura","steve","bill","alex","james","bob","scott","ive"]
a1 = []
for i in a:
    if i[0] in "aeiouAEIOU":
        a1.append(i)
print(a1)
#list comprehension
a1 = [i for i in a if i[0] in "aeiouAEIOU"]
print(a1)
'''

#languages
b = ["python","perl","js","c++","php","Python"]
c = []
for i in b:
    if i[0] in "pP":
        c.append(i)
print(c)
#comprehension
c = [i for i in b if i[0] in "pP"]
print(c)


        
#consonants
a = ["laura","steve","bill","alex","james","bob","scott","ive"]
b = []
for i in a:
    if i[0] not in "aeiouAEIOU":
        b.append(i)
print(b)
# comprehension
b = [i for i in a if i[0] not in "AEIOUaeiou"]
print(b)

#6characters
names = ["apple","gmail","google","good","flipkart","goibibo"]
new = [i for i in names if len(i)<=6]
print(new)
