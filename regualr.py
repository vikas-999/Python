import re

s = "hello world welcome to my python class and hello again"
print(re.findall("hello",s))
print(re.findall("w",s))
print(re.findall("h",s))
print(re.findall("python",s))

print(re.findall(r".","hello how you doin!@#"))
print(re.findall(r"a.b","axyzb"))
print(re.findall(r"a.b","acb"))
print(re.findall(r"a.b","a b"))
print(re.findall(r"a.b","a.b"))
print(re.findall(r"a.b","how are acb doing"))
print(re.findall(r"a.b","abhi"))

print(re.findall(r"a..b","acvb"))
print(re.findall(r"v...s","vikas"))


# caps symbol (^) at  the start
s="hello how are you doing hello again"
print(re.findall(r"hello",s))
print(re.findall(r"^hello",s))

# caps symbol ($) at the end
s="hello how are you doing hello"
print(re.findall(r"hello",s))
print(re.findall(r"hello$",s))
print(re.findall(r"hello$","hello how are you doing hello again"))

# *
print(re.findall(r"v.*s","vikas"))
print(re.findall(r"v.*s","vs"))
print(re.findall(r"vi*s","vs"))
print(re.findall(r"an*a","aa"))
print(re.findall(r"v*s","vikas"))
print(re.findall(r"an*a","annnnnnna"))
print(re.findall(r".*","qwreyaiiaoao"))

# ?
print(re.findall(r"an?a","aa"))
print(re.findall(r"an?a","ana"))
print(re.findall(r"an?a","anna"))
print(re.findall(r"colour?","orange color is my favourite colour and colour"))

# +
print(re.findall(r"an+a","aa"))
print(re.findall(r"an+a","ana"))
print(re.findall(r"an+a","anna"))
print(re.findall(r"an+a","annnnnna"))
print(re.findall(r"an+a","anmmma"))

# eg
url1 = "http://www.google.com"
url2 = "https://www.google.com"
print(re.findall("http",url1))
print(re.findall("http",url2))
print(re.findall("https?",url1))
print(re.findall("https?",url2))

a = "hello dude how is it goging"
print(re.findall(r"[aeiou]", a))
print(len(re.findall(r"[aeiou]", a)))

#matching range of characters
print(re.findall(r"[0-9]","the cost of this book is rs.1000"))
print(re.findall(r"[0123456789]","the cost of this book is rs.1000"))
print(re.findall(r"[a-z]","the cost of this book is rs.1000"))
print(re.findall(r"\d","the cost of this book is rs.1000"))

print(re.findall(r"[0-9]+","the cost of this book is rs.1000 or 50% off on limited"))
print(re.findall(r"\d+","the cost of this book is rs.1000"))


#matching upper case alphabets individually
print(re.findall(r"[a-z]","THIS is a PYthon PROgraming class"))
print(re.findall(r"[A-Z]","THIS is a PYthon PROgraming CLASS"))
print(re.findall(r"[a-z]+","THIS is a PYthon PROgraming class"))
print(re.findall(r"[A-Z]+","THIS is a PYthon PROgraming CLASS"))
print(re.findall(r"[A-Za-z0-9]","THIS is a 465000 PYthon PROgraming CLASS"))

#counting number of spaces \s
print(re.findall(r"\s","THIS is a PYthon PROgraming CLASS"))
print(re.findall(r"\S","THIS is a !@#$%^&* PYthon PROgraming CLASS"))

#words strating with p and j
s = "python is a programming lanaguage python is easier than java"
print(re.findall(r"[pj][a-zA-Z]+",s))
print(re.findall(r"\b[pj][a-zA-Z]+",s))

#words ending with y

a = "hai how are you happy happy birthday"
print(re.findall(r"[a-z]+y",a))
print(re.findall(r"[a-z]+y\b",a))
print(re.sub(r"\s","\n",a))