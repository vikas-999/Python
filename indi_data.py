#data types
'''
datatypes defines the type of data stored in the memory address(i.e., variables)
we don't need to define the data while we are declaring it
because python is the dynamic typed language. it is automatically going to bind the data with its type

there are two types of data types
1. individual datatype
2. collection datatype

integer, boolean, float , complex comes under individual datatype
string,tuple,list,set,dictionary comes under collection dataype

'''
# integer default value is 0
a = 54
b = 11

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)

print(type(a))
print(type(b))
a = -10
print(abs(a))

print(dir(int))

#float default value is 0.0
a = 54.6
b = 11.5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)

print(round(a))
from math import trunc
print(trunc(a))

a = 10.9
print(abs(a))
a = -10.9
print(abs(a))


print(dir(float))

#complex default value is 0j
a = 2+3j
print(type(a))
b = complex(2,5)
print(b)
c = complex(2+5, 5+7)
print(c)

print(dir(complex))


x = 5+ 10j
y = 6+ 12j
print(x+y)
print(x-y)
print(x*y)
print(x/y)
# print(x//y) we cannot do floor divison in complex

z = 10 + 100j
print(abs(z))

#boolean
# default value for true is 1
# default value for false is 0

a = 10
j = 11
k = 12

b = []
i = 0
print(bool(a))
print(bool(b))
print(bool(i))
print(bool(j))
print(bool(k))

print(isinstance(10,int))
print(isinstance(10.0,int))
print(isinstance(10.11,float))
print(isinstance((10, 10.8, True),(int, float, bool, complex)))
print(isinstance(10,(int,float,bool,complex)))
print(isinstance(10,(float,bool,complex)))

print(dir(bool))





