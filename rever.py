'''
def convert_(string):
        s = reversed(string)
        a = ""
        for i in s:
                a+=i
        return a
print(convert_("hello"))


s = input("enter a string: ")
count = 0
substr = input("enter a character: ")
for i in range(len(s)):
    if s[i] == substr:
        count=count+1
        if count == 2:
            print(i)


'''

def append_(l,e):
        
        
