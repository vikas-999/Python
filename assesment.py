
#1. WAP to create a dictionary and count number of occurance of characters in a string without using built-in function.
string = 'hello good morning'
d = {}
count = 0
for i in range(len(string)):
    count = 0
    for j in string:
        if string[i] == j:
            count+=1
    d[string[i]] = count
print(d)


     


#2. WAP to count no of digits and alphabets and space in a given string.
string = 'India got Independence on August 15 1947'
space_count = 0
digit_count = 0
alpha_count = 0
for i in string:
    if i.isspace() == True:
        space_count+=1
    elif i.isdigit() == True:
        digit_count+=1
    elif i.isalpha() == True:
        alpha_count+=1
    else:
        print("nothing")
print(space_count,"spaces in the string")
print(digit_count,"digits in the string")
print(alpha_count,"alphabets in the string")



#3. WAP to print repetative characters in a  string.
sentence = 'hello welcome to python'
s = ""
for i in sentence:
    if sentence.count(i) > 2:
        print(i)
        
   
    
    
    



#4. WAP to print dupliacte characters and non-duplicate characters using inbuilt function.
string = 'hello python'
dup = ""
nodup = ""
for i in string:
    if string.count(i) < 2:
        dup = dup + i
    else:
        nodup = nodup + i
print(dup,nodup,sep = "\n")




#5. WAP to print 2nd occurance of the given substring.
s = input("enter a string: ")
count = 0
substr = input("enter a character: ")
for i in range(len(s)):
    if s[i] == substr:
        count=count+1
        if count == 2:
            print(i)





#6. WAP to create a list with even length words
string = 'India got Independence on August 15 1947'
l = string.split()
l1 =[]
for i in l:
    if len(i)%2 == 0:
        l1.append(i)
print(l1)
        
    


#7.   WAP to print prime numbers from 1-20
for i in range(1,20):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)
        

#8.  WAP to get given output .
#I/p : [ sun flower, lilly flower, Marigold flower, lotus flower, lion animal, tiger animal, cat animal, tulasi plant, cow animal, money plant]

#O/p: {animal : [tiger, cat, cow, lion], flower: [sun, lilly.........], Plant: [money, tulasi]}

l = [ "sun flower", "lilly flower", "Marigold flower", "lotus flower", "lion animal", "tiger animal", "cat animal", "tulasi plant", "cow animal", "money plant"]
d = dict()
l2 =[]
l3 =[]
l4 = []
for i in l:
    if i not in d:
        if i.endswith("flower"):
            l2.append(i)
            d["flower"] = l2
        elif i.endswith("animal"):
            l3.append(i)
            d["animal"] = l3
        else:
            l4.append(i)
            d["plant"] = l4
print(d)


#9. WAP to get dictionary having first char of word as key and list containing words starting with that char.
#Take a list having 5 words.
l =["python","php","omegle","ola","netflix"]
d = {}
l1 =[]
l2 =[]
l3 = []
for i in l:
    if i not in d:
        if i.startswith("p"):
            l1.append(i)
            d["p"] = l1
        elif i.startswith("o"):
            l2.append(i)
            d["o"] = l2
        else:
            l3.append(i)
            d["n"] = l3
print(d)
            


#10.  WAP to strip the characters without using strip
s = "####assesment # day####"
a = "##"
length = len(a)
s1 = ""
if s[0:length:1] == a and s[-1:-length-1:-1] == a:
    for i in s:
        s1 = s1+i
print(s1[length:-length:1])


  
 
#11.  WAP to print first 10 prime numbers.
for i in range(1,11):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)
            




#12. WAP to extend a list without using inbuilt method.
l = [1,2,3,4,5]
t = (1,2,3)
for i in t:
    l.append(i)
print(l)


#13.  WAP to print alternative alphabets (upper case)
s = "hello world"
s1 =""
for i in range(len(s)):
    if i%2 == 0:
        s1 = s1 + s[i].upper()
    else:
        s1 = s1 + s[i]
print(s1)



#14. WAP to print alphabets like AaBbCcDdEe............Zz.
s = "abcdefghijklmnopqrstuvwxyz"
s2 = ""
for i in s:
    s2 = s2 + i.upper() + i
print(s2)
    

#15. Take two lists remove common elements in both and return a list of unique elements
l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [2,4,6,8,10]
l3 = []
for i in range(len(l1)):
    if l1[i] in l1 and l1[i] in l2:
        l3.append(i)
print(l3)


