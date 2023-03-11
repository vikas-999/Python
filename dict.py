'''
l = ["facebook","facebook", "instagram", "whatsapp", "uber", "ola","ichat"]
l2 = [2,4,6,8,10,1]
d = {}
for i in l:
    if i[0] not in d:
        d[i[0]]=i
    else:
        d[i[0]] = i
print(d)
    
        

a = 0
b = 1
while a < 20:
    c = a + b
    a = b
    b = c 
print(c)

'''
#10.  WAP to strip the characters without using strip
s = "####assesment # day####"
a = "##"
length = len(a)
s1 = ""
if s[0:length:1] == a and s[-1:-length-1:-1] == a:
    for i in s:
        s1 = s1+i
print(s1[length:-length:1])


