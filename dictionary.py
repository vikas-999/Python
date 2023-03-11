'''
#wap to create a dictionary if it has values as string print in reverse order or else print the same thing
d = {"a":1,"b":"ball","c":"camel","d":"1234","e":5}
print("the given dictionary is  : ",d)
new_dict = dict({})
k = []
v = []
v1 = []
for h  in d.keys():
    k.append(h)
for i in d.values():
    v.append(i)
for j in v:
    if j == str(j):
        v1.append(j[::-1])
    else:
        v1.append(j)
for l in range(len(k)):
    for m in range(len(v1)):
        new_dict.update({k[l]:v1[l]})
print("the updated dictionary is:",new_dict)





#wap to print a elements in an iterable of reverse order
ch = input("enter a string :")
for i in ch:
    print(i[::-1],end = ' ')




#interchange the keys and values in dictionary
d = {"a":1,"b":2,"c":3,"d":4,"e":5}
print("the given dictionary is  : ",d)
new_dict = dict({})
k = []
v = []
for h  in d.keys():
    k.append(h)
for i in d.values():
    v.append(i)
for l in range(len(k)):
    for m in range(len(v)):
        new_dict.update({v[l]:k[l]})
print("the updated dictionary is:",new_dict)




#vowel dictionary
s = "haii good afternoon welcome to afternun session"
print("the given string is : ",s)
a= s.split()
new_l = []
new_v = []
new_dict = dict({})
for i in range(len(a)):
    if a[i][0] in "aeiouAEIOU":
        new_l.append(a[i])
for j in new_l:
    new_v.append(len(j))
for a in range(len(new_l)):
    for b in range(len(new_v)):
        new_dict.update({new_l[a]:new_v[a]})
print(new_dict)


'''

#list of words ends with vowels
s = "haii hello everyone how are you"
print("the given string is : ",s)
new_l = s.split()
list1 = []
for i in range(len(new_l)):
    if new_l[i][-1] in "aeiouAeiou":
        list1.append(new_l[i])
print(list1)
        

        




    
    


    
        
