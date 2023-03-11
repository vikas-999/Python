import datetime
print("Here is the menu,  you can pick as many items as you can")
add = 0
d = {'rice' : 17, 'chicken' : 18, 'shrimp soup' : 21, 'paneer' : 20, 'tandoori' : 25}
print("FOOD MENU")
for i in d.items():
    print(i)
print()
d1 = {'jameson' : 8, 'black label' : 10, 'summit' : 8}
print("DRINKS MENU")
for z in d1.items():
    print(z)
print()
a = int(input("enter 1 if you want to add food, or else enter 0 if you are done or if you dont want : "))
l = []
l1 = []
while a == True:
    b = input("enter the food or drink item you want : ")
    if b in d.keys() or b in d1.keys():
        l.append(b)
        a = input("enter 1 if you want to add food, or else enter 0 if you are done or if you dont want : ")
          
    else:
        print("you entered an item which is not in the menu")
        print("please double check or enter an item from the menu")
for j in l:
    if j in d.keys():
        l1.append(d[j])
    elif j in d1.keys():
        l1.append(d1[j])
for k in l1:
    add = add + k



print("-"*100)
print(" "*40,"vikas bar and grill"," "*40)
print(" "*42,"st cloud, mn"," "*40)
print(" "*40,"united states, 56301"," "*40)
x = datetime.datetime.now()
print(" "*40,x)
print("-"*100)

for x in range(len(l)):
    print(l[x]," "*15,l1[x])

print("-"*100)
print(" "*5,"total bill",add)
gst = add * 0.18
print(" "*5,"tax",gst)
add = add + gst
print(" "*5,"final bill with tax",add)




    

        
