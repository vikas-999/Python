'''
#questions
#1.wap to returns a list of name starting with vowels using comprehension
a = ["john", "ive", "alex", "bob", "apple", "steve", "acott"]
b = [i for i in a if i[0] in "aeiouAEIOU"]
print(b)


#2.wap to flip the keys and values of the dictionary using dict comprehension
d = {"a":1, "b":"hello","c":85, "d":12.3, "e":"[1,2,3]"}
d1 = {j:i for i,j in d.items()}
print(d1)

    



# 3.waf to search for a character in a given string and return the corresponding index
def charecter(s,sub):
    for i in range(len(s)):
        if sub == s[i]:
            print(i)
charecter("hello","l")

#4.waf to count the number of positional and keyword arguments passed to it
def fun(*args,**kwargs):
    return f"There are {len(args)} : positional arguments and , {len(kwargs)} : functional arguments"
print(fun(12,15,17,a = 13,b=14))


#5.write a function to check if the given number is fibonacci number
def fib(n):
    a = 0
    b = 1
    while b < n:
        c = a + b
        print(c)
        a = b
        b = c
fib(10)
    


#6.wap to create a dictionary with word and its count pair using comprehension
sentence= "hello haii how are you"
d = {i : sentence.count(i) for i in sentence}
print(d)
    


#7.wap to reverse a item of list if the list is of odd length string ,otherwise keep 
#the item as it is using comprehension
l = ["apple", "google","flipkart", "goibibo", "dunzo", "zomato", "swiggy"]
a = [i if len(i)%2==0 else i[::-1] for i in l]
print(a)



#8.waf to add a element to a list at first index by unpacking given iterable
def _insert(pos,col):
    l = [2,4,6,8,10]
    for i in col:
        l.insert(pos,i)
    print(l)
_insert(1,[3,5])
    
    

#9.waf to return a reversed string
def rev(s):
    s1 = ""
    for i in s:
        s1 = i+s1
    print(s1)
rev("hello")

#10.wap to raise the power of list index
l = [1, 2, 3, 4, 5, 6]
l1 = []
for i in range(len(l)):
    l1.append(l[i]**i)
print(l1)
    
    

#11.wap to grouping cars and bikes in below list 
l = ["honda-bike","audi-car", "bmw-car","apache-bike", "bullet-bike","skoda-car"]
d = {}
l1 = []
l2 = []
for i in l:
    if i.endswith("bike"):
        l1.append(i[0:-5:1])
        d['bike'] = l1
    else:
        l2.append(i[0:-4:1])
        d['car'] = l2
print(d)



#12.writa a function to print the largestnumber in the given list
def largestnumber(l):
    return max(l)
print(largestnumber([1,2,45,6,19]))

#or
def largestnumber(l):
    a = l[0]
    for i in l:
        if a < i:
            a = i
    print(a)

largestnumber([1,2,45,6,19])
        
        



#13.waf to filtering out those names which are less than 6 characters
def filter(l):
    for i in l:
        if len(i) > 6:
            print(i)
filter(["vikas","balavikas","kohli","virat kohli"])
    


#14.waf to check the names starting with consonants
def consonantCheck(l):
    for i in l:
        if i[0] not in "aeiouAEIOU":
            print(i, " starts with consonant")
consonantCheck(["apple","xmas","zebra","elephant"])

#15.waf to create a dictionary by makingb one list of elements as key and other list as value
def dictfun(l1,l2):
    d = {}
    for i,j in zip(l1,l2):
        d[i] = j
    print(d)
dictfun([1,2,3],["one","two","three"])

l1 = [10,20,30]
l2 = ["apple", "google","flipkart"]

#16.waf to create  a set of words ending with vowels
def vowels(l):
    l1 = []
    for i in l:
        if i[-1] in "aeiouAEIOU":
            l1.append(i)
    print(l1)
vowels(["website","include","jack"])
          
    


#17.waf to print duplicate characters without using inbuilt method
def dup(s):
    for i in s:
        count = 0
        for j in s:
            if i == j:
                count+=1
        if count > 1:
            print(i,end="")
                
dup("good")
            



#18.waf to remove the duplicates or repeated character  in the string
def remdup(s):
    count = 0
    c = ""
    for i in s:
        if not s.count(i) > 1:
            c = c + i
    print(c)
remdup("hello")
        
'''

l = ["instagram","rood","facebook"]
x = lambda a: [a,len(a)] if len(a)%2 == 0 else "none"
print(list(map(x,l)))



