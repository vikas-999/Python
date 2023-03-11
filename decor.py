'''
def sq_li(func):
    def inner(a):
        l = []
        for i in a:
            l.append(i*i)
        print("square of the numbers in list are : ",l)
        return func
    return inner

@sq_li
def li(a):
    print(a)
n = [2,4,6,8,10]
li(n)

def smart(func):
    def inner_smart(*args,**kwargs):
        print("The addition of two numbers is : ",end="")
        func(*args,**kwargs)
    return inner_smart

@smart
def add(a,b):
    print(a+b)

add(13,11)

#wadf to calculate no of characters and number of words
def o_char(func):
    def i_char(*args,**kwargs):
        func(*args)
        for i in args:
            print(f"Number of charcater in the string are : {len(i)}")
            print(f"Number of words in the string are : {len(i.split())}")

    return i_char
@o_char
def char_(s):
    print(s)
char_("hey how you doin")


def outer(func):
    def wrapper(*args,**kwargs):
        c=0
        for i in args:
            c+=1
        print("The addition of all numbers is : ",end="")
        func(*args,**kwargs)
        print(f"{c} is the count of all numbers")
    return wrapper

@outer
def add(a,b,c,d):
    print(a+b+c+d)
add(10,20,10,30)
#=======================================================
c = 0
def outer(func):
    def wrapper(*args,**kwargs):
        global c
        c +=1
        print("The addition of all numbers is : ",end="")
        func(*args,**kwargs)
    return wrapper

@outer
def add(a,b):
    print(a+b)
add(10,20)
add(11,21)
add(12,22)
add(13,24)

print(f"{c} is the count")

def up(func):
    def inup(*args,**kwargs):
        c = 0
        for i in args[0]:
            if "A" <= i <= "Z":
                c+=1
        print(f"There are {c} upper case in the given string")
    return inup

@up
def msg(s,m):
    print(s)
msg("PROgramING")
'''